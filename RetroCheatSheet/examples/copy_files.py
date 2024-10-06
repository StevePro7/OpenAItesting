import os.path
import shutil


def get_files(dirX: str) -> list:
    file: str = f"copy_{dirX}.txt"
    with open(file, 'r') as fh:
        files = fh.readlines()
    return files


def copy_file(file, extn: str):
    path: str = os.path.abspath(os.path.dirname(__file__))
    print(f"Starting file copy '{file}'")
    srce: str = f"{path}/../data/stable/{file}/rom.{extn}"
    dest: str = f"{path}/../.venv/lib/python3.8/site-packages/retro/data/stable/{file}/rom.{extn}"
    shutil.copy(srce, dest)
    print(f"Complete file copy '{file}'")


def process(dirX, extn: str) -> None:
    files: list = get_files(dirX)
    for file in files:
        file = file.strip()
        copy_file(file, extn)


if __name__ == '__main__':
    process("Sms", "sms")
    process("Genesis", "md")
