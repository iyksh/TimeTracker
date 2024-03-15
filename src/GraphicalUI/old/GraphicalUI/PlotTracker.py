import json
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt

def create_pie_chart(data_path, frame: tk.Frame):
    # Load the JSON data
    with open(data_path) as f:
        data = json.load(f)

    # Initialize a dictionary to store the total duration for each app
    app_durations = {}

    # Loop through the events
    for event in data['buckets']['aw-watcher-window_LAPTOP-PQUI9S75']['events']:
        app = event['data']['app']
        duration = event['duration']

        # Add the duration to the total for the app
        if app in app_durations:
            app_durations[app] += duration
        else:
            app_durations[app] = duration

    # Create a single pie chart for all the app durations
    apps = list(app_durations.keys())
    durations = list(app_durations.values())

    fig, ax = plt.subplots()
    ax.pie(durations, labels=apps, autopct='%1.1f%%')
    ax.set_title('Time Spent on Each App')
    ax.axis('equal')

    # Convert the pie chart to a Tkinter-compatible format
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Find the most used apps with a duration of 60% or more
    most_used_apps = [app for app, duration in app_durations.items() if duration >= sum(durations) * 0.4]

    # Create a label to display the most used apps
    most_used_label = tk.Label(frame, text=f"Most Used Apps (>=40%): {', '.join(most_used_apps)}")
    most_used_label.pack()

