import shutil
from pathlib import Path
from datetime import datetime
import sys

# command line arguments
source_directory = Path(sys.argv[1])
backup_directory = Path(sys.argv[2])

backup_directory.mkdir(exist_ok=True)

log_file = open("backup_log.txt", "a")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


for file in source_directory.iterdir():

    if file.suffix not in [".csv", ".json"]:
        continue

    new_name = f"{file.stem}_{timestamp}{file.suffix}"
    destination = backup_directory / new_name

    shutil.copy2(file, destination)

    log_file.write(f"Copied {file.name} -> {new_name}\n")

    backups = sorted(backup_directory.glob(f"{file.stem}_*{file.suffix}"))

    if len(backups) > 5:
        old_files = backups[:-5]

        for old in old_files:
            old.unlink()
            log_file.write(f"Deleted old backup {old.name}\n")


log_file.close()

print("Backup completed.")