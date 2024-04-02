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
from customtkinter import (
    CTkCheckBox,
    CTkButton,
    CTk,
    CTkTextbox,
    CTkFrame,
    CTkLabel
)
from file import (
    load_config
)
from controller import Controller


class MainFrame(CTkFrame):
    """
    main frame for application
    shows a textarea for paths that should be organized
    and a button to start organizing
    """
    id: str = 'main'
    controller: Controller
    def __init__(self, master=None, controller=None):
        super(MainFrame, self).__init__(master=master)
        self.controller = controller

    def build_ui(self):
        l = CTkLabel(master=self, text='t')
        l.grid(row=0, column=0)

        text = CTkTextbox(master=self, width=500, height= 400, border_spacing = 0)
        text.grid(row=0, column=0)
        text.insert('1.0', text=self.controller.target_list_to_string(self.controller.get_config('target_list')))

    def show_frame(self):
        self.tkraise()

class Config(CTkFrame):
    """
    config frame for application
    show options:
    - which file types to organize 
        - images: jpg, png, gif, bitmap, svg
        - documents: txt, docx, xlsx
        - music: mp3, mp4 
    """

    # vars: list = []
    controller: Controller
    id: str = 'config'
    vars: dict = {}
    chks: dict = {}

    def __init__(self, master=None, controller=None):
        super(Config, self).__init__(master=master)
        self.controller = controller


    def show_frame(self):
        self.tkraise()

    def build_ui(self, padx = 0, pady = 0):
        row = 0

        options = self.controller.get_config("typeconfig")
        for option in options:
            col = 0
            label = CTkLabel(master=self, text=option.capitalize(), padx=padx, pady=pady)
            label.grid(row=row, column=col, padx=padx, pady=pady)
            row += 1
            for item in options[option]:
                id = "typeconfig_" + option + "_" + item
                self.vars[id] = IntVar(value=options[option][item], name=id)
                self.chks[id] = CTkCheckBox(self, text = item, variable=self.vars[id], width=80, checkbox_width=20, checkbox_height=20, command=lambda id=id: self.controller.update_config(id, self.vars[id].get()))
                self.chks[id].grid(row=row, column=col, padx=0, pady=0)
                col += 1
            row += 1
        

class App:

    window: CTk
    frames = {}
    controller: Controller

    def __init__(self, title='App', width = 800, height = 600):
        self.window = CTk()
        # self.window.after(201, )
        self.window.geometry(f'{width}x{height}')
        self.window.title(title)
        self.controller = Controller('config.json')
        self.controller.load_config()
        print(self.controller.config)


    def build_ui(self):
        main = MainFrame(master = self.window, controller = self.controller)
        self.frames[main.id] = main
        main.grid(row=0, column=0, sticky="nsew")

        config = Config(master = self.window, controller = self.controller)
        self.frames[config.id] = config
        config.grid(row=0, column=1, sticky="nsew")

        main.build_ui()
        config.build_ui(5, 5)

        #execute frame
        e_frame = CTkFrame(master=self.window)
        e_frame.grid(row=2, column=0, columnspan = 2, padx=5, pady=10, sticky="nsew")
        #execute button
        execute = CTkButton(master=e_frame, text='Execute', command=self.execute)
        execute.pack()

    def execute(self):
        pass

    def toggle_frame(self, id):
        print("Togggle for frame: " + id)
        self.frames[id].tkraise()

    def run(self):
        self.window.mainloop()