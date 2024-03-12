import sys
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
    
    up_text_label = Ctk.CTkLabel(frame, text="The system is up for:", font=("Arial", 15), anchor="center",
                                 fg_color="transparent", text_color=("gray10", "gray90"))  # Create a label
    
    up_text_label.grid(row=0, column=0, pady=25, padx=20, sticky="nsew")  # Add sticky="nsew" to center the label
    
    clock = Ctk.CTkLabel(frame, font=("times", 50, "bold"), anchor="center",
                            fg_color="transparent", text_color=("gray10", "gray90"))  # Create a label
    
    clock.grid(row=2, column=0, pady=25, padx=20, sticky="nsew")  # Add sticky="nsew" to center the clock

    # Create and start a separate thread for updating the clock
    thread = threading.Thread(target=update_clock, args=(clock,))
    thread.daemon = True  # Set the thread as a daemon so it exits when the main program ends
    thread.start()

