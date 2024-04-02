from json import load, dump
from os import (
    listdir,
    path
)
from shutil import move

class Controller:
    """
    the controller class manages state and data of the app
    """

    config_file_path: str
    config: dict = {}

    def __init__(self, config_file_path: str):
        self.config_file_path = config_file_path

    def list_files(self, dir_path: str):
        return [file for file in listdir(dir_path) if path.isfile(path.join(path.abspath(dir_path), file))]

    def move_file(self, dir_path: str, file_name: str, new_dir: str):
        file_path = path.join(dir_path, file_name)
        new_file_path = path.join(new_dir, file_name)
        move(file_path, new_file_path)

    def load_config(self):
        file_path = path.relpath(self.config_file_path)
        with open(file_path, 'r') as f:
            self.config = load(f)
        
    def save_config(self, file_path):
        file_path = path.relpath(file_path)
        with open(file_path, 'w') as f:
            dump(self.config, f)
    
    def get_config(self, config_ref):
        return self.config[config_ref]

    def target_list_to_string(self, target_list: list):
        return "\n".join(target_list)
    
    def string_to_target_list(self, string):
        return string.split("\n")
    
    def set_value_by_key_chain(self, key_chain, new_value):
        keys = key_chain.split('_')
        current_dict: dict = self.config
        for key in keys[:-1]:
            current_dict = current_dict.setdefault(key, {})
        current_dict[keys[-1]] = new_value
    
    def update_config(self, id: str, value):
        print(id)
        self.set_value_by_key_chain(id, value)


        print(self.config)