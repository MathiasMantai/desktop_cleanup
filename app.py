from os import listdir
from tkinter import (
    Tk,
    Label,
    Frame,
    Checkbutton,
    IntVar,
    Button,
    Text
)
from file import (
    load_config
)


class MainFrame(Frame):
    """
    main frame for application
    shows a textarea for paths that should be organized
    and a button to start organizing
    """
    id: str = 'main'
    def __init__(self, master=None):
        super(MainFrame, self).__init__(master=master)

    def build_ui(self, controller):
        l = Label(master=self, text='t')
        l.grid(row=0, column=0)

        text = Text()

        config = Button(master=self, text='Config', command=lambda: controller.toggle_frame('config'))
        config.grid(row=0, column=1)

    def show_frame(self):
        self.tkraise()

class Config(Frame):
    """
    config frame for application
    show options:
    - which file types to organize 
        - images: jpg, png, gif, bitmap, svg
        - documents: txt, docx, xlsx
        - music: mp3, mp4 
    """

    vars: list = []
    id: str = 'config'

    def __init__(self, master=None):
        super(Config, self).__init__(master=master)


    def show_frame(self):
        self.tkraise()


    def build_ui(self, options: dict, controller, padx = 0, pady = 0):
        row = 0
        for option in options:
            col = 0
            label = Label(master=self, text=option.capitalize(), padx=padx, pady=pady)
            label.grid(row=row, column=col)
            col += 1
            for item in options[option]:
                var = IntVar()
                chk = Checkbutton(self, text = item, variable=var)
                self.vars.append(var)
                chk.grid(row=row, column=col)
                col += 1
            row += 1
        
        back = Button(master=self, text='Zurück', command=lambda: controller.toggle_frame('main'))
        back.grid(row=row + 1, column = 0, sticky="nsew")
        

class App:

    window: Tk
    config: dict
    frames = {}

    def __init__(self, title='App', width = 800, height = 600):
        self.window = Tk()
        self.window.geometry(f'{width}x{height}')
        self.window.title(title)
        self.config = load_config('config.json')


    def build_ui(self):
        config = Config(self.window)
        self.frames[config.id] = config
        config.grid(row=0, column=0, sticky="nsew")

        main = MainFrame(self.window)
        self.frames[main.id] = main
        main.grid(row=0, column=0, sticky="nsew")

        main.build_ui(self)
        config.build_ui(self.config["type_config"], self, 5, 5)


    def toggle_frame(self, id):
        print("Togggle for frame: " + id)
        self.frames[id].tkraise()

    def run(self):
        self.window.mainloop()