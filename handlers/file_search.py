import os


def find_file(root: str = os.curdir, filename: str = '') -> str:
    for dirpath, dirnames, filenames in os.walk(root):
        if filename in filenames:
            return os.path.join(dirpath, filename)

    return None