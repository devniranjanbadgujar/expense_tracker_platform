from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

FILES_TO_CHECK = [
    PROJECT_ROOT / "backend" / ".env",
    PROJECT_ROOT / "backend" / "Dockerfile",
    PROJECT_ROOT / "compose" / "docker-compose.yml"
]

print("=" * 50)
print("Expense tracker health report")
print("=" * 50)

print(f"Project root: {PROJECT_ROOT}")

for file in FILES_TO_CHECK:

    if file.exists():
        print(f"[PASS] {file.name}")
    else:
        print(f"[FAIL] {file.name}")