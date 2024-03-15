from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import os

class TimeTrackingGUI():
    
    def __init__(self, images_relative_path: str) -> None:
        
        self.images_relative_path = images_relative_path
        app = CTk()
        app.geometry("856x645")
        app.resizable(0,0)

        set_appearance_mode("light")

        sidebar_frame = CTkFrame(master=app, fg_color="#131b2c",  width=180, height=700, corner_radius=0)
        sidebar_frame.pack_propagate(0)
        sidebar_frame.pack(fill="y", anchor="w", side="left")

        logo_img_data = Image.open(images_relative_path + "microsoft-icon.png")
        logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(75.00, 80.00))
        CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(30, 100), anchor="center")


        self.create_button(sidebar_frame, "analytics_icon.png", "Dashboard", self.dashboard_event)
        self.create_button(sidebar_frame, "package_icon.png", "Orders", self.orders_event)
        self.create_button(sidebar_frame, "list_icon.png", "Orders", self.returns_event)
        self.create_button(sidebar_frame, "returns_icon.png", "Returns", self.returns_event)
        self.create_button(sidebar_frame, "settings_icon.png", "Settings", self.settings_event)
        self.create_button(sidebar_frame, "person_icon.png", "Account", self.account_event)
        
        main_view = CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
        main_view.pack_propagate(0)
        main_view.pack(side="left")

        app.mainloop()


    def create_button(self, master, image_path, text, command):
        button_img_data = Image.open(self.images_relative_path + image_path)
        button_img = CTkImage(dark_image=button_img_data, light_image=button_img_data)
        CTkButton(master=master, image=button_img, text=text, fg_color="transparent", font=("Arial Bold", 14), hover_color="#8321b4", anchor="w", command=command).pack(anchor="w", ipady=5, pady=(15, 0))

    
    def dashboard_event(self, frame):
        print("Dashboard")
        pass
    
    def orders_event(self):
        pass

    def returns_event(self):
        pass
    
    def settings_event(self):
        pass
    
    def account_event(self):
        pass

if __name__ == "__main__":
    os.system("python __main_.py")