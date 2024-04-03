from customtkinter import (
    CTkFrame,
    CTkTextbox,
    CTkLabel
)
from src.controller import Controller


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
        super(TargetList, self).__init__(master=master)
        self.controller = controller

    def on_text_changed(self, event):
        target_list_string = self.target_list.get("1.0",'end-1c')
        self.controller.update_target_list(target_list_string)

    def build_ui(self):
        l = CTkLabel(master=self, text='t')
        l.grid(row=0, column=0)

        self.target_list = CTkTextbox(master=self, width=300, height= 400, border_spacing = 0)
        self.target_list.grid(row=0, column=0)
        self.target_list.insert('1.0', text=self.controller.target_list_to_string(self.controller.get_config('target_list')))
        self.target_list.bind("<KeyRelease>", self.on_text_changed)
        print(self.target_list.get("1.0",'end-1c'))

    def show_frame(self):
        self.tkraise()