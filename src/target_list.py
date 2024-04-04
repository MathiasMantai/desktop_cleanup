from customtkinter import (
    CTkFrame,
    CTkTextbox,
    CTkLabel
)
from src.controller import Controller
from tkinter import TOP, BOTTOM


class TargetList(CTkFrame):
    """
    main frame for application
    shows a textarea for paths that should be organized
    and a button to start organizing
    """
    id: str = 'main'
    target_list: CTkTextbox = None
    controller: Controller
    def __init__(self, master=None, controller=None):
        self._bg_color = "#333333"
        super(TargetList, self).__init__(master=master, corner_radius=0, bg_color="#333333")
        self.controller = controller

    def on_text_changed(self, event):
        target_list_string = self.target_list.get("1.0",'end-1c')
        self.controller.update_target_list(target_list_string)

    def build_ui(self):
        header = CTkLabel(master=self, text='Target Directories', font=('Helvetica', 18, 'bold'), bg_color="#333333", width=300, corner_radius=0, padx=5, pady=10)
        header.pack(side=TOP)

        self.target_list = CTkTextbox(master=self, width=300, height= 400, border_spacing = 0, corner_radius = 0)
        self.target_list.pack(side=BOTTOM)
        self.target_list.insert('1.0', text=self.controller.target_list_to_string(self.controller.get_config('target_list')))
        self.target_list.bind("<KeyRelease>", self.on_text_changed)

        # print(self.target_list.get("1.0",'end-1c'))

    def show_frame(self):
        self.tkraise()