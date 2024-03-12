import customtkinter  
import webbrowser
from tkinter import ttk

def save_window(frame):
    frame.columnconfigure(0, weight=1)  # Center the content horizontally
    frame.rowconfigure([0, 1, 2], weight=1)  # Center the content vertically

    label1 = customtkinter.CTkLabel(frame, text="Save Your Data!", font=("Arial Bold", 30), anchor="center",
                                    fg_color="transparent", text_color=("gray10", "gray90"))  # Create a label
    label2 = customtkinter.CTkLabel(frame, text="Please, read all the text below before saving your data",
                                    fg_color="transparent", text_color=("gray10", "gray90"))  # Create a label

    text = """This is a intuitive application crafted to seamlessly monitor your digital routines across various devices.

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

    text_widget = customtkinter.CTkTextbox(frame, font=("Arial", 15), wrap="word")
    text_widget.insert("1.0", text)
    text_widget.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

    # Add a scrollbar
    scrollbar = customtkinter.CTkScrollbar(frame, command=text_widget.yview)
    scrollbar.grid(row=2, column=1, sticky="ns")
    text_widget.configure(yscrollcommand=scrollbar.set)

    label3 = customtkinter.CTkLabel(frame, text="Note: This application does not store any data on the cloud or any other server.\nAll data is stored locally on your device."+\
        "Make sure to read the privacy policy before using this application.", font=("Arial", 15), anchor="center",
        fg_color="transparent", text_color=("gray10", "gray90")) 


    button = customtkinter.CTkButton(frame, text="Save", corner_radius=6, command=save_data)

    label1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    label2.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
    
    label3.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
    button.grid(row=4, column=0, padx=20, pady=20, sticky="nsew")

    # Adjust button width to fit content
    button.update()
    button_width = button.winfo_reqwidth() + 20  # Add padding
    button.configure(width=button_width)

    
def save_data():
    webbrowser.open("http://localhost:5600/api/0/export")

    return True