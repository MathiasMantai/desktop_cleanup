from src.app import App
from os import (
    path
)


data_dir = path.dirname(__file__)

if __name__ == '__main__':
    config_file_path = path.join(data_dir, 'src', 'data')
    config_file_name = 'config.json'
    icon_file_path = path.join(path.dirname(__file__), 'src', 'assets', 'icon_32x32.png')
    log_file_path = path.join(data_dir, 'log')
    app = App('Desktop Organizer', data_dir, config_file_path, config_file_name, log_file_path, icon_file_path, 905, 485)
    app.build_ui()
    app.run()