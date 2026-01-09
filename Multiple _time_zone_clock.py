# tkinter - Used to create GUI (window, labels, buttons)
import tkinter as tk

from datetime import datetime
#pytz - Used for different country time zones
import pytz

root = tk.Tk()
root.title("Multiple Time Zone Clock")
root.attributes("-fullscreen", True)
root.configure(bg="black")

# ESC to exit(When you press ESC, the app closes)
root.bind("<Escape>", lambda e: root.destroy())

# Time zones dictionary
time_zones = {
    "India 🇮🇳": "Asia/Kolkata",
    "USA 🇺🇸": "US/Eastern",
    "UK 🇬🇧": "Europe/London",
    "Dubai 🇦🇪": "Asia/Dubai",
    "Japan 🇯🇵": "Asia/Tokyo",
    "Australia 🇦🇺": "Australia/Sydney"

}

labels = {}

# Create labels
for zone in time_zones:
    lbl = tk.Label(
        root,
        font=("Arial", 40, "bold"),
        bg="black",
        fg="cyan"
    )
    lbl.pack(pady=10)
    labels[zone] = lbl


def update_time():
    for zone, tz in time_zones.items():
        time_now = datetime.now(pytz.timezone(tz))
        current_time = time_now.strftime("%I:%M:%S %p  |  %A %d %B %Y")
        labels[zone].config(text=f"{zone} : {current_time}")
    root.after(1000, update_time)
    #Calls update_time() again after 1000 ms (1 second)


update_time()
root.mainloop()
