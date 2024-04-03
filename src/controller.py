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
        try:
            file_path = path.join(dir_path, file_name)
            new_file_path = path.join(new_dir, file_name)
            move(file_path, new_file_path)
        except Exception as e:
            print(str(e))

    def load_config(self):
        file_path = path.relpath(self.config_file_path)
        with open(file_path, 'r') as f:
            self.config = load(f)
        
    def save_config(self, file_path):
        file_path = path.relpath(file_path)
        with open(file_path, 'w') as f:
            dump(obj= self.config, fp=f, indent=4)
    
    def get_config(self, config_ref):
        return self.config[config_ref]

    def target_list_to_string(self, target_list: list):
        return "\n".join(target_list)
    
    def string_to_target_list(self, string):
        return string.split("\n")
    
    def set_value_by_key_chain(self, key_chain, new_value):
        keys = key_chain.split(".")
        current_dict: dict = self.config
        for key in keys[:-1]:
            current_dict = current_dict.setdefault(key, {})
        current_dict[keys[-1]] = new_value
    
    def update_config(self, id: str, value):
        self.set_value_by_key_chain(id, value)
        self.save_config(self.config_file_path)

    def update_target_list(self, target_list_string: str):
        new_target_list = target_list_string.split("\n")
        self.set_value_by_key_chain("target_list", new_target_list)
        self.save_config(self.config_file_path)

    def execute_file_movement(self, file_path: str, file_name: str, allowed_file_extensions: list, new_dir):
        file_parts = file_name.split(".")
        if file_parts[-1] in allowed_file_extensions:
            print("file to move: " + file_name)
            self.move_file(file_path, file_name, new_dir)

    def execute_file_movements(self):
        options: dict = self.get_config("type_config")
        for path in self.get_config("target_list"):
            for option in options:
                if 1 in options[option]["file_extensions"].values():
                    new_dir = options[option]["new_dir"]
                    file_extensions = list(options[option]["file_extensions"].keys())
                    print(new_dir)
                    print(file_extensions)
                    files = self.list_files(path)
                    print(files)
                    for file in files:
                        self.execute_file_movement(path, file, file_extensions, new_dir)