from tkinter import *


def close_window():
    # Closes the program
    window.destroy()

def adtran():
    print("In Adtran")
    window.destroy()
    import Adtran

def audio():
    print("In Audio Codes")
    window.destroy()
    import Audio

def cisco():
    print("In Cisco")
    window.destroy()
    import Cisco

#Create Window
window = Tk()
window.configure(bg='white')
window.rowconfigure(0)
window.columnconfigure(1)
window.title("Conversion Program")

#Crate Label
lbl_Title = Label(window, 
                  text="Configuration Program",
                  font=('Arial Black', 40, 'bold'),
                  bg='white')
lbl_Title.grid(row=0,column=0, columnspan=3, padx=5 ,pady=(2, 10), sticky="ew")
lbl_NON_CML = Label(window, 
                  text="NON CML",
                  font=('Arial Black', 20))
lbl_NON_CML.grid(row=1, column=0, columnspan=3, sticky="ew")
btn_CML = Button(window, 
                  text="CML",
                  font=('Arial Black', 20))
btn_CML.grid(row=3, column=0, columnspan=3, sticky="ew")


#Create Buttons

btn_Adtran = Button(window, 
                    text="Adtran",
                    font=('Arial', 20), cursor="hand2" ,
                    activebackground='#8CBD8C', command=adtran)
btn_Adtran.grid(row=2, column=0, padx=0,pady=0,sticky="ew")
btn_Audio = Button(window, 
                   text="Audio Codes",
                   font=('Arial',20), cursor="hand2", 
                   activebackground='#8CBD8C', command=audio)
btn_Audio.grid(row=2, column=1, padx=0, pady=0,sticky="ew")
btn_Cisco = Button(window, 
                   text="Cisco",
                   font=('Arial', 20), cursor="hand2", 
                   activebackground='#8CBD8C', command=cisco)
btn_Cisco.grid(row=2, column=2, padx=0, pady=0,sticky="ew")


btn_Adtran = Button(window, 
                    text="Adtran",
                    font=('Arial', 20), cursor="hand2" ,
                    activebackground='#8CBD8C', command=adtran)
btn_Adtran.grid(row=4, column=0, padx=0,pady=0,sticky="ew")
btn_Audio = Button(window, 
                   text="Audio Codes",
                   font=('Arial',20), cursor="hand2", 
                   activebackground='#8CBD8C', command=audio)
btn_Audio.grid(row=4, column=1, padx=0, pady=0,sticky="ew")
btn_Cisco = Button(window, 
                   text="Cisco",
                   font=('Arial', 20), cursor="hand2", 
                   activebackground='#8CBD8C', command=cisco)
btn_Cisco.grid(row=4, column=2, padx=0, pady=0,sticky="ew")
btn_Exit = Button(window, 
                  text="Exit",
                  font=('Arial Black', 20), cursor="hand2", 
                  activebackground='#FFA896', command = close_window)
btn_Exit.grid(row=8, column=0, columnspan=3, sticky="ew")


#Run Window
window.mainloop()
