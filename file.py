from json import load
from os import (
    listdir,
    path
)
from shutil import move

def list_files(dir_path: str):
    return [file for file in listdir(dir_path) if path.isfile(path.join(path.abspath(dir_path), file))]

def move_file(dir_path: str, file_name: str, new_dir: str):
    file_path = path.join(dir_path, file_name)
    new_file_path = path.join(new_dir, file_name)
    move(file_path, new_file_path)

def load_config(file_path):
    file_path = path.relpath(file_path)
    with open(file_path, 'r') as f:
        return load(f)