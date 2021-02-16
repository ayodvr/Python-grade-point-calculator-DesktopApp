from tkinter import *
from gpcalculator import *

root = Tk()
root.configure(bg="#000")
root.title("Gp Calculator")
root.rowconfigure(13,minsize="20")
root.columnconfigure([0,1,2,3,4,5,6],minsize="20")

Title = Label(root,text="SEMESTER GRADE POINT CALCULATOR",font=(30),bg="#000",fg="#fff")
Title.grid(row=0,column=3,padx=10,pady=10)

Name = Label(root,text="ENTER YOUR NAME",font=(30),bg="#000",fg="#fff")
Name.grid(row=1,column=3,padx=5,pady=5)

Input = Entry(root,width=60)
Input.grid(row=2,column=3,padx=5,pady=5)

Header = Label(root,text="SCORES INPUT",font=(30),bg="#000",fg="#fff")
Header.grid(row=3,column=3,padx=5,pady=5)

Sn = Label(root,text="SN",font=(30),bg="#000",fg="#fff")
Sn.grid(row=4,column=0)

CourseName = Label(root,text="COURSE NAME",font=(20),bg="#000",fg="#fff")
CourseName.grid(row=4,column=2)

Scores = Label(root,text="SCORES",font=(20),bg="#000",fg="#fff")
Scores.grid(row=4,column=3)

CourseUnit = Label(root,text="COURSE UNIT",font=(20),bg="#000",fg="#fff")
CourseUnit.grid(row=4,column=4)

num1 = Label(root,text="1",font=(10),bg="#000",fg="#fff")
num1.grid(row=5,column=0)

num2 = Label(root,text="2",font=(10),bg="#000",fg="#fff")
num2.grid(row=6,column=0)

num3 = Label(root,text="3",font=(10),bg="#000",fg="#fff")
num3.grid(row=7,column=0)

num4= Label(root,text="4",font=(10),bg="#000",fg="#fff")
num4.grid(row=8,column=0)

num5= Label(root,text="5",font=(10),bg="#000",fg="#fff")
num5.grid(row=9,column=0)

options = [
    "Select Course",
    "Html",
    "Css",
    "Javascript",
    "Php",
    "Python"
]
c_name1 = StringVar()
c_name1.set(options[0])
course1 = OptionMenu(root,c_name1,*options)
course1.grid(row=5,column=2,padx=5,pady=5)

c_name2 = StringVar()
c_name2.set(options[0])
course2 = OptionMenu(root,c_name2,*options)
course2.grid(row=6,column=2,padx=5,pady=5)

c_name3 = StringVar()
c_name3.set(options[0])
course3 = OptionMenu(root,c_name3,*options)
course3.grid(row=7,column=2,padx=5,pady=5)

c_name4 = StringVar()
c_name4.set(options[0])
course4 = OptionMenu(root,c_name4,*options)
course4.grid(row=8,column=2,padx=5,pady=5)

c_name5 = StringVar()
c_name5.set(options[0])
course5 = OptionMenu(root,c_name5,*options)
course5.grid(row=9,column=2,padx=5,pady=5)

Scores1 = Entry(root,width=5)
Scores1.grid(row=5,column=3,padx=5,pady=5)

Scores2 = Entry(root,width=5)
Scores2.grid(row=6,column=3,padx=5,pady=5)

Scores3 = Entry(root,width=5)
Scores3.grid(row=7,column=3,padx=5,pady=5)

Scores4 = Entry(root,width=5)
Scores4.grid(row=8,column=3,padx=5,pady=5)

Scores5 = Entry(root,width=5)
Scores5.grid(row=9,column=3,padx=5,pady=5)

options = [
    0,
    1.5,
    3,
    2,
    2.5,
    4
] 
cunit1 = IntVar()
cunit1.set(options[0])
unit1 = OptionMenu(root,cunit1,*options)
unit1.grid(row=5,column=4,padx=5,pady=5)

cunit2 = IntVar()
cunit2.set(options[0])
unit2 = OptionMenu(root,cunit2,*options)
unit2.grid(row=6,column=4,padx=5,pady=5)

cunit3 = IntVar()
cunit3.set(options[0])
unit3 = OptionMenu(root,cunit3,*options)
unit3.grid(row=7,column=4,padx=5,pady=5)

cunit4 = IntVar()
cunit4.set(options[0])
unit4 = OptionMenu(root,cunit4,*options)
unit4.grid(row=8,column=4,padx=5,pady=5)

cunit5 = IntVar()
cunit5.set(options[0])
unit5 = OptionMenu(root,cunit5,*options)
unit5.grid(row=9,column=4,padx=5,pady=5)

Name = Label(root,text="Name :",font=(20),bg="#000",fg="#fff")
Name.grid(row=11,column=2)

GradePoint = Label(root,text="Grade Point :",font=(20),bg="#000",fg="#fff")
GradePoint.grid(row=12,column=2)

Remarks = Label(root,text="Remarks :",font=(20),bg="#000",fg="#fff")
Remarks.grid(row=13,column=2)

def calGp():
    Inputs = Input.get()

    sc1 = Scores1.get()
    sc2 = Scores2.get()
    sc3 = Scores3.get()
    sc4 = Scores4.get()
    sc5 = Scores5.get()

    cu1 = cunit1.get()
    cu2 = cunit2.get()
    cu3 = cunit3.get()
    cu4 = cunit4.get()
    cu5 = cunit5.get()
    cgpa = Gpcalculator([sc1,sc2,sc3,sc4,sc5],[cu1,cu2,cu3,cu4,cu5])
    score   = cgpa.getCgp()
    remark  = cgpa.remark()
    rel = Label(root,text=Inputs,font=(20),bg="#000",fg="#fff")
    rel.grid(row=11,column=3)
    res = Label(root,text=score,font=(20),bg="#000",fg="#fff")
    res.grid(row=12,column=3)
    rem = Label(root,text=remark,font=(20),bg="#000",fg="#fff")
    rem.grid(row=13,column=3)
    

Button = Button(root,text="Calculate",width=20,bg="gold",fg="#000",font=20,command=calGp)
Button.grid(row=10,column=3)

root.mainloop()