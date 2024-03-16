from customtkinter import *
from CTkTable import CTkTable
from PIL import Image


def tasks_running_window(app):

    set_appearance_mode("light")
    images_relative_path = "images/"
    
    main_view = app

    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

    
    CTkLabel(master=title_frame, text="Tasks Running", font=("Arial Black", 25), text_color="#601E88").pack(anchor="nw", side="left")
    CTkButton(master=title_frame, text="+ Edit Task",  font=("Arial Black", 15), text_color="#fff", fg_color="#601E88", hover_color="#E44982").pack(anchor="ne", side="right")
    
    metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
    metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(36, 0))

    orders_metric = CTkFrame(master=metrics_frame, fg_color="#601E88", width=200, height=60)
    orders_metric.grid_propagate(0)
    orders_metric.pack(side="left")

    logitics_img_data = Image.open(images_relative_path + "delivered_icon.png")
    logistics_img = CTkImage(light_image=logitics_img_data, dark_image=logitics_img_data, size=(43, 43))

    CTkLabel(master=orders_metric, image=logistics_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

    CTkLabel(master=orders_metric, text="Tasks Running", text_color="#fff", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=orders_metric, text="4", text_color="#fff",font=("Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

    search_container = CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
    search_container.pack(fill="x", pady=(45, 0), padx=27)

    CTkEntry(master=search_container, width=305, placeholder_text="Search Task", border_color="#601E88", border_width=2).pack(side="left", padx=(13, 0), pady=15)

    CTkComboBox(master=search_container, width=125, values=["Date", "Most Recent Order", "Least Recent Order"], button_color="#601E88", border_color="#601E88", border_width=2, button_hover_color="#E44982",dropdown_hover_color="#E44982" , dropdown_fg_color="#601E88", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)
    CTkComboBox(master=search_container, width=125, values=["Status", "Processing", "Confirmed", "Packing", "Shipping", "Delivered", "Cancelled"], button_color="#601E88", border_color="#601E88", border_width=2, button_hover_color="#E44982",dropdown_hover_color="#E44982" , dropdown_fg_color="#601E88", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)

    table_data = [
        ["Date", "Task", "Employee", "Email", "Start Time", "End Time", "Status", "Priority", "Notes"],
        ['2021-09-03', 'Customer Support', 'Alice Johnson', "alice@email.com", '09:00:00', '10:00:00', "In Progress", 'Low', 'Follow-up needed'],
        ["2021-09-04", "Development", "Bob Thompson", "bob@example.com", "13:00:00", "15:00:00", "In Progress", "High", "Debugging required"],
        ["2021-09-05", "Meeting", "Sarah Lee", "sarah@example.com", "11:30:00", "12:30:00", "In Progress", "Medium", "Agenda to be prepared"],
        ["2021-09-06", "Training", "Michael Brown", "michael@email.com", "10:00:00", "12:00:00", "In Progress", "High", "Materials distributed"],
    ]


    table_frame = CTkScrollableFrame(master=main_view, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#601E88", hover_color="#B4B4B4")
    table.edit_row(0, text_color="#fff", hover_color="#601E88")
    table.pack(expand=True)
    

    


