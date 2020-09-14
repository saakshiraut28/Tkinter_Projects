from tkinter import *
from PIL import Image, ImageTk

def closewin():
    close_window = Tk()
    close_window.title("Thanks_Giving")
    close_window.geometry("400x250")
    Label(close_window, text="Thanks for visiting..  😃 \n Have a great journey..!",
    font=("Comic Sans MS", 16),bg="#e6fff0",fg="#00635a",width="450",height="250").pack()
    close_window.mainloop()

def getvals():
    print("Submiting form")

    print(f"{namevalue.get(), phonevalue.get(), emer_contactvalue.get(), addressvalue.get(), emailaddressvalue.get() }"
          f"{paymentvalue.get(), foodservicevalue.get()}")
    with open("record.txt", "a") as f:
          f.write(f"{namevalue.get(), phonevalue.get(), emer_contactvalue.get(), addressvalue.get(), emailaddressvalue.get()}"
          f"{paymentvalue.get(), foodservicevalue.get()}\n")
    closewin()


root = Tk()
root.geometry("720x660")
root.title("Travelogy")
canvas= Canvas(root,bg="#ddf0ff")



title = Label(canvas, text="___________Travelogy___________", font=("Comic Sans MS", 25), bg="#c5d0ff", width="60")
title.pack()
Label(canvas, text="Details",font=("Comic Sans MS", 17), fg="#633a4b",  bg="#ddf0ff",borderwidth=2, relief="ridge").pack()

canvas.pack() 
main_form = Frame(root, bg="#ddf0ff", padx="220",pady="1")
name = Label(main_form, text="Name", font=("Comic Sans MS", 14), fg="#001a8a",  bg="#ddf0ff")
phone = Label(main_form, text="Phone", font=("Comic Sans MS", 14), fg="#001a8a", bg="#ddf0ff")
emergency_contact = Label(main_form, text="Route", font=("Comic Sans MS", 14), fg="#001a8a", bg="#ddf0ff")
address = Label(main_form, text="Address", font=("Comic Sans MS", 14), fg="#001a8a", bg="#ddf0ff")
email = Label(main_form, text="Email_ID", font=("Comic Sans MS", 14), fg="#001a8a", bg="#ddf0ff")
payment = Label(main_form, text="Payment Mode", font=("Comic Sans MS", 14), fg="#001a8a", bg="#ddf0ff")

# dispalying text below the first one
name.grid(row=1, column=0)
phone.grid(row=2, column=0)
emergency_contact.grid(row=3, column=0)
address.grid(row=4, column=0)
email.grid(row=5, column=0)
payment.grid(row=6, column=0)

namevalue = StringVar()
phonevalue = StringVar()
emer_contactvalue = StringVar()
addressvalue = StringVar()
emailaddressvalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

# entry widget for input

nameentry = Entry(main_form, textvariable=namevalue)
phoneentry = Entry(main_form, textvariable=phonevalue)
emergency_contactentry = Entry(main_form, textvariable=emer_contactvalue)
addressentry = Entry(main_form, textvariable=addressvalue)
emailentry = Entry(main_form, textvariable=emailaddressvalue)
paymententry = Entry(main_form, textvariable=paymentvalue)

# to display boxes

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
emergency_contactentry .grid(row=3, column=3)
addressentry.grid(row=4, column=3)
emailentry.grid(row=5, column=3)
paymententry.grid(row=6, column=3)


# checkbox
foodservice = Checkbutton(main_form, text="Want to prebook your meal", variable=foodservicevalue, font=("Comic Sans MS", 12),fg="#001a8a",  bg="#ddf0ff")
foodservice.grid(row=7, column=3)

# button
Button(main_form, text="SUBMIT", command=getvals,font=("Comic Sans MS", 12),fg="#001a8a",  bg="#ddf0ff").grid(row=8, column=3)
main_form.pack(padx="0", pady="0")


img = Image.open("travel.jpg")
render = ImageTk.PhotoImage(img)
img = Label(root, image=render)
img.image = render
img.place(x=0, y=355)

      

root.mainloop()