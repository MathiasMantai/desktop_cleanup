from src.app import App
from os import path


if __name__ == '__main__':
    config_file_path = path.join(path.dirname(__file__), 'src', 'data', 'config.json')
    icon_file_path = path.join(path.dirname(__file__), 'src', 'assets', 'icon.png')
    app = App('Desktop Organizer', config_file_path, icon_file_path, 990, 450)
    app.build_ui()
    app.run()