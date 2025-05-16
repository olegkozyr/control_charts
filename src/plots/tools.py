import os


def create_directory(dir_path):
    exist = os.path.exists(dir_path)
    if not exist:
        os.makedirs(dir_path)