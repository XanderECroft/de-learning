from pathlib import Path
from typing import Union # added to accept str or path in function def
from datetime import datetime

# Establish Base Directory
BASE_DIR = Path(__file__).parent

# Write a function create_landing_zone(base_dir, sources) that takes a base path and a list 
# of source system names, and creates this directory structure for each source: 
# base/raw/{source}/, base/staging/{source}/, base/archive/{source}/. 
# Call it with base_dir="de-learning/lake" and sources=["orders", "customers", "products"]. 
# Then print the full directory tree using iterdir().

def create_landing_zone(base_dir: Union[str, Path], sources: list[str]) -> None:
    base = Path(base_dir)

    # for source in sources:
    #     raw_dir = base / "raw" / source
    #     staging_dir = base / "staging" / source
    #     archive_dir = base / "archive" / source
    #     raw_dir.mkdir(parents=True, exist_ok=True)
    #     staging_dir.mkdir(parents=True, exist_ok=True)
    #     archive_dir.mkdir(parents=True, exist_ok=True)
    for source in sources:
        for zone in ["raw", "staging", "archive"]:
            (base / zone / source).mkdir(parents=True, exist_ok=True)

    for p in sorted(base.rglob("*")):
        depth = len(p.relative_to(base).parts) - 1
        indent = "  " * depth
        print(f"{indent}{p.name} — {'dir' if p.is_dir() else 'file'}")

base_dir=BASE_DIR.parent / "lake"
sources=["orders", "customers", "products"]
create_landing_zone(base_dir, sources)

# File Processor with glob
# Write a script that: (1) creates 5 CSV files in week2/data/raw/orders/ named 
# orders_2024-01-01.csv through orders_2024-01-05.csv, each with a header and 3 data rows, 
# (2) uses glob("orders_*.csv") to find all of them sorted chronologically, (3) reads each 
# file, counts rows, and prints a processing log. This is exactly how a real ingestion 
# pipeline discovers files in a landing zone.
# Create a few test files to glob over
base = BASE_DIR/ "data/raw/orders/"
base.mkdir(parents=True, exist_ok=True)
for order_dates in ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"]:
    (base / f"orders_{order_dates}.csv").write_text("order_id,amount\n1,100\n2,200\n3,300\n",encoding="utf-8")

csv_files = list(base.glob("*.csv"))
print(f"Found {len(csv_files)} CSV files:")
for f in sorted(csv_files):
    contents = f.read_text(encoding="utf-8").splitlines()
    row_count = len(contents) - 1  # subtract header
    print(f"{f.name} processed - {row_count} rows read.")


# Archive mover
# Write a function archive_processed(source_dir, archive_dir, pattern="*.csv") that: finds 
# all files matching the pattern in source_dir, moves each one to archive_dir (using 
# Path.rename()), and returns a list of the files moved. Handle the case where a file with 
# the same name already exists in the archive (append a timestamp to avoid overwriting). 
# Test by processing your 5 order files from exercise 2.
def archive_processed(source_dir: Union[str, Path], archive_dir: Union[str, Path], pattern="*.csv") -> list:
    source_path = Path(source_dir)
    archive_base = Path(archive_dir)
    file_inventory=[]

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    for f in source_path.glob(pattern):
        archive_path = archive_base / f"{f.name}_{timestamp}"
        f.rename(archive_path)
        file_inventory.append(f.name)

    return file_inventory

archive = BASE_DIR/ "data/archive"
archive.mkdir(parents=True, exist_ok=True)
archived_files = archive_processed(BASE_DIR/ "data/raw/orders/", archive)
print(f"Archived {len(archived_files)} files:")
for fname in archived_files:
    print(f"  {fname}")