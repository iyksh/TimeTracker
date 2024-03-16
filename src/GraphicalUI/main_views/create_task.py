import datetime
from customtkinter import *
import tkinter
from PIL import Image

def create_task_window(frame:tkinter.Frame, user_email:str):

    tasks = ["Insurances", "Orders", "Returns", "Payments", "Administration","Others"]
    set_appearance_mode("light")

    main_view = frame

    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))
    
    CTkButton(master=title_frame, text="+ Start Task",  font=("Arial Black", 15), text_color="#fff", fg_color="#601E88", hover_color="#E44982").pack(anchor="ne", side="right")

    CTkLabel(master=title_frame, text="Create Task", font=("Arial Black", 25), text_color="#601E88").pack(anchor="nw", pady=(29,0), padx=27, side="left")
    CTkLabel(master=main_view, text="Task", font=("Arial Bold", 17), text_color="#601E88").pack(anchor="nw", pady=(25,0), padx=27)
    
    #.pack(side="left", padx=(13, 0), pady=15)

    task_combobox = CTkComboBox(master=main_view, width=1000, height=40,values=tasks, button_color="#601E88", border_color="#601E88", border_width=2, button_hover_color="#E44982",dropdown_hover_color="#E44982" , dropdown_fg_color="#601E88", dropdown_text_color="#fff")
    task_combobox.pack(pady=(10,0), padx=27)

    CTkLabel(master=main_view, text="Customer E-mail", font=("Arial Bold", 17), text_color="#601E88").pack(anchor="nw", pady=(10,0), padx=27)

    CTkEntry(master=main_view, fg_color="#F0F0F0", border_width=0).pack(fill="x", pady=(10,0), padx=27, ipady=10)


    grid = CTkFrame(master=main_view, fg_color="transparent")
    grid.pack(fill="both", padx=27, pady=(31,0))

    CTkLabel(master=grid, text="Customer", font=("Arial Bold", 17), text_color="#601E88", justify="left").grid(row=0, column=0, sticky="w")
    CTkEntry(master=grid, fg_color="#F0F0F0", border_width=0, width=300).grid(row=1, column=0, ipady=10)

    
    CTkLabel(master=grid, text="Priority", font=("Arial Bold", 17), text_color="#601E88", justify="left").grid(row=0, column=1, sticky="w", padx=(25,0))
    priority_combobox = CTkComboBox(master=grid, width=300, height=56, values=["High", "Medium", "Low"], button_color="#601E88", border_color="#601E88", border_width=2, button_hover_color="#E44982",dropdown_hover_color="#E44982" , dropdown_fg_color="#601E88", dropdown_text_color="#fff")
    priority_combobox.grid(row=1, column=1, padx=(13,0), pady=(0,0))
    
    CTkLabel(master=grid, text="Employee", font=("Arial Bold", 17), text_color="#601E88", justify="left").grid(row=0, column=2, sticky="w", padx=(25, 0))
    CTkLabel(master=grid, fg_color="#F0F0F0", corner_radius=10, width=300, text=user_email, text_color="black", anchor="w").grid(row=1, column=2, ipady=10, padx=(24,0))

    CTkLabel(master=grid, text="Status", font=("Arial Bold", 17), text_color="#601E88", justify="left").grid(row=2, column=0, sticky="w", ipady=15)

    status_var = tkinter.IntVar(value=0)

    CTkRadioButton(master=grid, variable=status_var, value=0, text="Confirmed", font=("Arial Bold", 14), text_color="#601E88", fg_color="#601E88", border_color="#601E88", hover_color="#601E88").grid(row=3, column=0, sticky="w", pady=(16,0))
    CTkRadioButton(master=grid, variable=status_var, value=1,text="Pending", font=("Arial Bold", 14), text_color="#601E88", fg_color="#601E88", border_color="#601E88", hover_color="#601E88").grid(row=4, column=0, sticky="w", pady=(16,0))
    CTkRadioButton(master=grid, variable=status_var, value=2,text="Scheduled", font=("Arial Bold", 14), text_color="#601E88", fg_color="#601E88", border_color="#601E88", hover_color="#601E88").grid(row=5, column=0, sticky="w", pady=(16,0))
    CTkRadioButton(master=grid, variable=status_var, value=3,text="Processing", font=("Arial Bold", 14), text_color="#601E88", fg_color="#601E88", border_color="#601E88", hover_color="#601E88").grid(row=6, column=0, sticky="w", pady=(16,0))
    
    CTkLabel(master=grid, text="Notes", font=("Arial Bold", 17), text_color="#601E88", justify="left").grid(row=2, column=1, sticky="w", ipady=15, padx=(24,0))
    CTkTextbox(master=grid, fg_color="#F0F0F0", width=300, height=100, corner_radius=8).grid(row=3, column=1, rowspan=5, sticky="w", ipady=15, padx=(24,0))
    
    CTkLabel(master=grid, text="Start Time", font=("Arial Bold", 17), text_color="#601E88", justify="left").grid(row=2, column=2, sticky="w", padx=(24,0))
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    CTkLabel(master=grid, fg_color="#F0F0F0", corner_radius=10, width=300, text=current_time, text_color="black", anchor="w").grid(row=3, column=2, ipady=15, padx=(24,0), sticky="w")

    
    actions= CTkFrame(master=main_view, fg_color="transparent")
    actions.pack(fill="both")