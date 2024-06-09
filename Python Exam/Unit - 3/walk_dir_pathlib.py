from pathlib import Path

if __name__ == "__main__":
    root_dir = Path('.')
    for path in root_dir.rglob('*'):
        print(path)
