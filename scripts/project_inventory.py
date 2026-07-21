from pathlib import Path
import os
from platform_utils.command import print_header

PROJECT_ROOT = Path(__file__).resolve().parent.parent

print_header()
print("\n")
print(f"Project root: {PROJECT_ROOT}")
print(f"Current working directory: {os.getcwd()}")
print("\n")

dir_count = 0
file_count = 0

for item in PROJECT_ROOT.iterdir():
    if item.is_dir():
        dir_count += 1
        print(f"[DIR] {item.name}")

    else:
        file_count += 1
        print(f"[FILE] {item.name}")

print("\nSummary:")
print(f"Directories: {dir_count}")
print(f"Files: {file_count}")