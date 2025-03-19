from tkinter import *
from Notes import *
from tkinter import messagebox
import re
from tkinter import ttk

def readMe():
    read = adreadMe()
    frameTxt.insert(END, read)

def currentWin():
     # Closes the program
    window.quit()

def validate_ip(event):
    ip = switchIPEntry.get()
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if pattern.match(ip):
        parts = ip.split(".")
        valid = all(0 <= int(part) <= 255 for part in parts)
        if valid:
            switchIPEntry.config(bg="#8CBD8C")
            print('Valid IP')
        else:
            switchIPEntry.config(bg="#FFA896")
            messagebox.showinfo("IP Incorrect", "IP Address must be in the following format: "
                                "0-255.0-255.0-255.0-255\n"
                                "For example: 10.12.0.5")
   # else:
     #   switchIPEntry.config(bg="red")

def validate_string(s):
    s = hostNameEntry.get()
    pattern = re.compile(r'^[A-Za-z0-9]{8}\d{2}w$')
    if bool(pattern.match(s)):
        hostNameEntry.config(bg="#8CBD8C")
        print("Valid")
    else:
        hostNameEntry.config(bg="#FFA896")
        messagebox.showinfo("Hostname Incorrect", "Hostname must be in the following format: Eight letters followed by two digits, then W. For example: ASDFGHJK02W")
        print("Invalid")


window = Tk()
window.configure(bg='white')
window.title("Adtran Configuration Program")

window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=400)

# Create two frames for the columns
frmLeft = Frame(window, relief=RAISED)
frmMiddle = Frame(window, relief=RAISED)
frmRight = Frame(window)

# Pack the frames side by side
frmLeft.pack(side="left", fill="both", expand=True)
frmMiddle.pack(side="left", fill="both", expand=True)
frmRight.pack(side="left", fill="both", expand=True)

# text Window
frameTxt = Text(frmRight)
frameTxt.grid(row=0, column=0, sticky="nsew")

# Ensure frmRight expands properly
frmRight.rowconfigure(0, weight=1)
frmRight.columnconfigure(0, weight=1)

# Create Entry Fields
hostNameEntry = Entry(frmLeft, justify="center", font=('Arial', 15))
hostNameEntry.insert(0, "Enter Hostname")
hostNameEntry.bind("<FocusIn>", lambda e: hostNameEntry.delete('0', 'end'))
hostNameEntry.bind("<FocusOut>", validate_string)
hostNameEntry.grid(row=0, column=0, padx=(0, 10))

switchIPEntry = Entry(frmLeft, justify="center", font=('Arial', 15))
switchIPEntry.insert(0, "Enter Switch IP")
switchIPEntry.bind("<FocusIn>", lambda e: switchIPEntry.delete('0', 'end'))
switchIPEntry.bind("<FocusOut>", validate_ip)
switchIPEntry.grid(row=0, column=1)

# Create Labels
port23 = Label(frmLeft, text="Port 23", font=('Arial', 15), borderwidth=2, relief="ridge")
port23.grid(row=1, column=0, sticky="ew")
subMask = Label(frmLeft, text="Subnet Mask", font=('Arial', 15), borderwidth=2, relief="ridge")
subMask.grid(row=2, column=0, sticky="ew")
connectVGW = Label(frmLeft, text="Connect to VGW", font=('Arial', 15), borderwidth=2, relief="ridge")
connectVGW.grid(row=3, column=0, sticky="ew")

# Create a variable to store the selected value of the dropdown menu
port23Var = StringVar(value="Yes")
subMaskVar = StringVar(value="255.255.252.0")
connectVGWVar = StringVar(value="Yes")

# Create a dropdown menu with Yes/No options
dropMenuPort = OptionMenu(frmLeft, port23Var, "Yes", "No")
dropMenuPort.grid(row=1, column=1, sticky="ew")
dropMenuMask = OptionMenu(frmLeft, subMaskVar, "255.255.252.0", "255.255.255.0")
dropMenuMask.grid(row=2, column=1, sticky="ew") 
dropMenuVGW = OptionMenu(frmLeft, connectVGWVar, "Yes", "No")
dropMenuVGW.grid(row=3, column=1, sticky="ew")

menu = dropMenuPort.nametowidget(dropMenuPort.menuname)
menu.configure(font=('Arial', 15))
menu = dropMenuMask.nametowidget(dropMenuMask.menuname)
menu.configure(font=('Arial', 15))
menu = dropMenuVGW.nametowidget(dropMenuVGW.menuname)
menu.configure(font=('Arial', 15))

# Create Buttons
btn_submit = Button(frmLeft, text="Submit".upper(), 
                    font=('Arial Black', 15),
                    cursor="hand2",
                    activebackground="#8CBD8C",
                    activeforeground="black")
btn_submit.grid(row=5, column=0, columnspan=2, sticky="nsew")
btn_Exit = Button(frmLeft, 
                  text="Exit".upper(),
                  font=('Arial Black', 15), 
                  cursor="hand2", 
                  activebackground='#FFA896', command=currentWin)
btn_Exit.grid(row=6, column=0, columnspan=2, sticky="nsew")

readMe()
window.mainloop()