from pathlib import Path

# Build paths with / operator — works on Windows AND Linux
base = Path("week2")
data_dir  = base / "data"
raw_dir   = data_dir / "raw"
out_dir   = data_dir / "output"

# Create directories (like mkdir -p)
raw_dir.mkdir(parents=True, exist_ok=True)
out_dir.mkdir(parents=True, exist_ok=True)

# # Check existence
print(raw_dir.exists())           # True
print((base / "missing").exists())  # False

# # File properties
f = base / "orders.csv"
print(f.name)         # orders.csv
print(f.stem)         # orders       (filename without extension)
print(f.suffix)       # .csv
print(f.parent)       # week2
print(f.resolve())    # full absolute path

# Write and read text files
output_file = out_dir / "report.txt"
output_file.write_text("Pipeline run complete.\nRows: 1500\n", encoding="utf-8")
contents = output_file.read_text(encoding="utf-8")
print(contents)

# List files in a directory
for p in base.iterdir():
    print(p.name, "—", "dir" if p.is_dir() else "file")
