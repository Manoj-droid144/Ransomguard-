from tkinter import *
import tkinter as tk
from tkinter import font as tkfont 
import os
from all_paths import username_file_path,password_file_path,email_file_path,purchase_file_path
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/assets_installer")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#118BE4")
window.title("Sign up")

import subprocess
def open_final_scanner():
    subprocess.Popen(["python", "ransomguard.py"])
    window.destroy()

canvas = Canvas(
    window,
    bg = "#118BE4",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    393.9999999999999,
    7.105427357601002e-15,
    861.9999999999999,
    519.0,
    fill="#FCFCFC",
    outline="")



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_final_scanner,
    relief="flat"
)
button_1.place(
    x=555.9999999999999,
    y=432.0,
    width=180.0,
    height=55.0
)

canvas.create_text(
    26.999999999999886,
    14.000000000000007,
    anchor="nw",
    text="Welcome to \nRansomguard Installer  ",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    600,
    17.000000000000007,
    anchor="nw",
    text="Sign up ",
    fill="#505485",
    font=("Ruda Regular", 24 * -1)
)



entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    684.4999999999999,
    110.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_1.place(
    x=568.9999999999999,
    y=80.0,
    width=231.0,
    height=59.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    684.4999999999999,
    199.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_2.place(
    x=568.9999999999999,
    y=169.0,
    width=231.0,
    height=59.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    684.4999999999999,
    297.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_3.place(
    x=568.9999999999999,
    y=267.0,
    width=231.0,
    height=59.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("sign up.png"))
entry_bg_4 = canvas.create_image(
    200,
    250.0,
    image=entry_image_4
)


canvas.create_text(
    437.9999999999999,
    186.0,
    anchor="nw",
    text="Password :",
    fill="#000000",
    font=("Roboto Bold", 24 * -1)
)


canvas.create_text(
    435.9999999999999,
    96.0,
    anchor="nw",
    text="User Name :",
    fill="#000000",
    font=("Roboto Bold", 22 * -1)
)
canvas.create_text(
    484.9999999999999,
    290.0,
    anchor="nw",
    text="Email :",
    fill="#000000",
    font=("Roboto Bold", 24 * -1)
)

def submit(): 
	user_name=entry_1.get()
	password=entry_2.get()
	#email=entry_4.get()
	email=entry_3.get()
	import datetime 
	from datetime import date 
	from tkinter import messagebox 
	#date_time_obj = datetime.datetime.strptime(purchase, '%d-%m-%Y').date()
	#main_date = date_time_obj + datetime.timedelta(days=365)
	
	#remaining_days = (main_date - date.today()).days
	messagebox.showinfo("showinfo", "Login succesfull")
	name = open(username_file_path, "w") #opens file usernames.txt and gets ready to write to it
	
	name.write(user_name) #writes contents in file to usernames.txt
	name.close() #closes file
	open1 = open(username_file_path, "r") #opens file to read it
	print (open1.read()) #prints whatever is in the text file

	#Password
	name = open(password_file_path, "w") #opens file usernames.txt and gets ready to write to it
	

	name.write(password) #writes contents in file to usernames.txt
	name.close() #closes file
	open1 = open(password_file_path, "r") #opens file to read it
	print (open1.read()) #prints whatever is in the text file

	#Email
	name = open(email_file_path, "w") #opens file usernames.txt and gets ready to write to it
	

	name.write(email) #writes contents in file to usernames.txt
	name.close() #closes file
	open1 = open(email_file_path, "r") #opens file to read it
	print (open1.read()) #prints whatever is in the text file 
window.resizable(False, False)	
window.mainloop()
