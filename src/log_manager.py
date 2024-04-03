from os.path import isdir, join, isfile
from os import mkdir
from datetime import datetime


class LogManager:

    log_dir: str = ''
    error_log_name: str = ''
    def __init__(self, log_dir, error_log_name):
        self.log_dir = log_dir
        self.error_log_name = error_log_name

    def init(self):
        """
        checks for log dir and log files and creates them if needed
        """

        #check for log dir
        log_dir_exists = self.log_dir_exists(self.log_dir)
        if not log_dir_exists:
            self.create_dir(self.log_dir)

        #check for error log
        error_log_file_path = join(self.log_dir, self.error_log_name)
        error_log_exists = self.file_exists(error_log_file_path)
        if not error_log_exists:
            self.create_file(error_log_file_path)


    def create_dir(self, path):
        mkdir(path)

    def create_file(self, path):
        with open(path, 'w'): 
            pass
    
    def log_dir_exists(self, path):
        return isdir(path)
    
    def file_exists(self, path):
        return isfile(path)
    
    def log_error(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_log_file_path = join(self.log_dir, self.error_log_name)
        with open(error_log_file_path, 'a') as f:
            f.write(f'[{timestamp}]: {message}\n')