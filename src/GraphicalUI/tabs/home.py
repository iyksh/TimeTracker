import customtkinter as Ctk
import time
import threading
import psutil

def times(clock):
    try:
        uptime = int(time.time() - psutil.boot_time())
        hours, remainder = divmod(uptime, 3600)
        minutes, seconds = divmod(remainder, 60)
        current_time = f"{hours:02d}:{minutes:02d}:{seconds:02d} Hours"
        
        clock.configure(text=current_time)

    except Exception as e:
        return

def update_clock(clock):
    while True:
        times(clock)
        time.sleep(1)

def home_window(frame):
    
    clock = Ctk.CTkLabel(frame, font=("times", 50, "bold"), anchor="center",
                            fg_color="transparent", text_color=("gray10", "gray90"))  # Create a label
    
    clock.pack(pady=25, padx=20, anchor="center")  # Use pack and set anchor to center


    entry_task = Ctk.CTkEntry(frame, placeholder_text="Add Task")
    add_button_ = Ctk.CTkButton(master=frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Add")
    
    entry_task.pack(pady=25, padx=20, anchor="center")
    add_button_.pack(pady=25, padx=20, anchor="center")
    


    # Create and start a separate thread for updating the clock
    thread = threading.Thread(target=update_clock, args=(clock,))
    thread.daemon = True  # Set the thread as a daemon so it exits when the main program ends
    thread.start()