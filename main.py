from src.app import App
from os import path
from sys import platform



if __name__ == '__main__':
    config_file_path = path.join(path.dirname(__file__), 'src', 'data')
    config_file_name = 'config.json'
    icon_file_path = path.join(path.dirname(__file__), 'src', 'assets', 'icon.png')
    log_file_path = path.join(path.dirname(__file__), 'src', 'log')
    app = App('Desktop Organizer', config_file_path, config_file_name, log_file_path, icon_file_path, 990, 450)
    app.build_ui()
    app.run()