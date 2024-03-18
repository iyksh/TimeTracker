from customtkinter import *

def configurations_window(frame:CTkFrame, user_email:str):
    
    languages = ["English", "Polish", "German"]
    appearance_modes = ["System", "Dark", "Light"]
    scalings = ["100%", "80%", "90%", "110%", "120%", "130%", "140%", "150%"]
    fonts = ["Arial", "Arial Bold", "Arial Black", "Arial Italic", "Arial Bold Italic", "Arial Narrow", "Arial Narrow Bold", "Arial Narrow Italic", "Arial Narrow Bold Italic", "Arial Rounded MT Bold", "Arial Unicode MS", "Arial Unicode MS Bold", "Arial Unicode MS"]

    set_appearance_mode("light")

    main_view = frame

    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))
    
    CTkButton(master=title_frame, text="+ Save Configurations",  font=("Arial Black", 15), text_color="#fff", fg_color="#601E88", hover_color="#E44982", command=lambda: apply_settings(language_combobox.get(), appearance_mode_combobox.get(), scaling_combobox.get(), font_combobox.get())).pack(anchor="ne", side="right")
    CTkLabel(master=main_view, text=f"Logged User: {user_email}", font=("Arial Bold", 17), text_color="#601E88").pack(anchor="nw", pady=(25,0), padx=27)

    CTkLabel(master=main_view, text="Appearance Mode", font=("Arial Bold", 17), text_color="#601E88").pack(anchor="nw", pady=(25,0), padx=27)

    appearance_mode_combobox = CTkComboBox(master=main_view, width=1000, height=40,values=appearance_modes, button_color="#601E88", border_color="#601E88", border_width=2, button_hover_color="#E44982",dropdown_hover_color="#E44982" , dropdown_fg_color="#601E88", dropdown_text_color="#fff")
    appearance_mode_combobox.pack(pady=(10,0), padx=27)

    CTkLabel(master=main_view, text="UI Scaling", font=("Arial Bold", 17), text_color="#601E88").pack(anchor="nw", pady=(25,0), padx=27)

    scaling_combobox = CTkComboBox(master=main_view, width=1000, height=40,values=scalings, button_color="#601E88", border_color="#601E88", border_width=2, button_hover_color="#E44982",dropdown_hover_color="#E44982" , dropdown_fg_color="#601E88", dropdown_text_color="#fff")
    scaling_combobox.pack(pady=(10,0), padx=27)

    CTkLabel(master=main_view, text="Font", font=("Arial Bold", 17), text_color="#601E88").pack(anchor="nw", pady=(25,0), padx=27)

    font_combobox = CTkComboBox(master=main_view, width=1000, height=40,values=fonts, button_color="#601E88", border_color="#601E88", border_width=2, button_hover_color="#E44982",dropdown_hover_color="#E44982" , dropdown_fg_color="#601E88", dropdown_text_color="#fff")
    font_combobox.pack(pady=(10,0), padx=27)
    
    CTkLabel(master=main_view, text="Language", font=("Arial Bold", 17), text_color="#601E88").pack(anchor="nw", pady=(25,0), padx=27)
    language_combobox = CTkComboBox(master=main_view, width=1000, height=40,values=languages, button_color="#601E88", border_color="#601E88", border_width=2, button_hover_color="#E44982",dropdown_hover_color="#E44982" , dropdown_fg_color="#601E88", dropdown_text_color="#fff")
    language_combobox.pack(pady=(10,0), padx=27)
    

    
    
    actions= CTkFrame(master=main_view, fg_color="transparent")
    actions.pack(fill="both")


    # Function to apply settings
def apply_settings(language: str, appearance_mode: str, scaling: str, font: str):

        print(f"Language: {language}")
        print(f"Appearance Mode: {appearance_mode}")
        print(f"Scaling: {scaling}")
        print(f"Font: {font}")
        
        
