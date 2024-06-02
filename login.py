from tkinter import *
from tkinter import messagebox
import os
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('Sign in')
        self.root.geometry('925x500+300+200')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)
        photo = PhotoImage(file='Antivirus_Logo.png')
        self.root.iconphoto(False, photo)

 # Load the image
        self.img = PhotoImage(file='login.png')

        # Display the image on a Label
        self.image_label = Label(self.root, image=self.img, bg='white')
        self.image_label.place(x=50, y=50)

        frame = Frame(self.root, width=350, height=350, bg="white")
        frame.place(x=488, y=70)
        heading = Label(frame, text='Log in', fg='#57a1f8', bg='white',
                        font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=120, y=5)

        self.user = Entry(frame, width=25, fg='black', border=0, bg="white",
                          font=('Microsoft YaHei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', self.on_enter)
        self.user.bind('<FocusOut>', self.on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        self.code = Entry(frame, width=25, fg='black', border=0, bg="white",
                          font=('Microsoft YaHei UI Light', 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        self.code.bind('<FocusIn>', self.on_enter)
        self.code.bind('<FocusOut>', self.on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        log_in = Button(frame, width=30, pady=10, text='log in', border=0,
                        bg='#57a1f8', cursor='hand2', fg='white',
                        font=('Microsoft YaHei UI Light', 12, 'bold'),
                        command=self.open_another_file)
        log_in.place(x=25, y=220)

    def on_enter(self, e):
        widget = e.widget
        widget.delete(0, 'end')

    def on_leave(self, e):
        widget = e.widget
        if not widget.get():
            if widget == self.user:
                widget.insert(0, 'Username')
            elif widget == self.code:
                widget.insert(0, 'Password')

    def open_another_file(self):
        # Check if the username and password are correct
        if self.user.get() == "user" and self.code.get() == "password":
            # Replace 'file_to_open.py' with the name of the Python file you want to open

            root.destroy()
            os.system('python ransomguard.py')

        else:
            messagebox.showwarning("Invalid Credentials", "Incorrect username or password!")


if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
