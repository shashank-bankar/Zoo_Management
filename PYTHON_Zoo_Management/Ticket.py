from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import LabelFrame
import mysql.connector
import random
import pytz

from tkcalendar import Calendar
from datetime import datetime


class Ticket_page:
    def _init_(self, root2):
        self.root2 = root2
        self.root2.title("Ticket Booking")
        self.root2.geometry("1550x800+0+0")
        self.root2.configure(bg="#E96479", relief=FLAT)

        lbltitle=Label(self.root2,text="TICKET BOOKING",bd=5,relief=FLAT,
                        bg='#4D455D',fg="#E9E8E8",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)
        lbltitle.config(highlightbackground="#420b07")



        DataFrameLeft=LabelFrame(self.root2,bd=10,relief=FLAT,padx=10,font=("times new roman",15,"bold"),labelanchor="n",bg="#BCCEF8")
        DataFrameLeft.place(x=10,y=100,width=400,height=310)
        
        

        DataFrameRight=LabelFrame(self.root2,bd=10,relief=FLAT,font=("times new roman",15,"bold"),labelanchor="n",bg="#BCCEF8")
        DataFrameRight.place(x=710,y=100,width=800,height=310)

        DownFrame=LabelFrame(self.root2,bd=10,relief=FLAT,font=("times new roman",15,"bold"),labelanchor="n",bg="#E96479")
        DownFrame.place(x=710,y=450,width=800,height=310)

        BottomFrame=LabelFrame(self.root2,bd=10,relief=FLAT,font=("times new roman",15,"bold"),labelanchor="n",bg="#C0DBEA")
        BottomFrame.place(x=10,y=450,width=400,height=310)

        lbl_ticket_info = Label(BottomFrame, font=('times new roman', 17, "bold"), 
        text="\n             * * * Rules: * * *\n \n \n1) Purchase tickets in advance \n2) Check for discounts \n3) Read the fine print \n4) Keep your tickets safe \n5) Follow the rules and guidelines \n6) Enjoy your visit!!!!!", 
        padx=2, bg="#C0DBEA",fg="#A61F69", anchor='nw', justify='left')
        lbl_ticket_info.place(x=0,y=0)
        lbl_ticket_info.pack(fill='both', expand=True)
        lbl_ticket_info.config(width=150, height=150)

        self.tree = ttk.Treeview(DownFrame, columns=("ID", "Name", "Breed", "Cage No.", "Type"))
        self.tree.heading("#0", text="No.")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Breed", text="Breed")
        self.tree.heading("Cage No.", text="Cage No.")
        self.tree.heading("Type", text="Type")
        self.tree.pack()
        self.tree.place(x=125,y=50)

        self.tree.column("#0", width=50)
        self.tree.column("ID",width=50)
        self.tree.column("Name",width=120)
        self.tree.column("Breed",width=170)
        self.tree.column("Cage No.",width=70)
        self.tree.column("Type",width=70)

        img11=Image.open("zoo28.jpeg")
        img11=img11.resize((280,310),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b11=Button(self.root2,image=self.photoimg11,borderwidth=0,relief=FLAT)
        b11.place(x=420,y=100)

        img12=Image.open("zoo21.png")
        img12=img12.resize((380,310),Image.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        b12=Button(self.root2,image=self.photoimg12,borderwidth=0,relief=FLAT)
        b12.place(x=420,y=450)

        lbl_animal_rightnow = Label(DownFrame, font=('times new roman', 17, "bold"), 
        text="* * * ANIMAL INFO * * *", 
        padx=2, bg="#E96479",fg="#FBFFB1", anchor='nw', justify='left')
        lbl_animal_rightnow.place(x=235,y=0)
        lbl_animal_rightnow.config(width=20, height=0)

        lbl_ticket_details = Label(DataFrameRight, font=('times new roman', 17, "bold"), 
        text="* * * YOUR TICKETS DETAILS WILL BE PRINTED HERE * * *", 
        padx=2, bg="#BCCEF8",fg="#10A19D", anchor='nw', justify='left')
        lbl_ticket_details.place(x=40,y=0)
        lbl_ticket_details.config(width=100, height=0)


        self.label_ticket_details = Label(DataFrameRight, font=('times new roman', 17, "bold"),
        padx=2,fg="#A61F69",bg="#BCCEF8", anchor='nw', justify='left')
        self.label_ticket_details.place(x=20,y=60)
        self.label_ticket_details.config(width=50, height=15)


       
        self.conn = mysql.connector.connect(host="localhost", user="root", password="9206", database="zoo")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM animal1")
        rows = self.cursor.fetchall()
        for i, row in enumerate(rows):
            self.tree.insert("", "end", text=str(i+1), values=row)




        self.label = Label(DataFrameLeft, text="Book Your Ticket",bg="#BCCEF8",fg="#9D3C72", font=('times new roman', 15, "bold"))
        self.label.place(x=80,y=25)
    
        self.label_date = Label(DataFrameLeft, text="Date of Visit:",bg="#BCCEF8",fg="#9D3C72", font=('times new roman', 12, "bold"))
        self.label_date.place(x=10,y=60)
        #self.label_date.pack(pady=10)

        self.entry_date = StringVar()
        self.entry_date_field = Entry(DataFrameLeft, textvariable=self.entry_date,width=25)
        self.entry_date_field.place(x=150,y=60)

        self.btn_calendar = ttk.Button(DataFrameLeft, text="Select Date", command=self.select_date,style="TButton")
        self.btn_calendar.place(x=175,y=90)

        self.Noticket_var=StringVar()
        self.label_tickets = Label(DataFrameLeft, text="Number of Tickets:",bg="#BCCEF8",fg="#9D3C72", font=('times new roman', 12, "bold"))
        self.label_tickets.place(x=0,y=140)

        style = ttk.Style()
        style.configure("TButton", padding=2, relief="flat", backgroundcolor="red", borderwidth=0, bordercolor="",font=("TImes new roman", 12), foreground="#9E4784", focuscolor="#46C2CB", focusthickness=0, highlightthickness=0, highlightcolor="#46C2CB", borderradius=200)

        self.combobox_tickets = ttk.Combobox(DataFrameLeft, values=[1, 2, 3, 4, 5,6],textvariable=self.Noticket_var,width=23)
        self.combobox_tickets.place(x=140,y=140)

        self.btn_book_tickets = ttk.Button(DataFrameLeft, text="Book Tickets", command=self.add_data,style="TButton")
        self.btn_book_tickets.place(x=175,y=170)

        self.btn_book_tickets_pdf = ttk.Button(DataFrameRight, text="Print Tickets", command=self.print_ticket_pdf,style="TButton")
        self.btn_book_tickets_pdf.place(x=30,y=250)

        self.btn_exit = ttk.Button(DataFrameRight, text="Exit", command=self.root2.destroy,style="TButton")
        self.btn_exit.place(x=150,y=250)


  

    def select_date(self):
       
        self.calendar_window = Toplevel(self.root2)
        self.calendar_window.geometry("+{}+{}".format(420, 100))
      
        timezone = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(timezone)
        current_date = current_time.date()
        
       
        self.calendar = Calendar(self.calendar_window, selectmode="day", year=current_date.year, 
                                  month=current_date.month, day=current_date.day, 
                                  date_format='y-mm-dd HH:MM:SS')
        self.calendar.pack(padx=20, pady=10)

       
        self.btn_confirm_date = ttk.Button(self.calendar_window, text="Confirm Date", command=self.confirm_date,style="TButton")
        self.btn_confirm_date.pack(pady=10)
    
    def confirm_date(self):
        # get the selected date and time in the Asia/Kolkata timezone
        selected_date = self.calendar.selection_get()
        timezone = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(timezone)
        
        selected_date = datetime(
            year=selected_date.year,
            month=selected_date.month,
            day=selected_date.day,
            hour=current_time.hour,
            minute=current_time.minute,
            second=current_time.second,
            tzinfo=timezone
        )
        
        self.entry_date.set(selected_date.strftime("%Y-%m-%d %H:%M:%S"))
        self.calendar_window.destroy()

                    
    def add_data(self):

        if self.entry_date.get()=="" or self.combobox_tickets.get()=="" :
                messagebox.showerror("Error","All Fields are Required")
                return
        
        conn = mysql.connector.connect(host="localhost",username="root",password="9206",database="zoo")
        my_cursor = conn.cursor()

        my_cursor.execute("INSERT INTO tickets (Date, NoTickets) VALUES (%s, %s)",
                        (self.entry_date.get(), self.Noticket_var.get()))
        
        
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success","Ticket Booked Successfully !!!")
        self.print_ticket()





    
    def calculate_ticket_price(self,num_tickets):
        ticket_price = 10
        total_price = num_tickets * ticket_price
        return total_price

    def print_ticket(self):
        self.ticket_no = random.randint(1, 100)
        date = datetime.strptime(self.entry_date.get(), '%Y-%m-%d %H:%M:%S')
        self.date_str = date.strftime('%A, %B %d, %Y booked at %I:%M %p')
        self.num_tickets = int(self.combobox_tickets.get())

        self.perticket =10

        self.ticket_price = self.calculate_ticket_price(self.num_tickets)

        ticket_details = f"Ticket_No.:      {self.ticket_no}\nDate of Visit:    {self.date_str}\nNo.of Tickets:   {self.num_tickets}\nPrice per Ticket: ₹{self.perticket}\nPrice of Ticket: ₹{self.ticket_price}"

        self.label_ticket_details.configure(text="Your Ticket Details:\n-----------------------------------------\n"+ticket_details)

    def print_ticket_pdf(self):
        # Set up canvas
        c = canvas.Canvas("ticket.pdf", pagesize=letter)
            

        # Draw ticket content
        c.setFont("Helvetica", 16)
        c.drawString(200, 750,"Zoo management System")
        c.drawString(100, 700, "Ticket ID:  " + str(self.ticket_no))
        c.drawString(100, 650, "------------------------------------------------------------------------------------")
        c.drawString(100, 600, "Date of Visit:  " + self.date_str)
        c.drawString(100, 550, "Ticket Price: Rs.  " + str(self.ticket_price)+"/-")
        c.drawString(100, 500, "No. of Tickets:  " + str(self.num_tickets))

    # Save PDF file
        c.save()
        messagebox.showinfo("Success","Ticket Downloaded Successfully!!")


       

if _name_ == "_main_":
    root2 = Tk()
    obj = Ticket_page(root2)
    root2.mainloop()