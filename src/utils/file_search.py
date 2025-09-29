import os


def find_file(root: str = r'c:\Users\User\Documents\Templates', filename: str = '') -> str | Exception:
    for dirpath, dirnames, filenames in os.walk(root):
        if filename in filenames:
            return os.path.join(dirpath, filename)

    return None