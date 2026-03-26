"""Generate lecture and project notebooks from the script sources."""

from __future__ import annotations

import ast
from pathlib import Path
from textwrap import dedent

import nbformat as nbf


LECTURE_METADATA = {
    "lecture_01_qubits.py": {
        "notes": "CS4268_Scribe_Notes/Lecture1 Final Notes.tex",
        "focus": "basis states, superposition, and measurement",
        "predict": [
            "What amplitudes should H|0> have?",
            "Why does measuring |+> look random in the computational basis?",
        ],
    },
    "lecture_02_bases_and_unitaries.py": {
        "notes": "CS4268_Scribe_Notes/Lecture2 Final Notes.tex",
        "focus": "basis changes, unitary gates, and phase",
        "predict": [
            "Which states are deterministic in the X basis?",
            "Why can two states share Z-basis probabilities but differ by phase?",
        ],
    },
    "lecture_03_composite_systems.py": {
        "notes": "CS4268_Scribe_Notes/Lecture3 Final Notes.tex",
        "focus": "tensor products, Bell states, and subsystem behavior",
        "predict": [
            "How are |01> and |10> ordered?",
            "Why are Bell-state marginals uniform?",
        ],
    },
    "lecture_04_teleportation_and_reversible.py": {
        "notes": "CS4268_Scribe_Notes/Lecture4 Final Notes.tex",
        "focus": "no-cloning, teleportation, and reversible logic",
        "predict": [
            "Why does CNOT fail as a universal copier?",
            "Which classical bits determine Bob's correction?",
        ],
    },
    "lecture_05_primitives.py": {
        "notes": "CS4268_Scribe_Notes/Lecture5 Final Notes.tex",
        "focus": "uncomputation, phase kickback, and Hadamard-Walsh",
        "predict": [
            "Which ancilla returns to |0> after uncomputation?",
            "Which basis state picks up a minus sign in the kickback demo?",
        ],
    },
    "lecture_06_deutsch_jozsa_bv.py": {
        "notes": "CS4268_Scribe_Notes/Lecture6 Final Notes.tex",
        "focus": "Deutsch, Deutsch-Jozsa, and Bernstein-Vazirani",
        "predict": [
            "What measurement separates constant from balanced oracles?",
            "Why does BV recover the secret exactly?",
        ],
    },
    "lecture_07_qft.py": {
        "notes": "CS4268_Scribe_Notes/Lecture7 Final Notes.tex",
        "focus": "hand-built QFT circuits and phase structure",
        "predict": [
            "How does QFT differ from H⊗n?",
            "Why do swaps appear at the end of the standard circuit?",
        ],
    },
    "lecture_08_simon.py": {
        "notes": "CS4268_Scribe_Notes/Lecture8 Final Notes.tex",
        "focus": "hidden xor structure and classical post-processing",
        "predict": [
            "Which rows satisfy y . s = 0?",
            "Why is one nonzero constraint enough for the 2-bit toy case?",
        ],
    },
    "lecture_09_order_finding.py": {
        "notes": "CS4268_Scribe_Notes/Lecture9 Scribe Template.tex",
        "focus": "periodicity and Fourier peaks",
        "predict": [
            "Where should the peaks appear if the period is 4?",
            "Why does periodic structure become sparse in the Fourier basis?",
        ],
    },
    "lecture_10_shor_scaffold.py": {
        "notes": "CS4268_Scribe_Notes/Lecture10 Scribe Template.tex",
        "focus": "continued fractions, order recovery, and factor extraction",
        "predict": [
            "Why can one peak give a bad denominator candidate?",
            "Why does an even order matter for factor recovery?",
        ],
    },
}


PROJECT_METADATA = {
    "project_teleportation_diagnostics.py": {
        "source": "Lecture 4",
        "focus": "branch-by-branch teleportation analysis and correction checks",
    },
    "project_bv_oracle_workbench.py": {
        "source": "Lecture 6",
        "focus": "secret sweeps and exact Bernstein-Vazirani recovery",
    },
    "project_simon_hidden_structure.py": {
        "source": "Lecture 8",
        "focus": "a larger Simon toy instance with nontrivial post-processing",
    },
    "project_shor_factor_15.py": {
        "source": "Lectures 9-10",
        "focus": "idealized order finding plus Shor post-processing on N = 15",
    },
}


def extract_parts(script_path: Path) -> tuple[str, str, str]:
    source = script_path.read_text()
    tree = ast.parse(source)
    lines = source.splitlines()

    docstring = ast.get_docstring(tree) or script_path.stem
    start_after_docstring = 0
    if (
        tree.body
        and isinstance(tree.body[0], ast.Expr)
        and isinstance(tree.body[0].value, ast.Constant)
        and isinstance(tree.body[0].value.value, str)
    ):
        start_after_docstring = tree.body[0].end_lineno or 0

    main_node = next(
        node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main"
    )
    prelude = dedent("\n".join(lines[start_after_docstring : main_node.lineno - 1])).strip()
    main_body = dedent("\n".join(lines[main_node.body[0].lineno - 1 : main_node.end_lineno])).strip()
    return docstring, prelude, main_body


def lecture_markdown(script_name: str, title_text: str) -> str:
    metadata = LECTURE_METADATA[script_name]
    predictions = "\n".join(f"- {item}" for item in metadata["predict"])
    return (
        f"# {title_text}\n\n"
        f"Matching notes: `{metadata['notes']}`\n\n"
        f"Focus: {metadata['focus']}.\n\n"
        f"Before running the code, predict:\n{predictions}"
    )


def project_markdown(script_name: str, title_text: str) -> str:
    metadata = PROJECT_METADATA[script_name]
    return (
        f"# {title_text}\n\n"
        f"Source lecture block: {metadata['source']}\n\n"
        f"Project focus: {metadata['focus']}."
    )


def make_notebook(title_text: str, intro_markdown: str, prelude: str, main_body: str) -> nbf.NotebookNode:
    notebook = nbf.v4.new_notebook()
    notebook.metadata["kernelspec"] = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    }
    notebook.metadata["language_info"] = {"name": "python"}
    notebook.cells = [nbf.v4.new_markdown_cell(intro_markdown)]
    if prelude:
        notebook.cells.append(nbf.v4.new_code_cell(prelude))
    notebook.cells.append(nbf.v4.new_code_cell(main_body))
    return notebook


def generate_from_directory(source_dir: Path, target_dir: Path, metadata_mode: str) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    for script_path in sorted(source_dir.glob("*.py")):
        title_text, prelude, main_body = extract_parts(script_path)
        if metadata_mode == "lecture":
            intro = lecture_markdown(script_path.name, title_text)
        else:
            intro = project_markdown(script_path.name, title_text)
        notebook = make_notebook(title_text, intro, prelude, main_body)
        output_path = target_dir / f"{script_path.stem}.ipynb"
        output_path.write_text(nbf.writes(notebook))
        print(f"wrote {output_path}")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    generate_from_directory(repo_root / "labs", repo_root / "notebooks" / "lectures", "lecture")
    generate_from_directory(repo_root / "projects", repo_root / "notebooks" / "projects", "project")


if __name__ == "__main__":
    main()
