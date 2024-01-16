from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from pydub import AudioSegment
from pydub.playback import play

from tkinter import messagebox

class ZoomanagementSystem:
        def __init__(self,root):
                self.root=root
                self.root.title("Zoo Management System")
                self.root.geometry("1550x800+0+0")
                self.root.configure(bg="#F3DEBA",relief=FLAT)
                
           
            # main variables
              
                self.Aname_var=StringVar()
                self.breed_var=StringVar()
                self.cageno_var=StringVar()
                self.type_var=StringVar()
                self.gender_var=StringVar()
                self.age_var=StringVar()

                lbltitle=Label(self.root,text="ZOO MANAGEMENT SYSTEM",bd=5,relief=FLAT,
                        bg='#A9907E',fg="#E9E8E8",font=("times new roman",50,"bold"),padx=2,pady=4)
                lbltitle.pack(side=TOP,fill=X)
                lbltitle.config(highlightbackground="#420b07")

        
        #DataFrames
                DataFrame = Frame(self.root,bd=15,relief=FLAT,bg="#F3DEBA",padx=20)
                DataFrame.place(x=0,y=100,width=1530,height=400)

                DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=FLAT,padx=140,text="Animal Information",bg="#F3DEBA",font=("times new roman",15,"bold"),labelanchor="n")
                DataFrameLeft.place(x=0,y=5,width=800,height=350)

                DataFrameRight=LabelFrame(DataFrame,bd=10,relief=FLAT,padx=100,bg="#F3DEBA",font=("times new roman",15,"bold"),labelanchor="n")
                DataFrameRight.place(x=810,y=0,width=800,height=400)

        # Images        

                img1=Image.open("zoo11.png")
                img1=img1.resize((250,300),Image.LANCZOS)
                self.photoimg1=ImageTk.PhotoImage(img1)
                b1=Button(DataFrame,image=self.photoimg1,borderwidth=0,relief=FLAT,bd=0)
                b1.config(highlightbackground="#95C690")
                b1.place(x=640,y=3)

                # self.audio_file = AudioSegment.from_file("zoo12_audio.mp3")
                # def play_audio(self):
                #         play(self.audio_file)
                img2=Image.open("zoo12.png")
                img2=img2.resize((130,90),Image.LANCZOS)
                self.photoimg2=ImageTk.PhotoImage(img2)
                b2=Button(self.root,image=self.photoimg2,borderwidth=0,relief=FLAT,bd=0)
                b2.config(highlightbackground="#95C690")
                b2.place(x=70,y=3)
               
               

                img3=Image.open("tiger1.jpg")
                img3=img3.resize((120,90),Image.LANCZOS)
                self.photoimg3=ImageTk.PhotoImage(img3)
                b3=Button(self.root,image=self.photoimg3,borderwidth=0)
                b3.place(x=120,y=427)

                img4=Image.open("jiraffe.jpg")
                img4=img4.resize((120,90),Image.LANCZOS)
                self.photoimg4=ImageTk.PhotoImage(img4)
                b4=Button(self.root,image=self.photoimg4,borderwidth=0)
                b4.place(x=270,y=427)


                img6=Image.open("chimps.jpg")
                img6=img6.resize((120,90),Image.LANCZOS)
                self.photoimg6=ImageTk.PhotoImage(img6)
                b6=Button(self.root,image=self.photoimg6,borderwidth=0)
                b6.place(x=420,y=427)

                img7=Image.open("chitah.jpg")
                img7=img7.resize((120,90),Image.LANCZOS)
                self.photoimg7=ImageTk.PhotoImage(img7)
                b7=Button(self.root,image=self.photoimg7,borderwidth=0)
                b7.place(x=580,y=427)

                img8=Image.open("eagle.jpg")
                img8=img8.resize((120,90),Image.LANCZOS)
                self.photoimg8=ImageTk.PhotoImage(img8)
                b8=Button(self.root,image=self.photoimg8,borderwidth=0)
                b8.place(x=730,y=427)

               
                img10=Image.open("meerkat.jpg")
                img10=img10.resize((120,90),Image.LANCZOS)
                self.photoimg10=ImageTk.PhotoImage(img10)
                b10=Button(self.root,image=self.photoimg10,borderwidth=0)
                b10.place(x=890,y=427)

                img11=Image.open("panda.jpg")
                img11=img11.resize((120,90),Image.LANCZOS)
                self.photoimg11=ImageTk.PhotoImage(img11)
                b11=Button(self.root,image=self.photoimg11,borderwidth=0)
                b11.place(x=1050,y=427)

                img12=Image.open("elephant.jpg")
                img12=img12.resize((120,90),Image.LANCZOS)
                self.photoimg12=ImageTk.PhotoImage(img12)
                b12=Button(self.root,image=self.photoimg12,borderwidth=0)
                b12.place(x=1200,y=427)
        #buttonsFrame
                ButtonFrame = Frame(self.root,bd=1.4,relief=RIDGE,padx=300,pady=10,bg="#ABC4AA")
                ButtonFrame.place(x=0,y=520,width=1530,height=55)
        # Main buttons
                btnAddData =Button(ButtonFrame,command=self.add_data,text="ADD ANIMAL",font=("times new roman",12,"bold"),bg="#159895",fg="white",relief=FLAT)
                btnAddData.grid(row=0,column=0)
                
                btnUPdateAni =Button(ButtonFrame,command=self.Update,text="UPDATE",font=("times new roman",12,"bold"),bg="#4f4d39",fg="white",relief=FLAT)
                btnUPdateAni.grid(row=0,column=1)

                btnDeleteAni =Button(ButtonFrame,command=self.Delete,text="DELETE",font=("times new roman",12,"bold"),bg="#E74646",fg="white",relief=FLAT)
                btnDeleteAni.grid(row=0,column=2)

                btnRestAni =Button(ButtonFrame,command=self.Reset,text="RESET",font=("times new roman",12,"bold"),bg="#767356",fg="white",relief=FLAT)
                btnRestAni.grid(row=0,column=3)

                btnExit =Button(ButtonFrame,command=root.destroy,text="EXIT",font=("times new roman",12,"bold"),bg="#8a8764",fg="white",relief=FLAT)
                btnExit.grid(row=0,column=4)
        #SEARCH BY
                lblsearch=Label(ButtonFrame,font=('times new roman',17,"bold"),text="Search By",padx=2,bg="#F3DEBA",fg="white",relief=FLAT)
                lblsearch.grid(row=0,column=5,sticky=W)

                #variable
                self.search_var=StringVar()

                search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=14,font=("arial",13,"bold"))
                search_combo["values"]=("ID","AnimalName","Breed")
                search_combo.grid(row=0,column=6)
                search_combo.current(0)
                
                self.searchTxt_var=StringVar()

                txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=14,font=("arial",13,"bold"))
                txtSearch.grid(row=0,column=7) 

                searchBtn =Button(ButtonFrame,command=self.search_data,text="SEARCH",font=("times new roman",12,"bold"),bg="#b2ad81",fg="white",relief=FLAT)
                searchBtn.grid(row=0,column=8)

                showAll =Button(ButtonFrame,command=self.fetch_data,text="SHOW ALL",font=("times new roman",12,"bold"),bg="#c6c190",fg="white",relief=FLAT)
                showAll.grid(row=0,column=9)

        # label And Entry
                lblID = Label(DataFrameRight, font=('times new roman', 17, "bold"), 
                text="Rules: \n \n1) Respect the animals \n2) Stay on designated paths and areas \n3) Do not feed the animals \n4) Do not litter \n5) Follow the rules and guidelines \n6) Do not climb fences or enter restricted areas \n7) Do not disturb or touch the exhibits \n\n ENJOY AND VISIT AGAIN !!!!", 
                padx=2, bg="#F3DEBA",fg="#A61F69", anchor='nw', justify='left')
                lblID.place(x=0,y=0)
                lblID.pack(fill='both', expand=True)
                lblID.config(width=150, height=150)



                lblName=Label(DataFrameLeft,font=('times new roman',17,"bold"),text="Animal Name",padx=2,bg="#F3DEBA")
                lblName.grid(row=2,column=0,sticky=W)


                txtName=Entry(DataFrameLeft,bd=3,textvariable=self.Aname_var,relief=RIDGE,width=30,font=("times new roman",13,"bold"))
                txtName.grid(row=2,column=1)

                lblBreed=Label(DataFrameLeft,font=('times new roman',17,"bold"),text="Breed",padx=2,bg="#F3DEBA")
                lblBreed.grid(row=3,column=0,sticky=W)
                
                txtBreed=Entry(DataFrameLeft,bd=3,textvariable=self.breed_var,relief=RIDGE,width=30,font=("times new roman",13,"bold"))
                txtBreed.grid(row=3,column=1)
                
                lblCage=Label(DataFrameLeft,font=('times new roman',17,"bold"),text="Cage No.",padx=2,bg="#F3DEBA")
                lblCage.grid(row=4,column=0,sticky=W)
                
                txtCage=Entry(DataFrameLeft,bd=3,textvariable=self.cageno_var,relief=RIDGE,width=30,font=("times new roman",13,"bold"))
                txtCage.grid(row=4,column=1)
                
                lbltype=Label(DataFrameLeft,font=('times new roman',17,"bold"),text="Type of Animal",padx=2,bg="#F3DEBA")
                lbltype.grid(row=5,column=0,sticky=W)

                Type_Combo=ttk.Combobox(DataFrameLeft,textvariable=self.type_var,width=27,font=("times new roman",13,"bold"))
                Type_Combo["values"]=("LAND","WATER","SKY")
                Type_Combo.grid(row=5,column=1)
                Type_Combo.current(0)

                lblGender=Label(DataFrameLeft,font=('times new roman',17,"bold"),text="Gender of Animal",padx=2,bg="#F3DEBA")
                lblGender.grid(row=6,column=0,sticky=W)
                
                Gender_Combo=ttk.Combobox(DataFrameLeft,textvariable=self.gender_var,width=27,font=("times new roman",13,"bold"))
                Gender_Combo["values"]=("MALE","FEMALE")
                Gender_Combo.grid(row=6,column=1)
                Gender_Combo.current(0)

                lblAge=Label(DataFrameLeft,font=('times new roman',17,"bold"),text="Age of Animal",padx=2,bg="#F3DEBA")
                lblAge.grid(row=7,column=0,sticky=W)
                
                txtAge=Entry(DataFrameLeft,bd=3,textvariable=self.age_var,relief=RIDGE,width=30,font=("times new roman",13,"bold"))
                txtAge.grid(row=7,column=1)


        # Frame Details
                Framedetails=Frame(self.root,bd=15,relief=FLAT,bg="#675D50")
                Framedetails.place(x=0,y=580,width=1530,height=210)

        # MAin table and Scrollbar
                Table_Frame=Frame(Framedetails,bd=0,relief=FLAT,bg="#675D50")
                Table_Frame.place(x=0,y=1,width=1500,height=180)


                scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
                scroll_y.pack(side=RIGHT,fill=Y)

                

                self.zoo_table=ttk.Treeview(Table_Frame,column=("ID","AnimalName","Breed","Cage","Type","Gender","Age"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.config(command=self.zoo_table.xview)
                scroll_y.config(command=self.zoo_table.yview)
               



                self.zoo_table["show"]="headings"

                self.zoo_table.heading("ID",text="ID")
                self.zoo_table.heading("AnimalName",text="Animal Name")
                self.zoo_table.heading("Breed",text="Breed")
                self.zoo_table.heading("Cage",text="Cage")
                self.zoo_table.heading("Type",text="Type")
                self.zoo_table.heading("Gender",text="Gender")
                self.zoo_table.heading("Age",text="Age")
                
                self.zoo_table.pack(fill=BOTH,expand=1)
                

                self.zoo_table.column("ID",width=100)
                self.zoo_table.column("AnimalName",width=100)
                self.zoo_table.column("Breed",width=100)
                self.zoo_table.column("Cage",width=100)
                self.zoo_table.column("Type",width=100)
                self.zoo_table.column("Gender",width=100)
                self.zoo_table.column("Age",width=100)
                
                self.fetch_data()
                self.zoo_table.bind("<ButtonRelease-1>",self.get_cursor)



#Main Table
        def add_data(self):

                if self.Aname_var.get()=="" or self.breed_var.get()=="" or self.cageno_var.get()=="" or self.type_var.get()=="" or self.gender_var.get()=="" or self.age_var.get()=="":
                        messagebox.showerror("Error","All Fields are Required")
                        return
                
                conn = mysql.connector.connect(host="localhost",username="root",password="SHA#27bankar7",database="zoo")
                my_cursor = conn.cursor()

                my_cursor.execute("INSERT INTO animal1 (AnimalName, Breed, Cage, Type, Gender, Age) VALUES (%s, %s, %s, %s, %s, %s)",
                                (self.Aname_var.get(), self.breed_var.get(), self.cageno_var.get(), self.type_var.get(), self.gender_var.get(), self.age_var.get()))
                
               
                conn.commit()
                conn.close()
                
               
                self.fetch_data()
                messagebox.showinfo("Success","Data Has been Inserted")


        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="SHA#27bankar7",database="zoo")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from animal1")
                row=my_cursor.fetchall()
                if len(row)!=0:
                    self.zoo_table.delete(*self.zoo_table.get_children())
                    for i in row:
                        self.zoo_table.insert("",END,values=i)
                    conn.commit()
                conn.close()

        def get_cursor(self,ev=""):
                cursor_row=self.zoo_table.focus()
                content=self.zoo_table.item(cursor_row)
                row=content["values"]

                #self.ref_var.set(row[0]),
                self.Aname_var.set(row[1]),
                self.breed_var.set(row[2]),
                self.cageno_var.set(row[3]),
                self.type_var.set(row[4]),
                self.gender_var.set(row[5]),
                self.age_var.set(row[6])

        def Update(self):
                if self.Aname_var.get()=="":
                        messagebox.showerror("Error","All fields are Required")
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="SHA#27bankar7",database="zoo")
                        my_cursor=conn.cursor() 
                        my_cursor.execute("update animal1 set AnimalName = %s,Breed=%s,Cage=%s,Type=%s,Gender=%s,Age=%s where AnimalName=%s",(
                
                self.Aname_var.get(),
                self.breed_var.get(),
                self.cageno_var.get(),
                self.type_var.get(),
                self.gender_var.get(),
                self.age_var.get(),
                self.Aname_var.get()
                #self.ref_var.get()

                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("success","Animal has been Updated")

        def Delete(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="SHA#27bankar7",database="zoo")
                my_cursor=conn.cursor()

                sql="delete from animal1 where AnimalName=%s"
                val=(self.Aname_var.get(),)
                my_cursor.execute(sql,val)

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Delete","Info deleted successfully")
        def Reset(self):
                #self.ref_var.set(" "),
                self.Aname_var.set(" "),
                self.breed_var.set(" "),
                self.cageno_var.set(" "),
                #self.type_var.set(" "),
                #self.gender_var.set(" "),
                self.age_var.set(" "),
                
        def search_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="SHA#27bankar7",database="zoo")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT * FROM animal1 WHERE " + str(self.search_var.get()) + " LIKE '" + str(self.searchTxt_var.get()) + "%'")

                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.zoo_table.delete(*self.zoo_table.get_children())
                        for i in rows:
                                self.zoo_table.insert("",END,values=i)
                        conn.commit()
                else:
                        messagebox.showerror("Error","Record not Found")
                        self.searchTxt_var.set(" ")
                conn.close()

if __name__ == "__main__":
        root = Tk()
        obj = ZoomanagementSystem(root)
        root.mainloop()
