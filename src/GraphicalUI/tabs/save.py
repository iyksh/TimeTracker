import customtkinter  
import webbrowser

def save_window(frame):
    frame.columnconfigure(0, weight=1)  # Center the content horizontally
    frame.rowconfigure([0, 1, 2], weight=1)  # Center the content vertically

    label1 = customtkinter.CTkLabel(frame, text="Save Your Data!", font=("Arial Bold", 30), anchor="center",
                                   fg_color="transparent", text_color=("gray10", "gray90"))  # Create a label
    label2 = customtkinter.CTkLabel(frame, text="Click the button below to save your data\nWill open a new tab in your default web browser",
                                   fg_color="transparent", text_color=("gray10", "gray90"))  # Create a label

    button = customtkinter.CTkButton(frame, text="Save", corner_radius=6, command=save_data, width=400)

    label1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    label2.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
    button.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

    label3 = customtkinter.CTkLabel(frame, text="Known what and why will be saved.", font=("Arial Bold", 30), anchor="center",
                                      fg_color="transparent", text_color=("gray10", "gray90"))  # Create a label
    
    text = """This is a intuitive application crafted to seamlessly monitor your digital routines across various devices.

    Guided by the ethos of open-source development and a commitment to safeguarding user privacy, we emerges as a versatile solution that effortlessly spans different platforms. Offering a captivating departure from traditional services like RescueTime, ManicTime, and WakaTime, it empowers individuals to glean profound insights into their digital engagements.

    Whether fine-tuning productivity, orchestrating project timelines, combating detrimental screen habits, or simply gaining clarity on time management, This application proves invaluable in deciphering the intricacies of our digital existence."""


    # Create a scrollbar
    scrollbar = customtkinter.CTkScrollbar(frame)
    scrollbar.grid(row=3, column=1, sticky="ns")

    # Create a text widget
    text_widget = customtkinter.CTkTextbox(frame, font=("Arial", 15), fg_color="transparent", text_color=("gray10", "gray90"))
    text_widget.insert("1.0", text)
    text_widget.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")

    # Configure the scrollbar to work with the text widget
    scrollbar.configure(command=text_widget.yview)
    text_widget.configure(yscrollcommand=scrollbar.set)
          
    
    
    
def save_data():
    webbrowser.open("http://localhost:5600/api/0/export")

    return True