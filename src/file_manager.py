from os.path import (
    isdir, 
    isfile, 
    join
)
from os import (
    mkdir, 
    listdir, 
    getlogin
)
from shutil import move
from pathlib import Path

class FileManager:
    def create_dir(self, path):
        try:
            mkdir(path)
        except Exception as e:
            print(str(e))

    def create_file(self, path, file_content: str | None = None):
        with open(path, 'w') as f: 
            if file_content is not None and file_content.strip() != '':
                f.write(file_content)
    
    def dir_exists(self, path):
        return isdir(path)
    
    def file_exists(self, path):
        return isfile(path)
    
    def write_file(self, path, permission, file_content):
        with open(path, permission) as f:
            f.write(file_content)

    def move_file(self, dir_path: str, file_name: str, new_dir: str):
        try:
            file_path = join(dir_path, file_name)
            new_file_path = join(new_dir, file_name)
            move(file_path, new_file_path)
        except PermissionError as e:
            return str(e)

    def list_dir(self, path: str):
        """
        list all files in a specified dir
        """
        return listdir(path)
    
    def get_drive_letter(self):
        """
        get the current drive letter
        e.g. "C:"
        """
        return Path.home().drive
    
    def get_current_active_user(self):
        return getlogin()