# A program that saves all of your apps. So that you can fetch and use them anytime just in a click.

import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.title("SAVE_APPS")
apps = []



def saveApps():

    for widget in frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfilename(initialdir="/", title="Select files",
                filetypes=(("executable", "*.exe"),("All files", "*.*")))
    apps.append(filename)
    for app in apps:
        print(app)
        with open("saved_app.txt","a") as f:
            f.write(app + "\n")

def appsRun():
    for app in apps:
        os.startfile(app)

def appsReload():
    with open("saved_app.txt","r") as f:
        location = f.read()
        tk.Label(frame, text=location).pack()



canvas = tk.Canvas(root, height="550", width="500", bg="#011a29")
canvas.pack()

frame = tk.Frame(canvas, bg="#fff")
frame.place( height="450", width="400", relx=0.1, rely=0.1)


open_button = tk.Button(root, text="OPEN", width="10", command=saveApps)
open_button.pack()

close_button = tk.Button(root, text="RUN", width="10", command=appsRun)
close_button.pack()

reload_button = tk.Button(root, text="RELOAD", width="10", command=appsReload)
reload_button.pack()

with open("saved_app.txt","r") as f:
    location = f.read()
    tk.Label(frame, text=location).pack()


root.mainloop()

