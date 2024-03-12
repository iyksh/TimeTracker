
import customtkinter
from PIL import Image, ImageTk
import yaml
import os
import webbrowser

from PlotTracker import *
from tkinter import filedialog

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
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
        
        with open("./config.yaml", "r") as FILE:
            self.config = yaml.safe_load(FILE)

        
        self.LANGUAGE = self.config['language']
        #======================================================================================
        # Left Sidebar
        #======================================================================================
        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="AHB Finance \nManagement Gmbh", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.create_left_sidebar_buttons(os.path.join(os.path.dirname(os.path.realpath(__file__)), "images"))

        #======================================================================================
        # Starts with organization logo
        #======================================================================================

        self.logo = Image.open(self.config['logo_path'])
        
        ctk_image = customtkinter.CTkImage(self.logo, size=(400, 300))
        self.logo_label = customtkinter.CTkLabel(self, image=ctk_image, text='')
        self.logo_label.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))
       


    def destroy_logo(self):
        if self.logo_label:
            self.logo_label.destroy()
            
    def create_left_sidebar_buttons(self, image_path):
        
        self.home_button = self.create_button(os.path.join(image_path, "home_light.png"), "Home", self.home, 1, 0, 0, 0)
        self.analisys_button = self.create_button(os.path.join(image_path, "analytics_light.png"), "Analytics", self.analytics, 2, 0, 0, 0)
        self.save_button = self.create_button(os.path.join(image_path, "save_light.png"), "Save", self.save, 3, 0, 0, 0)
        self.settings_button = self.create_button(os.path.join(image_path, "settings_light.png"), "Settings", self.settings, 5, 0, 0, 0)
        
        
    
    def create_button(self, image_ppath, text, command, row, column, padx, pady):
        self.image = customtkinter.CTkImage(light_image=Image.open(image_ppath),
                                            dark_image=Image.open(image_ppath), size=(20, 20))
        
        
        self.button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40, border_spacing=10, text=text,
                                              fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                              image=self.image, anchor="w", command=command, font=customtkinter.CTkFont(size=16))
        
        self.button.grid(row=row, column=column, padx=padx, pady=pady, sticky="ew")
        
        return self.button
    
    #======================================================================================
    # Home Page and functions
    #======================================================================================

        
    def home(self):
        self.destroy_logo()
        self.destroy_home()
        
        self.entry_task = customtkinter.CTkEntry(self, placeholder_text="Add Task")
        self.entry_task.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.add_button_ = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Add")
        self.add_button_.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        pass
    
    def destroy_home(self):
        # Destroy the entry widget
        if hasattr(self, 'entry_task'):  # Check if the attribute exists
            self.entry_task.destroy()

        # Destroy the button widget
        if hasattr(self, 'add_button_'):  # Check if the attribute exists
            self.add_button_.destroy()

        
        
    def save(self):
        webbrowser.open("http://localhost:5600/api/0/export")
        
        
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

        
    #======================================================================================
    # Settings Page and functions
    #======================================================================================
        
    def settings(self):
        self.destroy_logo()
        self.destroy_home()

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=2500, height=100)
        self.tabview.grid(row=0, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.tabview.add("Configurations")
        self.tabview.tab("Configurations").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        # Language Option Menu
        self.text_language = customtkinter.CTkLabel(self.tabview.tab("Configurations"), text="Language:", anchor="w")
        self.text_language.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        self.language_optionmenu = customtkinter.CTkOptionMenu(self.tabview.tab("Configurations"), dynamic_resizing=False,
                                                               values=["English", "Polish", "German"])
        self.language_optionmenu.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="w")

        # Appearance Mode Option Menu
        self.text_appearance_mode = customtkinter.CTkLabel(self.tabview.tab("Configurations"), text="Appearance Mode:", anchor="w")
        self.text_appearance_mode.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")

        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.tabview.tab("Configurations"), dynamic_resizing=False,
                                                                     values=["System", "Dark", "Light"],
                                                                     command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=1, column=1, padx=20, pady=(20, 10), sticky="w")

        # Scaling Option Menu
        self.text_scaling = customtkinter.CTkLabel(self.tabview.tab("Configurations"), text="UI Scaling:", anchor="w")
        self.text_scaling.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")

        self.scaling_optionmenu = customtkinter.CTkOptionMenu(self.tabview.tab("Configurations"), dynamic_resizing=False,
                                      values=["100%", "80%", "90%", "110%", "120%"],
                                      command=self.change_scaling_event)
        self.scaling_optionmenu.grid(row=2, column=1, padx=20, pady=(20, 10), sticky="w")

        # Font Option Menu
        self.text_font = customtkinter.CTkLabel(self.tabview.tab("Configurations"), text="Font:", anchor="w")
        self.text_font.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")

        self.font_optionmenu = customtkinter.CTkOptionMenu(self.tabview.tab("Configurations"), dynamic_resizing=False,
                                   values=["Arial", "Times New Roman", "Courier New"])
        self.font_optionmenu.grid(row=3, column=1, padx=20, pady=(20, 10), sticky="w")

        # Theme Option Menu
        self.text_theme = customtkinter.CTkLabel(self.tabview.tab("Configurations"), text="-", anchor="w")
        self.text_theme.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="w")

        self.theme_optionmenu = customtkinter.CTkOptionMenu(self.tabview.tab("Configurations"), dynamic_resizing=False,
                                    values=["-", ""])
        self.theme_optionmenu.grid(row=4, column=1, padx=20, pady=(20, 10), sticky="w")
        
        self.text_theme = customtkinter.CTkLabel(self.tabview.tab("Configurations"), text="-", anchor="w")
        self.text_theme.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="w")

        self.theme_optionmenu = customtkinter.CTkOptionMenu(self.tabview.tab("Configurations"), dynamic_resizing=False,
                                    values=["-", ""])
        self.theme_optionmenu.grid(row=5, column=1, padx=20, pady=(20, 10), sticky="w")
        
        self.text_theme = customtkinter.CTkLabel(self.tabview.tab("Configurations"), text="-", anchor="w")
        self.text_theme.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")

        self.theme_optionmenu = customtkinter.CTkOptionMenu(self.tabview.tab("Configurations"), dynamic_resizing=False,
                                    values=["-", ""])
        self.theme_optionmenu.grid(row=6, column=1, padx=20, pady=(20, 10), sticky="w")

        # Save Settings Button
        self.save_settings_button = customtkinter.CTkButton(self.tabview.tab("Configurations"), text="Save Settings",
                                                            command=self.save_settings)
        self.save_settings_button.grid(row=20, column=0, columnspan=2, padx=20, pady=(20, 10))

        # center the tabview
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def save_settings(self):
        language = self.language_optionmenu.get()
        self.config['language'] = language
        
        with open("./config.yaml", "w") as FILE:
            yaml.dump(self.config, FILE)
            
        
        


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()