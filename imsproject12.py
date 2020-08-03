from tkinter import *
import mysql.connector as msc
import datetime
from PIL import  ImageTk, Image
from tkinter import messagebox


#ADD STUDENT

def m1():

    def addstu():
        admno=t1.get()
        sname=t2.get()
        cls=t3.get()
        sec=t4.get()
        fn=t5.get()
        mn=t6.get()
        phn=t7.get()
        dob=t8.get()

        con=msc.connect(host="localhost",user="root",password="sujay",database="ims")
        query="insert into students values({},'{}',{},'{}','{}','{}','{}','{}')".format(admno,sname,cls,sec,fn,mn,phn,dob)
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        con.close()
        messagebox.showinfo("Success","Student details have been saved successfully") 

        t1.delete(0,'end')
        t2.delete(0,'end')
        t3.delete(0,'end')
        t4.delete(0,'end')
        t5.delete(0,'end')
        t6.delete(0,'end')
        t7.delete(0,'end')
        t8.delete(0,'end')




    stu=Tk()
    stu.geometry("550x550")
    stu.config(background="black")
    stu.title("Add Student")

    l1=Label(stu,text="FILL DETAILS TO ADD STUDENT")
    l1.config(font=("courier",16),bg="yellow")
    l1.place(x=90,y=10)

    l2=Label(stu,text="Admission No.-->",bg="green",font=("comic sans ms",14))
    l2.place(x=40,y=70)
    l3=Label(stu,text="Student Name-->",bg="green",font=("comic sans ms",14))
    l3.place(x=40,y=120)
    l4=Label(stu,text="Class-->",bg="green",font=("comic sans ms",14))
    l4.place(x=40,y=170)
    l5=Label(stu,text="Section-->",bg="green",font=("comic sans ms",14))
    l5.place(x=40,y=220)
    l6=Label(stu,text="Fathers Name-->",bg="green",font=("comic sans ms",14))
    l6.place(x=40,y=270)
    l7=Label(stu,text="Mothers Name-->",bg="green",font=("comic sans ms",14))
    l7.place(x=40,y=320)
    l8=Label(stu,text="Phone No.-->",bg="green",font=("comic sans ms",14))
    l8.place(x=40,y=370)
    l9=Label(stu,text="Dob-->",bg="green",font=("comic sans ms",14))
    l9.place(x=40,y=420)
    

    t1=Entry(stu,width=40)
    t1.place(x=230,y=70)
    t2=Entry(stu,width=40)
    t2.place(x=230,y=120)
    t3=Entry(stu,width=40)
    t3.place(x=230,y=170)
    t4=Entry(stu,width=40)
    t4.place(x=230,y=220)
    t5=Entry(stu,width=40)
    t5.place(x=230,y=270)
    t6=Entry(stu,width=40)
    t6.place(x=230,y=320)
    t7=Entry(stu,width=40)
    t7.place(x=230,y=370)
    t8=Entry(stu,width=40)
    t8.place(x=230,y=420)


    b1=Button(stu,text="ADD",width=10,height=1,command=addstu,bg="blue",fg="white",font=(7))
    b1.place(x=400,y=470)

    stu.mainloop()
    
#DELETE STUDENT

def m2():
    
    def remstu():
        admno=t1.get()
        sname=t2.get()
        cls=t3.get()
        
        con=msc.connect(host="localhost",user="root",password="sujay",database="ims")
        query="delete from students where admno={} and sname='{}' and cls={}".format(admno,sname,cls)
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        con.close()
        messagebox.showinfo("Success","Student details have been removed successfully")
        t1.delete(0,'end')
        t2.delete(0,'end')
        t3.delete(0,'end')

    stu=Tk()
    stu.geometry("700x400")
    stu.config(background="black")
    l1=Label(stu,text="FILL DETAILS AND CLICK REMOVE TO REMOVE STUDENT")
    l1.config(font=("courier",18),bg="yellow")
    l1.place(x=25,y=40)
    l2=Label(stu,text="Admission No.-->",bg="green",font=("comic sans ms",14))
    l2.place(x=120,y=110)
    l3=Label(stu,text="Student Name-->",bg="green",font=("comic sans ms",14))
    l3.place(x=120,y=160)
    l4=Label(stu,text="Class-->",bg="green",font=("comic sans ms",14))
    l4.place(x=120,y=210)

    t1=Entry(stu,width=40)
    t1.place(x=320,y=110)
    t2=Entry(stu,width=40)
    t2.place(x=320,y=160)
    t3=Entry(stu,width=40)
    t3.place(x=320,y=210)

    b1=Button(stu,text="REMOVE",width=12,height=2,command=remstu,bg="blue",fg="white",font=(7))
    b1.place(x=300,y=300)

    stu.mainloop()

#VIEW STUDENT DETAIL   

   
def m3():
    
    def viewstu():
        admno=t1.get()
        
        con=msc.connect(host="localhost",user="root",password="sujay",database="ims")
        query="select * from students where admno={}".format(admno)
        cur=con.cursor()
        cur.execute(query)
        records=cur.fetchall()
        
        if len(records)==0:
            messagebox.showinfo("Sorry","no student available of admission no. {}".format(admno))
        else:
            row=records[0]
            t2.delete(0,'end')
            t3.delete(0,'end')
            t4.delete(0,'end')
            t5.delete(0,'end')
            t6.delete(0,'end')
            t7.delete(0,'end')
            t8.delete(0,'end')

            t2.insert(0,row[1])
            t3.insert(0,row[2])
            t4.insert(0,row[3])
            t5.insert(0,row[4])
            t6.insert(0,row[5])
            t7.insert(0,row[6])
            t8.insert(0,row[7])
        con.close()
        
    stu=Tk()
    stu.geometry("700x650")
    stu.config(background="black")
    l1=Label(stu,text="FILL ADMISSION NO. TO GET DETAILS OF STUDENT")
    l1.config(font=("courier",16),bg="yellow")
    l1.place(x=70,y=10)
    l2=Label(stu,text="Admission No.-->",bg="green",font=("comic sans ms",14))
    l2.place(x=100,y=70)
    l3=Label(stu,text="Student Name-->",bg="green",font=("comic sans ms",14))
    l3.place(x=50,y=220)
    l4=Label(stu,text="Class-->",bg="green",font=("comic sans ms",14))
    l4.place(x=50,y=270)
    l5=Label(stu,text="Section>",bg="green",font=("comic sans ms",14))
    l5.place(x=50,y=320)
    l6=Label(stu,text="Fathers Name-->",bg="green",font=("comic sans ms",14))
    l6.place(x=50,y=370)
    l7=Label(stu,text="Mothers Name-->",bg="green",font=("comic sans ms",14))
    l7.place(x=50,y=420)
    l8=Label(stu,text="Phone No-->",bg="green",font=("comic sans ms",14))
    l8.place(x=50,y=470)
    l9=Label(stu,text="Dob-->",bg="green",font=("comic sans ms",14))
    l9.place(x=50,y=520)

    l10=Label(stu,text="---------------DETAILS---------------",bg="black",fg="white",font=("courier",16))
    l10.place(x=100,y=150)

    t1=Entry(stu,width=40)
    t1.place(x=300,y=75)
    t2=Entry(stu,width=40)
    t2.place(x=240,y=220)
    t3=Entry(stu,width=40)
    t3.place(x=240,y=270)
    t4=Entry(stu,width=40)
    t4.place(x=240,y=320)
    t5=Entry(stu,width=40)
    t5.place(x=240,y=370)
    t6=Entry(stu,width=40)
    t6.place(x=240,y=420)
    t7=Entry(stu,width=40)
    t7.place(x=240,y=470)
    t8=Entry(stu,width=40)
    t8.place(x=240,y=520)

    b1=Button(stu,text="SHOW",width=12,height=1,command=viewstu,bg="blue",fg="white",font=(7))
    b1.place(x=500,y=570)

    stu.mainloop()


#ADD TEACHER INFO
    

def m4():    
    
    def  addtch():
        empno=t1.get()
        ename=t2.get()
        exp=t3.get()
        qualification=t4.get()
        subject=t5.get()
        salary=t6.get()
        pno=t7.get()
        

        con=msc.connect(host="localhost",user="root",password="sujay",database="ims")
        query="insert into teachers values({},'{}','{}','{}','{}',{},'{}')".format(empno,ename,exp,qualification,subject,salary,pno)
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        con.close()
        messagebox.showinfo("Success","Teacher details have been saved successfully")

        
    tch=Tk()
    tch.geometry("500x500")
    tch.config(background="black")
    tch.title("Add Teacher Information")

    l1=Label(tch,text="FILL DETAILS TO ADD TEACHER")
    l1.config(font=("courier",16),bg="yellow")
    l1.place(x=90,y=10)

    l2=Label(tch,text="Employment No-->",bg="green",font=("comic sans ms",14))
    l2.place(x=40,y=70)
    l3=Label(tch,text="Teachers Name-->",bg="green",font=("comic sans ms",14))
    l3.place(x=40,y=120)
    l4=Label(tch,text="Experience(in yrs)-->",bg="green",font=("comic sans ms",14))
    l4.place(x=40,y=170)
    l5=Label(tch,text="Qualifications-->",bg="green",font=("comic sans ms",14))
    l5.place(x=40,y=220)
    l6=Label(tch,text="Subject Teaching-->",bg="green",font=("comic sans ms",14))
    l6.place(x=40,y=270)
    l7=Label(tch,text="Salary-->",bg="green",font=("comic sans ms",14))
    l7.place(x=40,y=320)
    l8=Label(tch,text="Phone No.-->",bg="green",font=("comic sans ms",14))
    l8.place(x=40,y=370)

    t1=Entry(tch,width=40)
    t1.place(x=230,y=70)
    t2=Entry(tch,width=40)
    t2.place(x=230,y=120)
    t3=Entry(tch,width=40)
    t3.place(x=230,y=170)
    t4=Entry(tch,width=40)
    t4.place(x=230,y=220)
    t5=Entry(tch,width=40)
    t5.place(x=230,y=270)
    t6=Entry(tch,width=40)
    t6.place(x=230,y=320)
    t7=Entry(tch,width=40)
    t7.place(x=230,y=370)

    b1=Button(tch,text="ADD",width=10,height=1,command=addtch,bg="blue",fg="white",font=(7))
    b1.place(x=370,y=430)

    tch.mainloop()
    
    
#VIEW TEACHER DETAIL
    
def m5():
    
    def viewtch():
        empno=t1.get()
        
        con=msc.connect(host="localhost",user="root",password="sujay",database="ims")
        query="select * from teachers where empno={}".format(empno)
        cur=con.cursor()
        cur.execute(query)
        records=cur.fetchall()
        
        if len(records)==0:
            messagebox.showinfo("Sorry","no teacher available of employment no. {}".format(admno))
        else:
            row=records[0]
            t2.delete(0,'end')
            t3.delete(0,'end')
            t4.delete(0,'end')
            t5.delete(0,'end')
            t6.delete(0,'end')
            t7.delete(0,'end')
            

            t2.insert(0,row[1])
            t3.insert(0,row[2])
            t4.insert(0,row[3])
            t5.insert(0,row[4])
            t6.insert(0,row[5])
            t7.insert(0,row[6])
            
        con.close()
        
    tch=Tk()
    tch.geometry("700x650")
    tch.config(background="black")
    l1=Label(tch,text="FILL EMPLOYMENT NO. TO GET DETAILS OF TEACHER")
    l1.config(font=("courier",16),bg="yellow")
    l1.place(x=70,y=10)
    l2=Label(tch,text="Employment No.-->",bg="green",font=("comic sans ms",14))
    l2.place(x=100,y=70)
    l3=Label(tch,text="Teachers Name-->",bg="green",font=("comic sans ms",14))
    l3.place(x=50,y=220)
    l4=Label(tch,text="Experience-->",bg="green",font=("comic sans ms",14))
    l4.place(x=50,y=270)
    l5=Label(tch,text="Qualification-->",bg="green",font=("comic sans ms",14))
    l5.place(x=50,y=320)
    l6=Label(tch,text="Subject-->",bg="green",font=("comic sans ms",14))
    l6.place(x=50,y=370)
    l7=Label(tch,text="Salary-->",bg="green",font=("comic sans ms",14))
    l7.place(x=50,y=420)
    l8=Label(tch,text="Phone No-->",bg="green",font=("comic sans ms",14))
    l8.place(x=50,y=470)
    

    l9=Label(tch,text="---------------DETAILS---------------",bg="black",fg="white",font=("courier",16))
    l9.place(x=100,y=150)

    t1=Entry(tch,width=40)
    t1.place(x=300,y=75)
    t2=Entry(tch,width=40)
    t2.place(x=240,y=220)
    t3=Entry(tch,width=40)
    t3.place(x=240,y=270)
    t4=Entry(tch,width=40)
    t4.place(x=240,y=320)
    t5=Entry(tch,width=40)
    t5.place(x=240,y=370)
    t6=Entry(tch,width=40)
    t6.place(x=240,y=420)
    t7=Entry(tch,width=40)
    t7.place(x=240,y=470)
    

    b1=Button(tch,text="SHOW",width=12,height=1,command=viewtch,bg="blue",fg="white",font=(7))
    b1.place(x=500,y=570)

    tch.mainloop()
    

#REMOVE TEACHER

def m6():

    def remtch():
        empno=t1.get()
        ename=t2.get()
        
        con=msc.connect(host="localhost",user="root",password="sujay",database="ims")
        query="delete from teachers where empno={} and ename='{}' ".format(empno,ename)
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        con.close()
        messagebox.showinfo("Success","Teachers details have been removed successfully")
        t1.delete(0,'end')
        t2.delete(0,'end')

    tch=Tk()
    tch.geometry("700x400")
    tch.config(background="black")
    l1=Label(tch,text="FILL DETAILS AND CLICK REMOVE TO REMOVE TEACHER")
    l1.config(font=("courier",18),bg="yellow")
    l1.place(x=25,y=40)
    l2=Label(tch,text="Employment No.-->",bg="green",font=("comic sans ms",14))
    l2.place(x=120,y=110)
    l3=Label(tch,text="Teachers Name-->",bg="green",font=("comic sans ms",14))
    l3.place(x=120,y=160)
    

    t1=Entry(tch,width=40)
    t1.place(x=320,y=110)
    t2=Entry(tch,width=40)
    t2.place(x=320,y=160)

    b1=Button(tch,text="REMOVE",width=12,height=2,command=remtch,bg="blue",fg="white",font=(7))
    b1.place(x=300,y=300)

    tch.mainloop()
    
#ADD
    
def m7():

    def remfee():
        
        con=msc.connect(host="localhost",user="root",password="sujay",database="ims")
        query="select(select totalfee from fees)-(select feepaid from fees)"
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        con.close()
        
    
        
        
    def  addfee():
        
        Class=t1.get()
        section=t2.get()
        totalfee=t3.get()
        feepaid=t4.get()
        admno=t5.get()
        

        con=msc.connect(host="localhost",user="root",password="sujay",database="ims")
        query="insert into fees values({},'{}',{},'{}',{},{},{})".format(Class,section,totalfee,feepaid,admno)
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        con.close()
        messagebox.showinfo("Success","Fees details have been added successfully")
        t1.delete(0,'end')
        t2.delete(0,'end')
        t3.delete(0,'end')
        t4.delete(0,'end')
        t5.delete(0,'end')
        

    fee=Tk()
    fee.geometry("1200x500")
    fee.config(background="black")
    fee.title("Add Fee")

    l1=Label(fee,text="FILL FEE DETAILS")
    l1.config(font=("courier",20),bg="yellow")
    l1.place(x=50,y=20)

    l2=Label(fee,text="Class.-->",bg="green",font=("comic sans ms",14))
    l2.place(x=60,y=130)
    l3=Label(fee,text="Section-->",bg="green",font=("comic sans ms",14))
    l3.place(x=60,y=180)
    l4=Label(fee,text="Total Fee-->",bg="green",font=("comic sans ms",14))
    l4.place(x=60,y=230)
    l6=Label(fee,text="Fee Paid-->",bg="green",font=("comic sans ms",14))
    l6.place(x=60,y=280)
    l7=Label(fee,text="Admission No.-->",bg="green",font=("comic sans ms",14))
    l7.place(x=60,y=330)



    t1=Entry(fee,width=40)
    t1.place(x=250,y=130)
    t2=Entry(fee,width=40)
    t2.place(x=250,y=180)
    t3=Entry(fee,width=40)
    t3.place(x=250,y=230)
    t4=Entry(fee,width=40)
    t4.place(x=250,y=280)
    t5=Entry(fee,width=40)
    t5.place(x=250,y=330)

    



    b3=Button(fee,text="REM",width=14,height=2,command=remfee,bg="blue",fg="white",font=(7))
    b3.place(x=940,y=330)
    b4=Button(fee,text="ADD",width=14,height=2,command=addfee,bg="blue",fg="white",font=(7))
    b4.place(x=940,y=360)
    

    fee.mainloop()



    

ims=Tk()
WIDTH, HEIGTH=800,800
ims.geometry("{}x{}".format(WIDTH, HEIGTH))

canvas=Canvas(ims,width=WIDTH,height=HEIGTH)
image=ImageTk . PhotoImage(Image.open("F:\\computer_lect\\imsimg.jpg"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
la1=Label(ims,text="EDUCATION IS THE KEY TO YOUR SUCCESS",background="black",fg="blue",font=("verdan 15",20,'underline'))
la1.place(x=50,y=30)
button1=Button(ims,text="Add Student",command=m1,bg="black",fg="yellow",font=("comic sans ms",14))
button1.place(x=60,y=100)
button2=Button(ims,text="Remove Student",command=m2,bg="black",fg="yellow",font=("comic sans ms",14))
button2.place(x=260,y=100)
button3=Button(ims,text="Student Details",command=m3,bg="black",fg="yellow",font=("comic sans ms",14))
button3.place(x=490,y=100)
button4=Button(ims,text="Add Teacher",command=m4,bg="black",fg="yellow",font=("comic sans ms",14))
button4.place(x=60,y=160)
button5=Button(ims,text="Teacher Detail",command=m5,bg="black",fg="yellow",font=("comic sans ms",14))
button5.place(x=260,y=160)
button6=Button(ims,text="Remove Teacher",command=m6,bg="black",fg="yellow",font=("comic sans ms",14))
button6.place(x=490,y=160)
button7=Button(ims,text="Add Fee Details",command=m7,bg="black",fg="yellow",font=("comic sans ms",14))
button7.place(x=110,y=220)
button8=Button(ims,text="Remove Fee Details",command=m8,bg="black",fg="yellow",font=("comic sans ms",14))
button8.place(x=390,y=220)

ims.mainloop()


#PROJECT COMPLETED
#THANK YOU

