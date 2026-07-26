import json
from pathlib import Path

notebook_dir = Path("notebooks")
output_file = Path("notebook_audit.txt")

with output_file.open("w", encoding="utf-8") as out:
    for notebook_path in sorted(notebook_dir.glob("*.ipynb")):
        out.write("\n" + "=" * 100 + "\n")
        out.write(f"NOTEBOOK: {notebook_path.name}\n")
        out.write("=" * 100 + "\n\n")

        with notebook_path.open("r", encoding="utf-8") as f:
            notebook = json.load(f)

        for i, cell in enumerate(notebook["cells"], start=1):
            cell_type = cell["cell_type"]
            source = "".join(cell["source"])

            out.write(f"\n--- CELL {i} | {cell_type.upper()} ---\n")
            out.write(source)
            out.write("\n")

            if cell_type == "code" and cell.get("outputs"):
                out.write(f"\n[OUTPUTS PRESENT: {len(cell['outputs'])}]\n")
