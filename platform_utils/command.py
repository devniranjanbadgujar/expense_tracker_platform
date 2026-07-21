import subprocess

def run_cmd(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
    return result

def print_header():

    print("=" * 60)
    print("Docker Health Report")
    print("=" * 60)