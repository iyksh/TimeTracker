
from src.GraphicalUI.main import TimeTrackingGUI
from src.AWManager.AWsettings import check_aw_processes

from customtkinter import *
from PIL import Image

class Login_Page():
    
    def __init__(self):
        relative_path = 'images/'
        
        self.images_relative_path = relative_path
        
        self.app = CTk()
        self.app.geometry("600x480")
        self.app.resizable(0,0)
        self.app.title("Login - TimeTracker")
        self.app.iconbitmap(relative_path + "application_icon.ico")
        
        
        side_img_data = Image.open(relative_path+"side-img-logo.png")
        email_icon_data = Image.open(relative_path+"email-icon.png")
        password_icon_data = Image.open(relative_path+"password-icon.png")
        microsoft_icon_data = Image.open(relative_path+"microsoft-icon.png")

        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
        email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
        password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))
        microsoft_icon = CTkImage(dark_image=microsoft_icon_data, light_image=microsoft_icon_data, size=(17,17))

        CTkLabel(master=self.app, text="", image=side_img).pack(expand=True, side="left")

        frame = CTkFrame(master=self.app, width=300, height=480, fg_color="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        self.email = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        self.email.pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
        self.password = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
        self.password.pack(anchor="w", padx=(25, 0))

        self.error_label = CTkLabel(master=frame, text="", text_color="#DC143C", anchor="w", justify="left", font=("Arial Bold", 12))
        self.error_label.pack(anchor="w", pady=(10, 0), padx=(25, 0))

        
        CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=self.manual_login).pack(anchor="w", pady=(40, 0), padx=(25, 0))
        CTkButton(master=frame, text="Continue With Microsoft", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Arial Bold", 9), text_color="#601E88", width=225, image=microsoft_icon).pack(anchor="w", pady=(20, 0), padx=(25, 0))


        
        self.app.mainloop()

    def manual_login(self):
        
        credentials_valid = self.check_login_credentials()
        if not credentials_valid[0]:
            self.error_label.configure(text="Invalid email or password!")
            self.error_label.pack(anchor="w", pady=(10, 0), padx=(25, 0))

            return
        
        self.error_label.configure(text="Login successful!", text_color="#32CD32")
        print("Logged user: ", credentials_valid[1])
        
        check_aw_processes()
        self.app.destroy()
        
        app = TimeTrackingGUI(self.images_relative_path, credentials_valid[1])
        
    def check_login_credentials(self):
        valid_credentials = {"user": "user", "root": "root", "ahbfinance": "admin"}
        
        email = self.email.get()
        password = self.password.get()

        if email in valid_credentials and password == valid_credentials[email] or email == "" and password == "":
            return True, email

        return False, None

if __name__ == "__main__":
    Login_Page()
    #app = TimeTrackingGUI('images/', "root")


