import platform
from json import load, dump, dumps
from os import (
    listdir,
    path
)
from shutil import move
from src.log_manager import LogManager
from src.file_manager import FileManager


class Controller:
    """
    the controller class manages state and data of the app
    """

    config_file_path: str
    config: dict = {}
    log_manager: LogManager
    file_manager: FileManager

    def __init__(self, data_dir, config_file_path: str, config_file_name: str, log_file_path: str):
        self.config_file_path = path.join(config_file_path, config_file_name)

        #file manager
        self.file_manager = FileManager()

        #check data dir
        data_dir_exists = self.file_manager.dir_exists(data_dir)
        print(data_dir_exists)
        if not data_dir_exists:
            self.file_manager.create_dir(data_dir)

        #log manager
        error_log_name = 'error.log'
        self.log_manager = LogManager(self.file_manager, log_file_path, error_log_name)
        self.log_manager.init()

        #check for data dir
        print("config dir: " + config_file_path)
        if not self.file_manager.dir_exists(config_file_path):
            self.file_manager.create_dir(config_file_path)
            
        #check for config json in data dir
        config_file_exists = self.file_manager.file_exists(self.config_file_path)
        if not config_file_exists:
            self.file_manager.create_file(self.config_file_path, dumps(obj=self.default_config_data(), indent=4))

        self.load_config()

        
        #try auto setting fields on first startup
        if self.get_config('first_startup') == 1:
            self.auto_set_new_dir()
            self.auto_set_target_list()
            self.update_config('first_startup', 0)

        

    def list_files(self, dir_path: str):
        return [file for file in listdir(dir_path) if path.isfile(path.join(path.abspath(dir_path), file))]

    def move_file(self, dir_path: str, file_name: str, new_dir: str):
        try:
            file_path = path.join(dir_path, file_name)
            new_file_path = path.join(new_dir, file_name)
            move(file_path, new_file_path)
        except PermissionError as e:
            print(str(e))
            self.log_manager.log_error(str(e))

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

    def execute_file_movements(self):
        type_config: dict = self.get_config("type_config")
        for path in self.get_config("target_list"):
            for option in type_config:
                if 1 in type_config[option]["file_extensions"].values():
                    new_dir = type_config[option]["new_dir"]
                    file_extensions = list(type_config[option]["file_extensions"].keys())
                    files = self.list_files(path)
                    for file in files:
                        file_parts = file.split(".")
                        if file_parts[-1] in file_extensions:
                            rs = self.file_manager.move_file(path, file, new_dir)
                            if rs is not None:
                                self.log_manager.log_error(rs)



    def default_config_data(self):
        """
        defines a default dict that will be used if no config file was found
        """
        return {
            "type_config": {
                "images": {
                    "new_dir": "",
                    "file_extensions": {
                        "jpg": 1,
                        "jpeg": 1,
                        "png": 1,
                        "gif": 0,
                        "bmp": 0,
                        "webp": 0,
                        "svg": 1
                    }
                },
                "documents": {
                    "new_dir": "",
                    "file_extensions": {
                        "txt": 1,
                        "docx": 1,
                        "xlsx": 1,
                        "ods": 1,
                        "csv": 1,
                        "pdf": 1
                    }
                },
                "music": {
                    "new_dir": "",
                    "file_extensions": {
                        "mp3": 0,
                        "mp4": 0
                    }
                }
            },
            "target_list": []
        }
    
    def auto_set_new_dir(self):
        """
        on first startup try to automatically detect 
        """
        drive = self.file_manager.get_drive_letter()
        cur_user = self.file_manager.get_current_active_user()
        plat = platform.system()
        user_path = ""
        if plat == "Windows":
            user_path = path.join(drive, '\\', 'Users', cur_user)
        print(user_path)
        type_config = self.get_config("type_config")
        for key, _ in type_config.items():
            id = "type_config." + key + ".new_dir"
            new_dir = path.join(user_path, key.capitalize())
            self.update_config(id, new_dir)

    def auto_set_target_list(self):
        """
        on first startup try to auto set target dir list for cleanup
        """
        drive = self.file_manager.get_drive_letter()
        cur_user = self.file_manager.get_current_active_user()
        plat = platform.system()
        user_path = ""
        if plat == "Windows":
            user_path = path.join(drive, '\\', 'Users', cur_user)
        print(user_path)
        target_list = [
            user_path,
            path.join(user_path, 'Desktop')
        ]
        id = "target_list"
        self.update_config(id, target_list)