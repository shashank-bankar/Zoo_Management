from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector



from tkinter import messagebox

class EmployeeManagementSystem:
        def __init__(self,root):
                
                self.root=root
                self.root.title("Employee Management System")
                self.root.geometry("1550x800+0+0")
                self.root.configure(bg="#66347F",relief=FLAT)
                
              
                self.Ename_var=StringVar()
                self.Dept_var=StringVar()
                self.cubical_var=StringVar()
                self.salary_var=StringVar()
                self.gender_var=StringVar()
                self.age_var=StringVar()

                lbltitle=Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEM",bd=5,relief=FLAT,
                        bg='#37306B',fg="#D5CEA3",font=("times new roman",50,"bold"),padx=2,pady=4)
                lbltitle.pack(side=TOP,fill=X)
                lbltitle.config(highlightbackground="#420b07")

        
        #DataFrames
                DataFrame = Frame(self.root,bd=15,relief=FLAT,bg="#66347F",padx=20)
                DataFrame.place(x=0,y=100,width=1530,height=400)

                DataFrameLeft=LabelFrame(DataFrame,relief=FLAT,text="Employee Information",bg="#66347F",fg="#DDF7E3",font=("times new roman",17,"bold"),labelanchor="nw")
                DataFrameLeft.place(x=0,y=5,width=800,height=350)

                DataFrameRight=LabelFrame(DataFrame,bd=10,relief=FLAT,bg="#66347F",font=("times new roman",15,"bold"),labelanchor="n")
                DataFrameRight.place(x=500,y=0,width=900,height=400)

                img=Image.open("emp1.jpeg")
                img=img.resize((420,500),Image.LANCZOS)
                self.photoimg=ImageTk.PhotoImage(img)
                b=Button(DataFrameRight,image=self.photoimg,borderwidth=0)
                b.place(x=450,y=0)

                img2=Image.open("emp2.jpeg")
                img2=img2.resize((390,400),Image.LANCZOS)
                self.photoimg2=ImageTk.PhotoImage(img2)
                b2=Button(DataFrameRight,image=self.photoimg2,borderwidth=0)
                b2.place(x=20,y=0)
        #buttonsFrame
                ButtonFrame = Frame(self.root,bd=1.4,relief=RIDGE,padx=300,pady=10,bg="#9E4784")
                ButtonFrame.place(x=0,y=520,width=1530,height=55)
        # Main buttons
                btnAddData =Button(ButtonFrame,command=self.add_data,text="ADD Employee",font=("times new roman",12,"bold"),bg="#159895",fg="white",relief=FLAT)
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
                search_combo["values"]=("ID","EmployeeName","Department")
                search_combo.grid(row=0,column=6)
                search_combo.current(0)
                
                self.searchTxt_var=StringVar()

                txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=14,font=("arial",13,"bold"))
                txtSearch.grid(row=0,column=7) 

                searchBtn =Button(ButtonFrame,command=self.search_data,text="SEARCH",font=("times new roman",12,"bold"),bg="#b2ad81",fg="white",relief=FLAT)
                searchBtn.grid(row=0,column=8)

                showAll =Button(ButtonFrame,command=self.fetch_data,text="SHOW ALL",font=("times new roman",12,"bold"),bg="#c6c190",fg="white",relief=FLAT)
                showAll.grid(row=0,column=9)




                lblName=Label(DataFrameLeft,font=('times new roman',17,"bold"),text="Employee Name",padx=2,bg="#66347F",fg="#DDF7E3")
                lblName.grid(row=2,column=0,sticky=W)


                txtName=Entry(DataFrameLeft,bd=3,textvariable=self.Ename_var,relief=RIDGE,width=30,font=("times new roman",13,"bold"))
                txtName.grid(row=2,column=1)

                lblBreed=Label(DataFrameLeft,font=('times new roman',17,"bold"),text="Department",padx=2,bg="#66347F",fg="#DDF7E3")
                lblBreed.grid(row=3,column=0,sticky=W)
                
                txtBreed=Entry(DataFrameLeft,bd=3,textvariable=self.Dept_var,relief=RIDGE,width=30,font=("times new roman",13,"bold"))
                txtBreed.grid(row=3,column=1)
                
                lblCage=Label(DataFrameLeft,font=('times new roman',17,"bold"),text="Cubical No.",padx=2,bg="#66347F",fg="#DDF7E3")
                lblCage.grid(row=4,column=0,sticky=W)
                
                txtCage=Entry(DataFrameLeft,bd=3,textvariable=self.cubical_var,relief=RIDGE,width=30,font=("times new roman",13,"bold"))
                txtCage.grid(row=4,column=1)
                
                lbltype=Label(DataFrameLeft,font=('times new roman',17,"bold"),text="Salary",padx=2,bg="#66347F",fg="#DDF7E3")
                lbltype.grid(row=5,column=0,sticky=W)

                txtsalary=Entry(DataFrameLeft,bd=3,textvariable=self.salary_var,relief=RIDGE,width=30,font=("times new roman",13,"bold"))
                txtsalary.grid(row=5,column=1)


                lblGender=Label(DataFrameLeft,font=('times new roman',17,"bold"),text="Gender",padx=2,bg="#66347F",fg="#DDF7E3")
                lblGender.grid(row=6,column=0,sticky=W)
                
                Gender_Combo=ttk.Combobox(DataFrameLeft,textvariable=self.gender_var,width=27,font=("times new roman",13,"bold"))
                Gender_Combo["values"]=("MALE","FEMALE")
                Gender_Combo.grid(row=6,column=1)
                Gender_Combo.current(0)

                lblAge=Label(DataFrameLeft,font=('times new roman',17,"bold"),text="Age of Employee",padx=2,bg="#66347F",fg="#DDF7E3")
                lblAge.grid(row=7,column=0,sticky=W)
                
                txtAge=Entry(DataFrameLeft,bd=3,textvariable=self.age_var,relief=RIDGE,width=30,font=("times new roman",13,"bold"))
                txtAge.grid(row=7,column=1)


        # Frame Details
                Framedetails=Frame(self.root,bd=15,relief=FLAT,bg="#D27685")
                Framedetails.place(x=0,y=580,width=1530,height=210)

        # MAin table and Scrollbar
                Table_Frame=Frame(Framedetails,bd=0,relief=FLAT,bg="#675D50")
                Table_Frame.place(x=0,y=1,width=1500,height=180)


                scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
                scroll_y.pack(side=RIGHT,fill=Y)

                

                self.emp_table=ttk.Treeview(Table_Frame,column=("ID","Employee Name","Department","Cubical No.","Salary","Gender","Age"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.config(command=self.emp_table.xview)
                scroll_y.config(command=self.emp_table.yview)
              



                self.emp_table["show"]="headings"

                self.emp_table.heading("ID",text="ID")
                self.emp_table.heading("Employee Name",text="Employee Name")
                self.emp_table.heading("Department",text="Department")
                self.emp_table.heading("Cubical No.",text="Cubical No.")
                self.emp_table.heading("Salary",text="Salary")
                self.emp_table.heading("Gender",text="Gender")
                self.emp_table.heading("Age",text="Age")
                
                self.emp_table.pack(fill=BOTH,expand=1)
                

                self.emp_table.column("ID",width=100)
                self.emp_table.column("Employee Name",width=100)
                self.emp_table.column("Department",width=100)
                self.emp_table.column("Gender",width=100)
                self.emp_table.column("Age",width=100)
                
                self.fetch_data()
                self.emp_table.bind("<ButtonRelease-1>",self.get_cursor)

        # def login(self):
        #         self.root1.withdraw()
        #         self.root.deiconify()

#Main Table
        def add_data(self):

                if self.Ename_var.get()=="" or self.Dept_var.get()=="" or self.cubical_var.get()=="" or self.salary_var.get()=="" or self.gender_var.get()=="" or self.age_var.get()=="":
                        messagebox.showerror("Error","All Fields are Required")
                        return
                
                conn = mysql.connector.connect(host="localhost",username="root",password="9206",database="employee")
                my_cursor = conn.cursor()

                my_cursor.execute("INSERT INTO employee_table (EmployeeName, Department, CubicalNo, Salary, Gender, Age) VALUES (%s, %s, %s, %s, %s, %s)",
                                (self.Ename_var.get(), self.Dept_var.get(), self.cubical_var.get(), self.salary_var.get(), self.gender_var.get(), self.age_var.get()))
                
               
                conn.commit()
                conn.close()
                
               
                self.fetch_data()
                messagebox.showinfo("Success","Data Has been Inserted")


        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="9206",database="employee")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from employee_table")
                row=my_cursor.fetchall()
                if len(row)!=0:
                    self.emp_table.delete(*self.emp_table.get_children())
                    for i in row:
                        self.emp_table.insert("",END,values=i)
                    conn.commit()
                conn.close()

        def get_cursor(self,ev=""):
                cursor_row=self.emp_table.focus()
                content=self.emp_table.item(cursor_row)
                row=content["values"]

                #self.ref_var.set(row[0]),
                self.Ename_var.set(row[1]),
                self.Dept_var.set(row[2]),
                self.cubical_var.set(row[3]),
                self.salary_var.set(row[4]),
                self.gender_var.set(row[5]),
                self.age_var.set(row[6])

        def Update(self):
                if self.Ename_var.get()=="":
                        messagebox.showerror("Error","All fields are Required")
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="9206",database="employee")
                        my_cursor=conn.cursor() 
                        my_cursor.execute("update employee_table set EmployeeName = %s,Department=%s,CubicalNo=%s,Salary=%s,Gender=%s,Age=%s where EmployeeName=%s",(
                
                self.Ename_var.get(),
                self.Dept_var.get(),
                self.cubical_var.get(),
                self.salary_var.get(),
                self.gender_var.get(),
                self.age_var.get(),
                self.Ename_var.get()
                #self.ref_var.get()

                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("success","Employee has been Updated")

        def Delete(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="9206",database="employee")
                my_cursor=conn.cursor()

                sql="delete from employee_table where EmployeeName=%s"
                val=(self.Ename_var.get(),)
                my_cursor.execute(sql,val)

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Delete","Info deleted successfully")
        def Reset(self):
                #self.ref_var.set(" "),
                self.Ename_var.set(" "),
                self.Dept_var.set(" "),
                self.cubical_var.set(" "),
                self.salary_var.set(" "),
                self.gender_var.set(" "),
                self.age_var.set(" "),
                
        def search_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="9206",database="employee")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT * FROM employee_table WHERE " + str(self.search_var.get()) + " LIKE '" + str(self.searchTxt_var.get()) + "%'")

                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.emp_table.delete(*self.emp_table.get_children())
                        for i in rows:
                                self.emp_table.insert("",END,values=i)
                        conn.commit()
                else:
                        messagebox.showerror("Error","Record not Found")
                        self.searchTxt_var.set(" ")
                conn.close()
        def exit(self):
               root.destroy()
             

if __name__ == "__main__":
  
    root = Tk()
    
    obj = EmployeeManagementSystem(root)
    root.mainloop()
