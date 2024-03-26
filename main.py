from app import App
from file import list_files, move_file


if __name__ == '__main__':
    # move_file('C:/Users/mathias/Desktop', 't.txt', 'C:/Users/mathias')
    # print(list_files('C:/Users/mathias/Desktop'))
    app = App('Desktop Organizer', 350, 200)
    app.build_ui()
    app.run()