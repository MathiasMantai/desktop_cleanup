from customtkinter import (
    CTkButton,
    CTk,
    CTkFrame,
    set_default_color_theme
)
from src.controller import Controller
from PIL.ImageTk import PhotoImage
from src.config import ConfigFrame
from src.target_list import TargetList


class App:
    window: CTk
    frames = {}
    controller: Controller

    def __init__(self, title, data_dir: str, config_file_path: str, config_file_name: str, log_file_path: str, icon='icon.png', width = 800, height = 600):
        self.window = CTk()
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")

        # config_path = 'data/config.json'
        self.controller = Controller(data_dir, config_file_path, config_file_name, log_file_path)

        set_default_color_theme('green')
        self.window.resizable(False, False)

        img = PhotoImage(file=icon)
        self.window.wm_iconbitmap()
        self.window.wm_iconphoto(False, img)


    def build_ui(self):
        main = TargetList(master = self.window, controller = self.controller)
        self.frames[main.id] = main
        main.grid(row=0, column=0, sticky="nsew")

        config = ConfigFrame(master = self.window, controller = self.controller)
        self.frames[config.id] = config
        config.grid(row=0, column=1, sticky="nsew")

        main.build_ui()
        config.build_ui(5, 5)

        #execute frame
        e_frame = CTkFrame(master=self.window, corner_radius=0)
        e_frame.grid(row=2, column=0, columnspan = 2, padx=5, pady=10, sticky="nsew")
        #execute button
        execute = CTkButton(master=e_frame, text='Execute', command=self.execute)
        execute.pack()
        main.update()
        config.update()

    def execute(self):
        self.controller.execute_file_movements()

    def toggle_frame(self, id):
        self.frames[id].tkraise()

    def run(self):
        self.window.mainloop()