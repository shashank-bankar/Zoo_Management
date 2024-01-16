from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from Ticket_zoo import ZoomanagementSystem
from Ticket_zoo3 import Ticket_page
import mysql.connector
from tkinter import Toplevel, Label, Entry, Button, messagebox


class Login_Page:
    def __init__(self, root1):
        self.user_var = StringVar()
        self.password_var = StringVar()

        self.root1 = root1
        self.root1.title("Katraj Zoo")
        self.root1.geometry("1550x800+0+0")
        self.root1.configure(bg="#F1DBBF", relief=FLAT)
        # self.root1.attributes('-fullscreen', True)

        self.background = PhotoImage(file="zoo25.png")
        label1 = Label(self.root1, image=self.background)
        label1.place(x=0, y=0,relheight=1,relwidth=1)



        lbltitle=Label(self.root1,text="WELCOME   TO    ZOO  ",bd=5,relief=FLAT,
                        bg='#A9907E',fg="#F8C4B4",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)
        lbltitle.config(highlightbackground="#420b07")


        DataFrame=LabelFrame(self.root1,bd=10,relief=FLAT,bg="#97DEFF",padx=100,font=("times new roman",15,"bold"),labelanchor="n")
        DataFrame.place(x=150,y=200,width=500,height=360)

        lblID = Label(DataFrame, font=('times new roman', 17, "bold"), 
        text="LOGIN HERE", 
        padx=2, bg="#97DEFF",fg="#3E54AC", anchor='nw', justify='left')
        lblID.place(x=60,y=20)
        
        lblID.config(width=50, height=10)

        self.label_user = Label(DataFrame, text="user:",fg="#3E54AC",bg="#97DEFF",font=("times new roman",13,"bold"))
        self.label_user.place(x=30,y=60)
        self.entry_user = Entry(DataFrame, textvariable=self.user_var,width=27,relief=FLAT)
        self.entry_user.place(x=120,y=60)

        self.label_password = Label(DataFrame, text="Password:",fg="#3E54AC",bg="#97DEFF",font=("times new roman",13,"bold"))
        self.label_password.place(x=30,y=110)
        self.entry_password = Entry(DataFrame,show="*", textvariable=self.password_var,width=27,relief=FLAT)
        self.entry_password.place(x=120,y=110)

        
    
        style = ttk.Style()
        style.configure("TButton", padding=2, relief="flat", backgroundcolor="red", borderwidth=0, bordercolor="",font=("TImes new roman", 12), foreground="#9E4784", focuscolor="#46C2CB", focusthickness=0, highlightthickness=0, highlightcolor="#46C2CB", borderradius=250)
        
        self.btn_signup = ttk.Button(DataFrame, text="Signup", command=self.signup,style="TButton")
        self.btn_signup.place(x=100,y=230)

        self.admin_log = ttk.Button(DataFrame, text="Admin Login", command=self.admin_login,style="TButton")
        self.admin_log.place(x=20,y=180)

        self.user_login = ttk.Button(DataFrame, text="User Login", command=self.User_login,style="TButton")
        self.user_login.place(x=170,y=180)

        self.exit_btn = ttk.Button(DataFrame, text="Exit", command=self.root1.destroy,style="TButton")
        self.exit_btn.place(x=100,y=285)
        

    
    def signup(self):
        # Create a new top-level window for the sign-up dialog
        signup_window = Toplevel(self.root1)
        signup_window.configure(bg="#FDD36A", relief=FLAT)
        signup_window.title("Sign up")
        x = self.root1.winfo_rootx()
        y = self.root1.winfo_rooty()
        offset_x = 280
        offset_y = 240
        signup_window.geometry(f"+{x + offset_x}+{y + offset_y}")

        # Add a label and entry widget for the user
        user_label = Label(signup_window, text="user:",bg="#FDD36A",font=("times new roman",12))
        user_label.grid(row=0, column=0, padx=5, pady=5)
        user_entry = Entry(signup_window,relief=FLAT)
        user_entry.grid(row=0, column=1, padx=5, pady=5)

        # Add a label and entry widget for the password
        password_label = Label(signup_window, text="Password:",bg="#FDD36A",font=("times new roman",12))
        password_label.grid(row=1, column=0, padx=5, pady=5)
        password_entry = Entry(signup_window, show="*",relief=FLAT)
        password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Add a label and entry widget for the confirm password
        confirm_label = Label(signup_window, text="Confirm Password:",bg="#FDD36A",font=("times new roman",12))
        confirm_label.grid(row=2, column=0, padx=5, pady=5)
        confirm_entry = Entry(signup_window, show="*",relief=FLAT)
        confirm_entry.grid(row=2, column=1, padx=5, pady=5)

        # Add a button to submit the sign-up form
        signup_button = ttk.Button(signup_window, text="Sign up", command=lambda: self.process_signup(user_entry.get(), password_entry.get(), confirm_entry.get(), signup_window),style="TButton")
        signup_button.grid(row=3, column=1, padx=5, pady=5)

    def process_signup(self, user, password, confirm_password, signup_window):
        if not user or not password:
            messagebox.showerror("Error", "user and password are required.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="SHA#27bankar7", database="zoo")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO user_data (username, password) VALUES (%s, %s)", (
                user,
                password
            ))
            conn.commit()
            messagebox.showinfo("Signup", "Signup Successful. Please login with your credentials.")
            signup_window.destroy()
            conn.close()


    def admin_login(self):
        user = self.entry_user.get()
        password = self.entry_password.get()
        # user_role = self.combobox_user_role.get()
        if user == "admin" and password == "password":
            self.new_window = Toplevel(self.root1)
            self.app = ZoomanagementSystem(self.new_window)
            self.root1.withdraw()
        else:
            messagebox.showerror("Error ","Wrong Admin Credentials")


    def User_login(self):
        user = self.entry_user.get()
        password = self.entry_password.get()
        # user_role = self.combobox_user_role.get()

        if self.user_var.get() == "" or self.password_var.get() == "":
                messagebox.showerror("Error", "All fields required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="SHA#27bankar7", database="zoo")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM user_data WHERE username = %s AND password = %s", (
                self.user_var.get(),
                self.password_var.get()
            ))
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showinfo("Login", "Login Succcesfull")
                self.new_window = Toplevel(self.root1)
                self.app = Ticket_page(self.new_window)
                self.root1.withdraw()

            else:
                messagebox.showerror("Error", "user and Password not found")
            conn.close()

        # else:
        #     self.label_error.config(text="Invalid user or password")


if __name__ == "__main__":
    root1 = Tk()
    obj = Login_Page(root1)
    root1.mainloop()


