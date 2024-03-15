if __name__ == "__main__":
    import subprocess
    subprocess.Popen(['powershell', f'python3 __main_.py'])
    
try:

    import customtkinter
    from PIL import Image, ImageTk
    import yaml
    import os
    import webbrowser
    
    from .PlotTracker import *
    from .tabs.login import login_window
    from .tabs.save import save_window
    from .tabs.home import home_window
    
    from tkinter import filedialog

    customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

except Exception as e:
    print(f'[GraphicalUI.py] [Error]: {e}')
    print(f'[GraphicalUI.py] [Error]: Maybe your PYTHONPATH is not set correctly?')
    input("Press any key to exit...")


class AppUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("TimeTracker")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        #yaml file
        
        with open("src/GraphicalUI/config_en.yaml", "r") as FILE:
            self.config = yaml.safe_load(FILE)

        
        self.LANGUAGE = self.config['language']
        #======================================================================================
        # Left Sidebar
        #======================================================================================
        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="AHB Finance", font=customtkinter.CTkFont(size=20, weight="bold"),
                                                 text_color=("gray", "white"), fg_color=("transparent"), bg_color=("transparent"), corner_radius=0, width=140, height=100            
                                                 
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.create_left_sidebar_buttons(os.path.join(os.path.dirname(os.path.realpath(__file__)), "images"))
        self.create_logo()
       
    def create_logo(self):
        self.logo = Image.open(self.config['logo_path'])
        
        ctk_image = customtkinter.CTkImage(self.logo, size=(400, 300))
        self.logo_label = customtkinter.CTkLabel(self, image=ctk_image, text='')
        self.logo_label.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))
        
    def create_left_sidebar_buttons(self, image_path):
        
        self.home_button = self.create_button(os.path.join(image_path, "home_light.png"), "Home", self.home, 1, 0, 0, 0)
        self.analisys_button = self.create_button(os.path.join(image_path, "analytics_light.png"), "Analytics", self.analytics, 2, 0, 0, 0)
        self.save_button = self.create_button(os.path.join(image_path, "save_light.png"), "Save you Activity", self.save, 3, 0, 0, 0)
        self.admin_buton = self.create_button(os.path.join(image_path, "login_light.png"), "Admin", self.login, 4, 0, 0, 0)
        
    def create_button(self, image_path, text, command, row, column, padx, pady):
        self.image = customtkinter.CTkImage(light_image=Image.open(image_path),
                                            dark_image=Image.open(image_path), size=(20, 20))
        
        self.button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=10, height=80, border_spacing=10, text=text,
                                              fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                              image=self.image, anchor="w", command=command, font=customtkinter.CTkFont(size=16))
        
        self.button.grid(row=row, column=column, padx=padx, pady=pady, sticky="w")
        
        return self.button
    
    
    #======================================================================================
    # Home Page and functions
    #======================================================================================
    
    def create_frame(self) -> customtkinter.CTkFrame:
        frame = customtkinter.CTkFrame(self, corner_radius=10, height=1920, width=1080)
        frame.grid(row=0, column=1, padx=(40, 40), pady=(40, 40), sticky="nsew")
        
        return frame 
        
    
    def destroy_previous_page(self):
        # Destroy the widgets of the previous page
        for widget in self.winfo_children():
            if isinstance(widget, customtkinter.CTkFrame) and widget != self.sidebar_frame:
                widget.destroy()
        if hasattr(self, 'entry_task'):
            self.entry_task.destroy()
        if hasattr(self, 'add_button_'):
            self.add_button_.destroy()
        if hasattr(self, 'logo_label'):
            self.logo_label.destroy()

    def save(self):
        self.destroy_previous_page()
        frame = self.create_frame()
        
        save_window(frame)
    
    def login(self):
        self.destroy_previous_page()
        frame = self.create_frame()
        
        login_window(frame)
        
    def home(self):
        self.destroy_previous_page()
        frame = self.create_frame()
        
        home_window(frame)
        
    
        
    def analytics(self):
        # Clear the existing content
        self.destroy_logo()
        self.destroy_home()
        
        # Open the file explorer to search for the data file
        data_path = filedialog.askopenfilename(title="Select the data file", filetypes=[("JSON files", "*.json")])
        
        frame = customtkinter.CTkFrame(self, corner_radius=0)
        frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        
        # Create the pie chart in the specified frame
        create_pie_chart(data_path, frame)
                 
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def sidebar_button_event(self):
        print("sidebar_button click")

