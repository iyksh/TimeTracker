import tkinter
import customtkinter
import webview
import multiprocessing


valid_logins = { "root": "root", "ahbfinance": "admin"}



def login_window(frame: tkinter.Frame):
    
    def login_event():
        if entry_1.get() in valid_logins and entry_2.get() == valid_logins[entry_1.get()]:
            entry_1.configure(text_color="white")
            entry_2.configure(text_color="white")
            
            admin_settings(frame)
        
        else:            
            label_3 = customtkinter.CTkLabel(master=frame, width=400, height=60, corner_radius=10,
            fg_color=("transparent"), text="Wrong Password/Username!", bg_color="transparent", font=("Arial bold", 15),
            text_color="red"
            
            )
            label_3.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    # Add some widgets for login page
    label_1 = customtkinter.CTkLabel(master=frame, width=400, height=60, corner_radius=10,
                                     fg_color=("transparent"), text="Welcome!", bg_color="transparent", font=("Arial bold", 30))
    label_1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    
    label_2 = customtkinter.CTkLabel(master=frame, width=400, height=60, corner_radius=10,
                                        fg_color=("transparent"), text="Please Login to Continue to the Admin Center", bg_color="transparent", font=("Arial bold", 15))
    label_2.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    entry_1 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Username")
    entry_1.place(relx=0.5, rely=0.52, anchor=tkinter.CENTER)

    entry_2 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, show="*", placeholder_text="Password")
    entry_2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    button_login = customtkinter.CTkButton(master=frame, text="LOGIN", corner_radius=6, command=login_event, width=400)
    button_login.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


def open_webrowser(tkinter_frame: tkinter.Frame):
    try:

        # Create a new process to open the web browser
        p = multiprocessing.Process(target=open_browser)
        p.start()

        return True

    except Exception as e:
        print(f'[login.py] [Error]: {e}')
        return False


def open_browser():
    webview.create_window('Admin Center', 'http://localhost:5600/#/buckets')
    webview.start()


def admin_settings(frame):
    def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    # create tabview
    tabview = customtkinter.CTkTabview(frame, width=2500, height=100)
    tabview.grid(row=0, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
    tabview.add("Admin-Configs")
    tabview.tab("Admin-Configs").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

    # aw-server Option Menu
    text_aw_server = customtkinter.CTkLabel(tabview.tab("Admin-Configs"), text="aw-server:", anchor="w")
    text_aw_server.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

    aw_server_optionmenu = customtkinter.CTkOptionMenu(tabview.tab("Admin-Configs"), dynamic_resizing=False,
                                                      values=["true", "false"])
    aw_server_optionmenu.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="w")

    # aw-server-rust Option Menu
    text_aw_server_rust = customtkinter.CTkLabel(tabview.tab("Admin-Configs"), text="aw-server-rust:", anchor="w")
    text_aw_server_rust.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")

    aw_server_rust_optionmenu = customtkinter.CTkOptionMenu(tabview.tab("Admin-Configs"), dynamic_resizing=False,
                                                            values=["true", "false"])
    aw_server_rust_optionmenu.grid(row=1, column=1, padx=20, pady=(20, 10), sticky="w")

    # aw-watcher-afk Option Menu
    text_aw_watcher_afk = customtkinter.CTkLabel(tabview.tab("Admin-Configs"), text="aw-watcher-afk:", anchor="w")
    text_aw_watcher_afk.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")

    aw_watcher_afk_optionmenu = customtkinter.CTkOptionMenu(tabview.tab("Admin-Configs"), dynamic_resizing=False,
                                                           values=["true", "false"])
    aw_watcher_afk_optionmenu.grid(row=2, column=1, padx=20, pady=(20, 10), sticky="w")

    # aw-watcher-window Option Menu
    text_aw_watcher_window = customtkinter.CTkLabel(tabview.tab("Admin-Configs"), text="aw-watcher-window:", anchor="w")
    text_aw_watcher_window.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")

    aw_watcher_window_optionmenu = customtkinter.CTkOptionMenu(tabview.tab("Admin-Configs"), dynamic_resizing=False,
                                                               values=["true", "false"])
    aw_watcher_window_optionmenu.grid(row=3, column=1, padx=20, pady=(20, 10), sticky="w")

    # Save Settings Button
    save_settings_button = customtkinter.CTkButton(tabview.tab("Admin-Configs"), text="Save Settings")
    save_settings_button.grid(row=20, column=0, columnspan=2, padx=20, pady=(20, 10))

    open_admin_center_button = customtkinter.CTkButton(tabview.tab("Admin-Configs"), text="Open Admin Center", command=lambda: open_webrowser(frame))
    open_admin_center_button.grid(row=25, column=0, columnspan=2, padx=20, pady=(20, 10))

    # center the tabview
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    tabview.add("Configurations")
    tabview.tab("Configurations").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

    # Language Option Menu
    text_language = customtkinter.CTkLabel(tabview.tab("Configurations"), text="Language:", anchor="w")
    text_language.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

    language_optionmenu = customtkinter.CTkOptionMenu(tabview.tab("Configurations"), dynamic_resizing=False,
                                                      values=["English", "Polish", "German"])
    language_optionmenu.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="w")

    # Appearance Mode Option Menu
    text_appearance_mode = customtkinter.CTkLabel(tabview.tab("Configurations"), text="Appearance Mode:", anchor="w")
    text_appearance_mode.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")

    appearance_mode_optionmenu = customtkinter.CTkOptionMenu(tabview.tab("Configurations"), dynamic_resizing=False,
                                                             values=["System", "Dark", "Light"],
                                                             command=change_appearance_mode_event)
    appearance_mode_optionmenu.grid(row=1, column=1, padx=20, pady=(20, 10), sticky="w")

    # Scaling Option Menu
    text_scaling = customtkinter.CTkLabel(tabview.tab("Configurations"), text="UI Scaling:", anchor="w")
    text_scaling.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")

    scaling_optionmenu = customtkinter.CTkOptionMenu(tabview.tab("Configurations"), dynamic_resizing=False,
                                                     values=["100%", "80%", "90%", "110%", "120%"],
                                                     command=change_scaling_event)
    scaling_optionmenu.grid(row=2, column=1, padx=20, pady=(20, 10), sticky="w")

    # Font Option Menu
    text_font = customtkinter.CTkLabel(tabview.tab("Configurations"), text="Font:", anchor="w")
    text_font.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")

    font_optionmenu = customtkinter.CTkOptionMenu(tabview.tab("Configurations"), dynamic_resizing=False,
                                                  values=["Arial", "Times New Roman", "Courier New"])
    font_optionmenu.grid(row=3, column=1, padx=20, pady=(20, 10), sticky="w")

    # Theme Option Menu
    text_theme = customtkinter.CTkLabel(tabview.tab("Configurations"), text="", anchor="w")
    text_theme.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="w")


    text_theme = customtkinter.CTkLabel(tabview.tab("Configurations"), text="", anchor="w")
    text_theme.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="w")





    
    selected_language = customtkinter.StringVar().get
    selected_appearance_mode = customtkinter.StringVar().get
    selected_scaling = customtkinter.StringVar().get
    selected_font = customtkinter.StringVar().get
    
    apply_settings_button = customtkinter.CTkButton(tabview.tab("Configurations"), text="Apply Settings", 
    command=lambda: apply_settings(selected_language, selected_appearance_mode, selected_scaling, selected_font))
    apply_settings_button.grid(row=7, columnspan=2, pady=(20, 10))
    


    # Function to apply settings
def apply_settings(language: str, appearance_mode: str, scaling: str, font: str):

        print(f"Language: {language}")
        print(f"Appearance Mode: {appearance_mode}")
        print(f"Scaling: {scaling}")
        print(f"Font: {font}")