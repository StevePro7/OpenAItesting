import os.path
import shutil


def get_lines(dirX: str) -> list:
    file: str = f"copy_{dirX}.txt"
    with open(file, 'r') as fh:
        lines = fh.readlines()
    return lines


def foo(dirX, extn: str) -> None:
    files: list = get_lines(dirX)
    for file in files:
        file = file.strip()
        bar(file, extn)
        #print(file)


def bar(file, extn: str):
    path: str = os.path.abspath(os.path.dirname(__file__))
    print(f"{file} beg")
    srce: str = f"{path}/../data/stable/{file}/rom.{extn}"
    dest: str = f"{path}/.venv/lib/python3.8/site-packages/retro/data/stable/{file}/rom.{extn}"
    shutil.copy(srce, dest)
    print(f"{file} end")

if __name__ == '__main__':
    foo("Sms", "sms")
    foo("Genesis", "md")


