from customtkinter import *
import webbrowser
from PIL import Image

def save_activity_window(app):

    set_appearance_mode("light")
    images_relative_path = "images/"
    
    main_view = app

    title_frame = CTkFrame(master=main_view, fg_color="transparent", width=1300, height=100)
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

    
    CTkLabel(master=title_frame, text="Save Activity Data", font=("Arial Black", 25), text_color="#601E88").pack(anchor="nw", side="left")

    CTkButton(master=title_frame, text="+ Save",  font=("Arial Black", 15), text_color="#fff", fg_color="#601E88", hover_color="#E44982").pack(anchor="ne", side="right")


    text_how_to = """This is a intuitive application crafted to seamlessly monitor your digital routines across various devices.

    Guided by the ethos of open-source development and a commitment to safeguarding user privacy, we emerges as a versatile solution that effortlessly spans different platforms. Offering a captivating departure from traditional services like RescueTime, ManicTime, and WakaTime, it empowers individuals to glean profound insights into their digital engagements.

    Whether fine-tuning productivity, orchestrating project timelines, combating detrimental screen habits, or simply gaining clarity on time management, This application proves invaluable in deciphering the intricacies of our digital existence.
    
    
    - How to save your data ?
    
        1. Click on the "Save" button below.
        2. Wait for open a new tab in your default browser.
        3. Wait for open a explorer window to save your data.
        4. Rename the file to: "YourName-Date" and save it in a secure place.
        5. Done!
        
    - How to send your data to us ?
    
        1. Open Microsoft 365.
        2. Open SharePoint and go to the "TimeTracker" site.
        3. Select the folder with your name or create a new one if you don't have it.
        4. Upload the file that you saved.
        5. Done!
    
    """
    search_container = CTkScrollableFrame(master=main_view, height=400, fg_color="#F0F0F0")
    search_container.pack(fill="x", pady=(45, 0), padx=27)
    CTkLabel(master=search_container, text=text_how_to, font=("Arial", 15), text_color="#601E88").pack(anchor="nw", pady=(25,0), padx=27)
    
    CTkLabel(master=search_container, text="Status", font=("Arial Bold", 17), text_color="#601E88", justify="left").pack(anchor="nw", pady=(10,0), padx=27)
    status_var = IntVar(value=0)
    CTkRadioButton(master=main_view, variable=status_var, value=1,text="I do not agree with the policy", font=("Arial Bold", 14), text_color="#601E88", fg_color="#601E88", border_color="#601E88", hover_color="#601E88").pack(anchor="nw", pady=(16,0), padx=27)
    CTkRadioButton(master=main_view, variable=status_var, value=2,text="I read and agree with the data policy", font=("Arial Bold", 14), text_color="#601E88", fg_color="#601E88", border_color="#601E88", hover_color="#601E88").pack(anchor="nw", pady=(16,0), padx=27)
    
   

def save_data():
    webbrowser.open("http://localhost:5600/api/0/export")

    return True