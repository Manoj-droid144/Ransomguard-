try:
    from datetime import date
    from tkinter import *
    import tkinter as tk                
    from tkinter import font as tkfont  
except ImportError:
    from datetime import date
   

#Import Variable
from all_paths import icon_path
from all_paths import Picture_path


import random
time = random.randint(100, 180)
percentage_c = random.randint(1, 100)

#Link
import webbrowser
def callback(url):
    webbrowser.open_new(url)

#Import path
from all_paths import username_file_path,password_file_path,email_file_path,purchase_file_path

#Import file
with open(purchase_file_path, 'r') as file:
    pur_date = file.read().rstrip('\n')

with open(username_file_path, 'r') as file:
    username = file.read().rstrip('\n')

with open(password_file_path, 'r') as file:
    password = file.read().rstrip('\n')

with open(email_file_path, 'r') as file:
    email = file.read().rstrip('\n')
short_email = email.split("@")



First_name = username.split(" ")[0]
Last_name = username.split(" ")[-1]

import tkinter as tk
import subprocess

def open_final_scanner():
    subprocess.Popen(["python", "FINAL SCANNER.py"])

class ransomguard(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

         #Icon
        photo = PhotoImage(file = icon_path)
        self.iconphoto(False, photo)
        self.resizable(True, True)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.configure(bg = "#3A59C7")
        self.title("Ransomguard")
        self.title_font = tkfont.Font(family='Cursive', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, minsize=500, weight=1)
        container.grid_columnconfigure(0, minsize=866, weight=1)
        container.grid_columnconfigure(1, weight=1)


        self.frames = {}
        for F in (Feedback, Home, Scan, Settings, Scan_Utility):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


#Home page------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        from pathlib import Path
        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
        from PIL import Image, ImageTk

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./assets/assets_home")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        canvas = Canvas(
            self,
            bg = "red",
            height = screen_height,
            width = screen_width,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.grid(row=0, column=0, sticky="nsew")

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Settings"),
            relief="flat"
        )
        button_2.place(
            x=80.0,
            y=150.0,   
        )
        button_2.photo = button_image_2

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Feedback"),
            relief="flat"
        )
        button_3.place(
            x=80.0,
            y=310.0,          
        )

        button_3.photo = button_image_3

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_5.place(
            x=80.0,
            y=470.0,         
        )

        button_5.bind("<Button-1>", lambda e: callback("https://manoj-droid144.github.io/ransomguard/"))
        button_5.photo = button_image_5


        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))   
        image_1 = canvas.create_image(960.0,540.0,image = image_image_1)
        canvas.photo = image_image_1
        
        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_6 = Button(
            canvas,    
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command = lambda: controller.show_frame("Scan"),
            relief="flat"
        )
        button_6.place(
            x=1048.0,
            y=780.0, 
        )
        button_6.photo = button_image_6
#Home page------------------------------------------------------------------------------------------------------------------------------------------------------------------

#SETTINGS PAGE--------------------------------------------------------------------------------------------------------------------------------------------------------

class Settings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        import datetime 
        from datetime import date  
        date_time_obj = datetime.datetime.strptime(pur_date, '%d-%m-%Y').date()
        main_date = date_time_obj + datetime.timedelta(days=365)       
        remaining_days = (main_date - date.today()).days    
        from pathlib import Path
        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
        from PIL import Image, ImageTk


        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./assets/assets_settings")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Create canvas to cover the entire window
        self.canvas = Canvas(
            self,
            bg="red",
            height=screen_height,
            width=screen_width,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack(fill="both", expand=True)
        # Load and place background image on canvas
        background_image_path = relative_to_assets("background_image.png")
        background_image = Image.open(background_image_path)
        background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)
        background_image = ImageTk.PhotoImage(background_image)
        self.canvas.create_image(0, 0, anchor="nw", image=background_image)
        self.canvas.image = background_image

        button_image_3 = PhotoImage( file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Feedback"),
            relief="flat"
        )
        button_3.place(
            x=80.0,
            y=150.0,
        )
        button_3.photo = button_image_3

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=80.0,
            y=310.0,
        )

        button_5.photo = button_image_5

        button_5.bind("<Button-1>", lambda e: callback("https://manoj-droid144.github.io/ransomguard/"))
        
        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_6 = Button(
            self.canvas,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=  lambda: controller.show_frame("Scan"),
            relief="flat"
        )
        button_6.place(
            x=80.0,
            y=630.0,
        )

        button_6.photo = button_image_6
        
        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            self.canvas,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_7.place(
            x=1090.0,
            y=750.0,
        )

        button_7.photo = button_image_7
        button_7.bind("<Button-1>", lambda e: callback("https://manoj-droid144.github.io/ransomguard/"))

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        button_8 = Button(
            self.canvas,
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Home"),
            relief="flat"
        )
        button_8.place(
            x=80.0,
            y=470.0, 
        )

        button_8.photo = button_image_8
       
        self.canvas.create_text(
            1110.0,
            400.0,
            anchor="nw",
            text=""+str(date.today()),
            fill="#FFFFFF",
            font=("Amaranth Regular", 40 * -1)
        )

        self.canvas.create_text(
            900.0,
            300.0,
            anchor="nw",
            text="Name       :",
            fill="#000000",
            font=("Amaranth Regular", 40 * -1)
        )

        self.canvas.create_text(
            900.0,
            400.0,
            anchor="nw",
            text="Date         :",
            fill="#000000",
            font=("Amaranth Regular", 40 * -1)
        )

        self.canvas.create_text(
            900.0,
            500.0,
            anchor="nw",
            text="Password :",
            fill="#000000",
            font=("Amaranth Regular", 40 * -1)
        )

        self.canvas.create_text(
            1110.0,
            500.0,
            anchor="nw",
            text=""+password,
            fill="#FFFFFF",
            font=("Amaranth Regular", 40 * -1)
        )
        
        self.canvas.create_text(
            1110.0,
            600.0,
            anchor="nw",
            text=short_email[0],
            fill="#FFFFFF",
            font=("Amaranth Regular", 40 * -1)
        )

        self.canvas.create_text(
            900.0,
            600.0,
            anchor="nw",
            text="Email        :",
            fill="#000000",
            font=("Amaranth Regular", 40 * -1)
        )
        self.canvas.create_text(
           1110.0,
            300.0,
            anchor="nw",
            text=First_name,
            fill="#FFFFFF",
            font=("Amaranth Regular", 40 * -1)
        )

# end of settings page------------------------------------------------------------------------------------------------------------------------------------------------
#scan page------------------------------------------------------------------------------------------------------------------------------------------------------------
scan_decider = 0
class Scan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Scan.scan_decider =  0
        from pathlib import Path
        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
        from PIL import Image, ImageTk
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./assets/assets_scan")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.canvas = Canvas(
            self,
            bg="red",
            height=screen_height,
            width=screen_width,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack(fill="both", expand=True)

        background_image_path = relative_to_assets("background_image1.png")
        background_image = Image.open(background_image_path)
        background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)
        background_image = ImageTk.PhotoImage(background_image)
        self.canvas.create_image(0, 0, anchor="nw", image=background_image)
        self.canvas.image = background_image

        def make_something(value):
            global scan_decider
            scan_decider = value
            return scan_decider


        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Settings"),
            relief="flat"
        )
        button_2.place(
            x=80.0,
            y=150.0, 
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Feedback"),
            relief="flat"
        )
        button_3.place(
            x=80.0,
            y=310.0,
        )


        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_5.place(
            x=80.0,
            y=470.0,
        )
        button_5.bind("<Button-1>", lambda e: callback("https://manoj-droid144.github.io/ransomguard/"))

        button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        button_10 = Button(
            self.canvas,
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command= open_final_scanner ,     
            relief="flat"
        )
        button_10.place(
            x=1058.0,
            y=380.0,
        )

        button_image_12 = PhotoImage(
            file=relative_to_assets("button_12.png"))
        button_12 = Button(
            self.canvas,
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Home"),
            relief="flat"
        )
        button_12.place(
            x=80.0,
            y=630.0,
        )
        button_2.photo = button_image_2
        button_3.photo = button_image_3
        button_5.photo = button_image_5
        button_10.photo = button_image_10
        button_12.photo = button_image_12    
#end of scan page--------------------------------------------------------------------------------------------------------------------------------------------------------       
#inside scan and fullscan option page----------------------------------------------------------------------------------------------------------------------------------------      

class Scan_Utility(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button = tk.Button(self, text=" Home Page ",command=lambda: controller.show_frame("Home"))

        from tkinter import ttk
        from tkinter.messagebox import showinfo
        from pathlib import Path
        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
        from PIL import Image, ImageTk

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./assets/assets_scan")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

 
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.canvas = Canvas(
            self,
            bg = "red",
            height = screen_height,
            width = screen_width,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.pack(fill="both", expand=True)

        background_image_path = relative_to_assets("background_image.png")
        background_image = Image.open(background_image_path)
        background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)
        background_image = ImageTk.PhotoImage(background_image)
        self.canvas.create_image(0, 0, anchor="nw", image=background_image)
        self.canvas.image = background_image  

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Settings"),
            relief="flat"
        )
        button_2.place(
            x=80.0,
            y=150.0, 
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Feedback"),
            relief="flat"
        )
        button_3.place(
            x=80.0,
            y=310.0, 
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_5.place(
            x=80.0,
            y=470.0, 
        )
        button_5.bind("<Button-1>", lambda e: callback("https://manoj-droid144.github.io/ransomguard/"))

        button_image_12 = PhotoImage(
            file=relative_to_assets("button_12.png"))
        button_12 = Button(
            self.canvas,
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Home"),
            relief="flat"
        )
        button_12.place(
            x=80.0,
            y=470.0, 
        )



        #button_1.photo = button_image_1
        button_2.photo = button_image_2
        button_3.photo = button_image_3
        #button_4.photo = button_image_4
        button_5.photo = button_image_5
       # button_6.photo = button_image_6
        button_12.photo = button_image_12
        #button_14.photo = button_image_14
        #button_1.bind("<Button-1>", lambda e: callback("https://github.com/HarshscGithub/Atarbals-Modern-Antivirus/releases"))

#inside scan and fullscan option page----------------------------------------------------------------------------------------------------------------------------------------      



#SCANNER OPERATIONS-----------------------------------------------------------------------------------------------------------------------------------------------------
        

        def start():
            if scan_decider == 0:
                return multi_scan(self)
            elif scan_decider == 1:
                return directory(self)
            


        button_image_13 = PhotoImage(
            file=relative_to_assets("button_13.png"))
        button_13 = Button(
            self.canvas,
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: start(),
            relief="flat"
        )
        button_13.place(
            x=1200.0,
            y=600.0,
        )
        button_13.photo = button_image_13

        def multi_scan(self):
            import scan.engine as m
            a = m.start(1)
            b = a[0]
            filename = a[1]
            viruse_files = m.main(b,filename)
            print(viruse_files)
            m.check(filename,viruse_files)

            import tkinter 
            from PIL import ImageTk, Image 
            import os 

            # creating main self 
            

            # loading the image 
            img = ImageTk.PhotoImage(Image.open(Picture_path)) 

            # reading the image 
            self.panel = tkinter.Label(self, image = img) 

            # setting the application 
            self.panel.place(x=960,y=540)

            # running the application 
            self.mainloop()

            return



        def directory(self):
            import scan.engine as m
            a = m.start(0)
            b = a[0]
            filename = a[1]
            viruse_files = m.main(b,filename)
            print(viruse_files)
            m.check(filename,viruse_files)

            import tkinter 
            from PIL import ImageTk, Image 
            import os 

            # creating main self 
            

            # loading the image 
            img = ImageTk.PhotoImage(Image.open(Picture_path)) 

            # reading the image 
            self.panel = tkinter.Label(self, image = img) 

            # setting the application 
            self.panel.place(x=380,y=210)

            # running the application 
            self.mainloop()

            return


        def start_scan(self):   
            def update_progress_label():
                return f"Scanning Progress: {self.pb['value']}%"

            self.pb = ttk.Progressbar(
                self,
                orient='horizontal',
                mode='determinate',
                length=280
            )
            # place the progressbar
            self.pb.place(x=430,y=160)

            # label
            self.value_label = ttk.Label(self, text=update_progress_label())
            self.value_label.place(x=500,y=190)

            
            
            self.percentage = 0
            
            self.load_bar()
 
    def load_bar(self):
        pb = self.pb 
        value_label = self.value_label 

        
        
        def update_progress_label():
            return f"Current Progress: {pb['value']}%"

        pb['value'] += 2
        value_label['text'] = update_progress_label()

        self.percentage +=2 #Edit 2
        

        if self.percentage == 100 and pb['value'] == 100:
            

            # importing required packages 
            import tkinter 
            from PIL import ImageTk, Image 
            import os 

            # creating main self 
            

            # loading the image 
            img = ImageTk.PhotoImage(Image.open(Picture_path)) 

            # reading the image 
            self.panel = tkinter.Label(self, image = img) 

            # setting the application 
            self.panel.place(x=380,y=210)

            
            value_label['text'] = update_progress_label()

            from tkinter import messagebox
            messagebox.showinfo("Congratulations", "Scanned succesfully and No virus found!")

            # running the application 
            self.mainloop()


            return
        
        else:
            
            self.after(percentage_c,self.load_bar)  # Edit 100

    
    def clear(self):
        try:
            self.panel.destroy()
            self.pb.destroy()
            self.value_label.destroy()
            from tkinter import messagebox
            messagebox.showinfo("Congratulations", "Cleared Succeessfully.")
        
        except:
            from tkinter import messagebox
            messagebox.showerror("Clearing error", "Please first Scan and then press Clear button.")
        
#SACNNER OPERATIONS----------------------------------------------------------------------------------------------------------------------------------------------------
         
                            

        
#FEEDBACK OPTION--------------------------------------------------------------------------------------------------------------------------------------------------------

import pywhatkit as kit        
class Feedback(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #label = tk.Label(self, text="Feed Back", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)
         
        def submit():
            # Get user input
            name = entry_2.get()
            subject = entry_3.get()
            feedback = entry_1.get("1.0", tk.END)

        # Format feedback message
            message = f"Feedback from {name}\nSubject: {subject}\nFeedback:{feedback}"

        # Send feedback to WhatsApp
            try:
                phone_number = '+918825902972'
                kit.sendwhatmsg_instantly(phone_number, message)
                messagebox.showinfo("Info", "Feedback sent successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to send feedback: {str(e)}")


        from pathlib import Path
        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
        from PIL import Image, ImageTk

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./assets/assets_feedback")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()


        self.canvas = Canvas(
            self,
            bg="red",
            height=screen_height,
            width=screen_width,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack(fill="both", expand=True)
        background_image_path = relative_to_assets("background_image.png")
        background_image = Image.open(background_image_path)
        background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)
        background_image = ImageTk.PhotoImage(background_image)
        self.canvas.create_image(0, 0, anchor="nw", image=background_image)
        self.canvas.image = background_image  

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Settings"),
            relief="flat"
        )
        button_2.place(
            x=80.0,
            y=150.0, 
        )
        button_2.photo = button_image_2

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        button_5.place(
            x=80.0,
            y=310.0,
        )

        button_5.bind("<Button-1>", lambda e: callback("https://manoj-droid144.github.io/ransomguard/"))
        button_5.photo = button_image_5

        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_6 = Button(
            self.canvas,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Scan"),
            relief="flat"
        )
        button_6.place(
            x=80.0,
            y=630.0,
        )

        button_6.photo = button_image_6

        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            self.canvas,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: submit(),
            relief="flat"
        )
        button_7.place(
            x=1343.0,
            y=800.0,
            width=160.0,
            height=50.0
        )

        button_7.photo = button_image_7

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        button_8 = Button(
            self.canvas,
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Home"),
            relief="flat"
        )
        button_8.place(
            x=80.0,
            y=470.0, 
        )
        button_8.photo = button_image_8

        entry_1 = Text(
            self.canvas,
            bd=0,
            bg = "white",
            highlightthickness=0
        )
        entry_1.place(
            x=600.0,
            y=455.0,
            width=900.0,
            height=321.0
        )
        entry_2 = Entry(
            self.canvas,
            bd=0,
            bg="white",
            highlightthickness=1
        )
        entry_2.place(
            x=600.0,
            y=250.0,
            width=600.0,
            height=50.0
        )

        entry_3 = Entry(
            self.canvas,
            bd=0,
            bg="white",
            highlightthickness=0
        )
        entry_3.place(
            x=600.0,
            y=350.0,
            width=600.0,
            height=50.0
        )
        self.canvas.create_text(
            600.0,
            200.0,
            anchor="nw",
            text="Name :",
            fill="white",
            font=("serif", 40 * -1)
        )

        self. canvas.create_text(
            600.0,
            300.0,
            anchor="nw",
            text="Subject :",
            fill="white",
            font=("serif", 40 * -1)
        )

        self.canvas.create_text(
            600.0,
            410.0,
            anchor="nw",
            text="Feedback :",
            fill="white",
            font=("serif", 40 * -1)
        )
def run_app():
    app = ransomguard()
    app.mainloop()

if __name__ == "__main__":
    run_app()
#END OF FEEDBACK--------------------------------------------------------------------------------------------------------------------------------------------------------