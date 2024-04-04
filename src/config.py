from tkinter import IntVar, LEFT, RIGHT
from customtkinter import (
    CTkFrame,
    CTkLabel,
    CTkCheckBox,
    CTkEntry
)
from src.controller import Controller


class ConfigFrame(CTkFrame):
    """
    config frame for application
    show options:
    - which file types to organize 
        - images: jpg, png, gif, bitmap, svg, webp
        - documents: txt, docx, xlsx
        - music: mp3, mp4 
    """

    # vars: list = []
    controller: Controller
    id: str = 'config'
    vars: dict = {}
    chks: dict = {}

    def __init__(self, master=None, controller=None):
        super(ConfigFrame, self).__init__(master=master, corner_radius=0)
        self.controller = controller

    def show_frame(self):
        self.tkraise()

    def build_ui(self, padx = 0, pady = 0):
        row = 0
        options = self.controller.get_config("type_config")
        for option in options:
            col = 0
            header_frame = CTkFrame(master=self, bg_color="transparent")
            header_frame.grid(row=row, columnspan=6, sticky='we')
            label = CTkLabel(master=header_frame, text=option.capitalize(), padx=padx, pady=pady, corner_radius=0, anchor="n", font=('Helvetica', 18, 'bold'))
            # label.grid(row=row, column=col, padx=padx, pady=pady)
            label.pack(side=LEFT, padx=10)
            new_dir_label = CTkLabel(master=header_frame, text="New Directory:")
            # new_dir_label.grid(row=row, column=1, padx=0, pady=5)
            new_dir_input = options[option]["new_dir"]
            new_dir_entry = CTkEntry(master=header_frame, corner_radius=5, width=200)
            new_dir_entry.insert(0, string=new_dir_input)
            # new_dir_entry.grid(row=row, column=2, sticky="e", padx=0, pady=5)
            new_dir_entry.pack(side=RIGHT, padx=5, pady=5)
            new_dir_label.pack(side=RIGHT)

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