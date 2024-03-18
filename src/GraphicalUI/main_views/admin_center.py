import tkinter
from customtkinter import *
import webview

from src.AWManager.AWsettings import is_aw_processes_alive

def open_webrowser():
    try:
        open_browser()

    except Exception as e:
        print(f'[login.py] [Error]: {e}')
        return False


def open_browser():
    webview.create_window("Admin Center", "http://localhost:5600/#/buckets")
    webview.start()

"""
def admin_center_window(frame):
    def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


    is_alive = is_aw_processes_alive()
    for i in range(len(is_alive)):
        is_alive[i] = "true" if is_alive[i] else "false"

    # create tabview
    tabview = customtkinter.CTkTabview(frame, width=2500, height=100)
    tabview.grid(row=0, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
    tabview.add("Admin-Configs")
    tabview.tab("Admin-Configs").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

    # aw-server Option Menu
    text_aw_server = customtkinter.CTkLabel(tabview.tab("Admin-Configs"), text="aw-server:", anchor="w")
    text_aw_server.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

    aw_server_optionmenu = customtkinter.CTkOptionMenu(tabview.tab("Admin-Configs"), dynamic_resizing=False,
                                                      values=[is_alive[0]])
    aw_server_optionmenu.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="w")

    # aw-server-rust Option Menu
    text_aw_server_rust = customtkinter.CTkLabel(tabview.tab("Admin-Configs"), text="aw-qt:", anchor="w")
    text_aw_server_rust.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")

    aw_server_rust_optionmenu = customtkinter.CTkOptionMenu(tabview.tab("Admin-Configs"), dynamic_resizing=False,
                                                            values=[is_alive[3]])
    aw_server_rust_optionmenu.grid(row=1, column=1, padx=20, pady=(20, 10), sticky="w")

    # aw-watcher-afk Option Menu
    text_aw_watcher_afk = customtkinter.CTkLabel(tabview.tab("Admin-Configs"), text="aw-watcher-afk:", anchor="w")
    text_aw_watcher_afk.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")

    aw_watcher_afk_optionmenu = customtkinter.CTkOptionMenu(tabview.tab("Admin-Configs"), dynamic_resizing=False,
                                                           values=[is_alive[1]])
    aw_watcher_afk_optionmenu.grid(row=2, column=1, padx=20, pady=(20, 10), sticky="w")

    # aw-watcher-window Option Menu
    text_aw_watcher_window = customtkinter.CTkLabel(tabview.tab("Admin-Configs"), text="aw-watcher-window:", anchor="w")
    text_aw_watcher_window.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")

    aw_watcher_window_optionmenu = customtkinter.CTkOptionMenu(tabview.tab("Admin-Configs"), dynamic_resizing=False,
                                                               values=[is_alive[2]])
    aw_watcher_window_optionmenu.grid(row=3, column=1, padx=20, pady=(20, 10), sticky="w")
    
    y_space_label = customtkinter.CTkLabel(tabview.tab("Admin-Configs"), text="", anchor="w")
    y_space_label.grid(row=26, column=4, padx=20, pady=(100, 100), sticky="w")

    open_admin_center_button = customtkinter.CTkButton(tabview.tab("Admin-Configs"), text="Admin Center", command=lambda: open_webrowser(frame))
    open_admin_center_button.grid(row=25, column=0, columnspan=2, padx=20, pady=(20, 10))

    # center the tabview
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    tabview.add("Configurations")
    tabview.tab("Configurations").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
    
    selected_language = customtkinter.StringVar().get
    selected_appearance_mode = customtkinter.StringVar().get
    selected_scaling = customtkinter.StringVar().get
    selected_font = customtkinter.StringVar().get
    
    apply_settings_button = customtkinter.CTkButton(tabview.tab("Configurations"), text="Apply Settings", 
    command=lambda: apply_settings(selected_language, selected_appearance_mode, selected_scaling, selected_font))
    apply_settings_button.grid(row=7, columnspan=2, pady=(20, 10))
    """

def admin_center_window(frame:CTkFrame):
    
    is_alive = is_aw_processes_alive()
    for i in range(len(is_alive)):
        is_alive[i] = ["Enabled"] if is_alive[i] else ["Disabled"]
    
    set_appearance_mode("light")

    aw_server = is_alive[0]
    aw_watcher_afk = is_alive[1]
    aw_watcher_window = is_alive[2]
    aw_qt = is_alive[3]
    
    main_view = frame

    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))
    
    CTkButton(master=title_frame, text="+ Admin Center TimeTracking",  font=("Arial Black", 15), text_color="#fff", fg_color="#601E88", hover_color="#E44982", command=open_webrowser).pack(anchor="ne", side="right")
    
    CTkLabel(master=main_view, text="ActivityWatch-server | Default: True", font=("Arial Bold", 17), text_color="#601E88").pack(anchor="nw", pady=(25,0), padx=27)
    aw_server_combobox = CTkComboBox(master=main_view, width=1000, height=40, values=aw_server, button_color="#601E88", border_color="#601E88", border_width=2, button_hover_color="#E44982", dropdown_hover_color="#E44982", dropdown_fg_color="#601E88", dropdown_text_color="#fff")
    aw_server_combobox.pack(pady=(10,0), padx=27)

    CTkLabel(master=main_view, text="ActivityWatch-watcher-afk | Default: True", font=("Arial Bold", 17), text_color="#601E88").pack(anchor="nw", pady=(25,0), padx=27)
    aw_watcher_afk_combobox = CTkComboBox(master=main_view, width=1000, height=40, values=aw_watcher_afk, button_color="#601E88", border_color="#601E88", border_width=2, button_hover_color="#E44982", dropdown_hover_color="#E44982", dropdown_fg_color="#601E88", dropdown_text_color="#fff")
    aw_watcher_afk_combobox.pack(pady=(10,0), padx=27)

    CTkLabel(master=main_view, text="ActivityWatch-watcher-window | Default: True", font=("Arial Bold", 17), text_color="#601E88").pack(anchor="nw", pady=(25,0), padx=27)
    aw_watcher_window_combobox = CTkComboBox(master=main_view, width=1000, height=40, values=aw_watcher_window, button_color="#601E88", border_color="#601E88", border_width=2, button_hover_color="#E44982", dropdown_hover_color="#E44982", dropdown_fg_color="#601E88", dropdown_text_color="#fff")
    aw_watcher_window_combobox.pack(pady=(10,0), padx=27)

    CTkLabel(master=main_view, text="ActivityWatch-qt | Default: False", font=("Arial Bold", 17), text_color="#601E88").pack(anchor="nw", pady=(25,0), padx=27)
    aw_qt_combobox = CTkComboBox(master=main_view, width=1000, height=40, values=aw_qt, button_color="#601E88", border_color="#601E88", border_width=2, button_hover_color="#E44982", dropdown_hover_color="#E44982", dropdown_fg_color="#601E88", dropdown_text_color="#fff")
    aw_qt_combobox.pack(pady=(10,0), padx=27)

   
    actions= CTkFrame(master=main_view, fg_color="transparent")
    actions.pack(fill="both")

        

    # Function to apply settings
def apply_settings(language: str, appearance_mode: str, scaling: str, font: str):

        print(f"Language: {language}")
        print(f"Appearance Mode: {appearance_mode}")
        print(f"Scaling: {scaling}")
        print(f"Font: {font}")
        
        
