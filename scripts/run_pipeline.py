import subprocess
import sys
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
STEPS = ["ingest.py", "clean.py", "transform.py", "warehouse.py", "data_quality.py", "archive.py", "performance.py"]

def main():
    for step in STEPS:
        print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] running {step}")
        subprocess.run([sys.executable, str(SCRIPTS_DIR / step)], check=True)
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] pipeline finished")


if __name__ == "__main__":
    main()