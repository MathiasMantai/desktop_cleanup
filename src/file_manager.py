from os.path import isdir, isfile
from os import mkdir

class FileManager:
    def create_dir(self, path):
        mkdir(path)

    def create_file(self, path, file_content: str | None = None):
        with open(path, 'w') as f: 
            if file_content is not None and file_content.strip() != '':
                f.write(file_content)
    
    def dir_exists(self, path):
        return isdir(path)
    
    def file_exists(self, path):
        return isfile(path)