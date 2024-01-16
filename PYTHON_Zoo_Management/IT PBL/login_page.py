from tkinter import *
from PIL import Image,ImageTk
from tkinter import Toplevel, Label, Entry, Button,messagebox
from mini_project import RestaurantManagementSystem

class Login:
    def __init__(self, home_root1):
        self.home_root1 = home_root1
        self.home_root1.title("Login PAGE")
        self.home_root1.geometry("1440x1080+0+0")
        self.home_root1.maxsize(1440, 1080)
        self.home_root1.minsize(1440, 1080)

        self.btn_login = Button(self.home_root1, text="LOGIN", command=self.login)
        self.btn_login.pack(pady=20)


    def login(self):
       
        #self.home_root.deiconify()
        self.new_window = Toplevel(self.home_root1)
        self.app =RestaurantManagementSystem(self.new_window)
        self.home_root1.withdraw()
        #self.home_root1.withdraw()

if __name__=="__main__":
    home_root1=Tk()
    obj=Login(home_root1)
    home_root1.mainloop()