from customtkinter import *
from CTkTable import CTkTable
from PIL import Image

from .user import User
from .main_views.dashboard import home
from .main_views.create_task import create_task_window
from .main_views.tasks_running import tasks_running_window

import os

class TimeTrackingGUI():
    
    def __init__(self, images_relative_path: str, email: str) -> None:
        
        
        self.logged_user = User("", email)
        
        self.images_relative_path = images_relative_path
        app = CTk()
        
        app.geometry("1200x645")
        app.resizable(0,0)

        set_appearance_mode("light")

        sidebar_frame = CTkFrame(master=app, fg_color="#0d132d",  width=180, height=700, corner_radius=0)
        sidebar_frame.pack_propagate(0)
        sidebar_frame.pack(fill="y", anchor="w", side="left")

        # Set background image
        background_img_data = Image.open(images_relative_path + "wallpaper.png")
        background_img = CTkImage(dark_image=background_img_data, light_image=background_img_data, size=(180, 700))
        CTkLabel(master=sidebar_frame, image=background_img, text='').place(x=0, y=0, relwidth=1, relheight=1)

        logo_img_data = Image.open(images_relative_path + "logo2.png")
        logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(75.00, 80.00))
        CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(30, 100), anchor="center")


        self.create_button(sidebar_frame, "analytics_icon.png", "Dashboard", self.dashboard_event)
        self.create_button(sidebar_frame, "package_icon.png", "Create Task", self.create_task_event)
        self.create_button(sidebar_frame, "list_icon.png", "Tasks Running", self.tasks_running_event)
        
        if self.logged_user.admin:
            self.create_button(sidebar_frame, "returns_icon.png", "Admin Center", self.returns_event)
        
        self.create_button(sidebar_frame, "settings_icon.png", "Settings", self.settings_event)
        self.create_button(sidebar_frame, "person_icon.png", "Account", self.account_event)
        
        self.main_view = self.create_main_view(app)

        self.app = app
        app.mainloop()


    def create_main_view(self, master):
        if hasattr(self, 'main_view'):
            self.main_view.destroy()
            
        main_view = CTkFrame(master=master, fg_color="#fff",  width=1300, height=650, corner_radius=0)
        main_view.pack_propagate(0)
        main_view.pack(side="left")
        
        return main_view

    def create_button(self, master, image_path, text, command):
        button_img_data = Image.open(self.images_relative_path + image_path)
        button_img = CTkImage(dark_image=button_img_data, light_image=button_img_data)
        CTkButton(master=master, image=button_img, text=text, fg_color="transparent", font=("Arial Bold", 14), hover_color="#8321b4", anchor="w", command=command).pack(anchor="w", ipady=5, pady=(15, 0))

    def dashboard_event(self):
        self.main_view = self.create_main_view(self.app)
        home(self.main_view)
        
        pass
    
    def create_task_event(self):
        self.main_view = self.create_main_view(self.app)
        create_task_window(self.main_view, self.logged_user.get_email())
        pass
    
    def tasks_running_event(self):
        self.main_view = self.create_main_view(self.app)
        tasks_running_window(self.main_view)

    def returns_event(self):
        pass
    
    def settings_event(self):
        pass
    
    def account_event(self):
        pass

if __name__ == "__main__":
    os.system("python __main_.py")