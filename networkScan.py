import subprocess
import platform
import sys

def ping_address(ip: str) -> bool:
    flag = "-n" if platform.system().lower() == "windows" else "-c"

    result = subprocess.run(
        ["ping", flag, "1", ip],
        stdout=subprocess.PIPE,   # ← capture output now
        stderr=subprocess.DEVNULL
    )
    output = result.stdout.decode().lower()  # convert to readable text

    # Windows fix — check for unreachable in the output
    if "unreachable" in output or "timed out" in output:
        return False

    return result.returncode == 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python networkScan.py <ip>")
        print("Example: python networkScan.py 8.8.8.8")
        sys.exit(1)

    ip = sys.argv[1]  

    if ping_address(ip):
        print(f"{ip} is UP")
    else:
        print(f"{ip} is DOWN")
