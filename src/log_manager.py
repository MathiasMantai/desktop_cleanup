from os.path import join
from datetime import datetime
from src.file_manager import FileManager

class LogManager:

    log_dir: str = ''
    error_log_name: str = ''
    file_manager: FileManager
    def __init__(self, file_manager, log_dir, error_log_name):
        self.log_dir = log_dir
        self.error_log_name = error_log_name
        self.file_manager = file_manager

    def init(self):
        """
        checks for log dir and log files and creates them if needed
        """

        #check for log dir
        log_dir_exists = self.file_manager.dir_exists(self.log_dir)
        if not log_dir_exists:
            self.file_manager.create_dir(self.log_dir)

        #check for error log
        error_log_file_path = join(self.log_dir, self.error_log_name)
        error_log_exists = self.file_manager.file_exists(error_log_file_path)
        if not error_log_exists:
            self.file_manager.create_file(error_log_file_path)

    def log_error(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_log_file_path = join(self.log_dir, self.error_log_name)
        with open(error_log_file_path, 'a') as f:
            f.write(f'[{timestamp}]: {message}\n')