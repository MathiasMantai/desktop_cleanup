from tkinter import IntVar
from customtkinter import (
    CTkFrame,
    CTkLabel,
    CTkCheckBox
)
from src.controller import Controller


class ConfigFrame(CTkFrame):
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
        super(ConfigFrame, self).__init__(master=master)
        self.controller = controller


    def show_frame(self):
        self.tkraise()

    def build_ui(self, padx = 0, pady = 0):
        row = 0

        options = self.controller.get_config("type_config")
        for option in options:
            col = 0
            label = CTkLabel(master=self, text=option.capitalize(), padx=padx, pady=pady)
            label.grid(row=row, column=col, padx=padx, pady=pady)
            row += 1
            for item in options[option]["file_extensions"]:
                if col >= 6:
                    row += 1
                    col = 0
                id = "type_config." + option + ".file_extensions." + item
                self.vars[id] = IntVar(value=options[option]["file_extensions"][item], name=id)
                self.chks[id] = CTkCheckBox(self, text = item, variable=self.vars[id], width=80, checkbox_width=20, checkbox_height=20, command=lambda id=id: self.controller.update_config(id, self.vars[id].get()))
                self.chks[id].grid(row=row, column=col, padx=10, pady=10)
                col += 1
            row += 1