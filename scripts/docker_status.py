from platform_utils.command import run_cmd
from platform_utils.command import print_header

print_header()

result = run_cmd(["docker", "ps"])

if result.returncode != 0:
    print("Docker command failed.")
    print(result.stderr)
    exit(1)

print(result.stdout)
lines = result.stdout.splitlines()
container_count = max(0, len(lines) - 1)

if container_count == 0:
    print("WARNING: No running containers detected.")
else:
    print("PASS")
    print(f"Running containers: {container_count}")

print(result.returncode)