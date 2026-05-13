from pathlib import Path

base = Path("week2")

# Create a few test files to glob over
for month in ["2024-01", "2024-02", "2024-03"]:
    (base / f"orders_{month}.csv").write_text(f"order_id,amount\n1,100\n")
(base / "config.json").write_text("{}")
(base / "README.md").write_text("# notes")

# glob: find files matching a pattern
csv_files = list(base.glob("*.csv"))
print(f"Found {len(csv_files)} CSV files:")
for f in sorted(csv_files):
    print(f"  {f.name}")

# glob with subdirectories
all_csvs = list(base.rglob("**/*.csv"))   # recursive

# Sort files by name (gets you chronological order if names are dated)
ordered = sorted(base.glob("orders_*.csv"), key=lambda p: p.stem)
print("\nOrdered order files:")
for f in ordered:
    print(f"  {f.stem}")