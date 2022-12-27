from tkinter import *
import pyodbc


try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Ahmed\Documents\Assign.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected To Database")

    cursor = conn.cursor()

except pyodbc.Error as e:
    print("Error in Connection", e)


#ClearRecord function
def ClearRecord():
    #Write your Clear Record Code Here
    cursor = conn.cursor()
    sname = ""
    fname = ""
    city = ""
    marks = ""
    cnic = cnicValue.get("")
    cursor.execute('UPDATE STUDENT SET sname = ?  , fname = ?  , city = ? , marks = ? WHERE cnic = ?', (sname, fname , city , marks , cnic))
    cnic = cnicValue.set("")
    conn.commit()
    cursor = conn.cursor()
    cursor.execute("UPDATE STUDENT SET cnic = ? WHERE sname = ?" , ("" , ""))
    conn.commit()
    print("Record Cleared")
    print("Clear Record")


#FirstRecord function
def FirstRecord():
    # Write your First Record Code Here
    print("First Record")
    cursor.execute('SELECT * FROM STUDENT')
    query_values = cursor.fetchall()[0]
    cursor.commit()
    name, fname, cnic , city , marks = query_values
    
    sNameValue.set(name)
    fNameValue.set(fname)
    cnicValue.set(cnic)
    cityValue.set(city)
    marksValue.set(marks)

#NextRecord function
def NextRecord():
    #Write your Next Record Code Here
    i = 0
    i = i + 1
    cursor.execute('SELECT * FROM STUDENT')
    data = cursor.fetchall()[i]
    (name, fname, cnic , city , marks) = data
    cursor.execute('UPDATE STUDENT SET sname = ?  , fname = ?  , city = ? , marks = ? WHERE cnic = ?', (name, fname , city , marks , cnic))
    cursor.commit()
    name  = sNameValue.set(name)
    fname  = fNameValue.set(fname)
    cnic  = cnicValue.set(cnic)
    city  = cityValue.set(city)
    
    print("Next Record")

#PreviousRecord function
def PreviousRecord():
    # Write your Previous Record Code Here
    i = 0
    i = i - 1
    cursor.execute('SELECT * FROM STUDENT')
    data = cursor.fetchall()[i]
    name, fname, cnic , city , marks = data
    sNameValue.set(name)
    fNameValue.set(fname)
    cnicValue.set(cnic)
    cityValue.set(city)
    marksValue.set(marks)
    print("Previous Record")

#LastRecord function
def LastRecord():
    # Write your Last Record Code Here
    print("Last Record")
    cursor.execute('SELECT * FROM STUDENT')
    query_values = cursor.fetchall()[-1]
    cursor.commit()
    name, fname, cnic , city , marks = query_values
    
    sNameValue.set(name)
    fNameValue.set(fname)
    cnicValue.set(cnic)
    cityValue.set(city)
    marksValue.set(marks)


#InsertRecord function
def InsertRecord():
    # Write your Insert Record Code Here
    print("Insert Record")
    name  = sNameValue.get()
    fname  = fNameValue.get()
    cnic  = cnicValue.get()
    city  = cityValue.get()
    marks  = marksValue.get()
    
    cursor.execute('INSERT INTO STUDENT VALUES (?,?,?,?,?);', (name , fname , cnic , city , marks))
    conn.commit()
    print('Data Inserted')
    sNameValue.set(name)
    fNameValue.set(fname)
    cnicValue.set(cnic)
    cityValue.set(city)
    marksValue.set(marks)

#UpdateRecord function
def UpdateRecord():
    # Write your Update Record Code Here
    print("Update Record")
    name  = sNameValue.get()
    fname  = fNameValue.get()
    cnic  = cnicValue.get()
    city  = cityValue.get()
    marks  = marksValue.get()

    cursor = conn.cursor()
    cursor.execute('UPDATE STUDENT SET sname = ?  , fname = ?  , city = ? , marks = ? WHERE cnic = ?', (name, fname , city , marks , cnic))
    conn.commit()
    print("Data updated")

#DeleteRecord function
def DeleteRecord():
    # Write your Delete Record Code Here
    print("Delete Record")
    user_cnic = input("enter the cnic of the user  to delete the data")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM STUDENT WHERE cnic = ?', (user_cnic))
    conn.commit()
    print("Data Deleted ")

#SearchRecord function
def SearchRecord():
    # Write your Search Record Code Here
    print("Search Record")
    user_cnic = cnicValue.get("")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM STUDENT WHERE cnic = ?' , (user_cnic))
    data = cursor.fetchall()[0]
    (name, fname, cnic , city , marks) = data
    sNameValue.set(name)
    fNameValue.set(fname)
    cnicValue.set(cnic)
    cityValue.set(city)
    marksValue.set(marks)

    conn.commit()

#Design the Student Database Form
root = Tk()
root.geometry("600x400")

#
Label(root, text = "Student Database Form", font="Arial 12 bold", foreground='blue').grid(row=0, column=0)
message = Label(root, text = "Message Will Appear Here!",foreground='red')
sname = Label(root,text='Student Name', font="ar 10 bold")
fname = Label(root,text='Father Name',font="ar 10 bold")
cnic = Label(root,text='CNIC# (P.Key)',font="ar 10 bold")
search = Label(root,text='Search Record',font="ar 10 bold")
city = Label(root,text='City',font="ar 10 bold")
marks = Label(root,text='Marks',font="ar 10 bold")

message.grid(row=0,column=1)
sname.grid(row=2,column=0)
fname.grid(row=3,column=0)
cnic.grid(row=4,column=0)
search.grid(row=4,column=2)
city.grid(row=5,column=0)
marks.grid(row=6,column=0)

sNameValue = StringVar()
fNameValue = StringVar()
cnicValue = StringVar()
cityValue = StringVar()
marksValue = IntVar()

sNameEntery = Entry(root, textvariable=sNameValue,width='30',font='ar 12 bold')
fNameEntery = Entry(root, textvariable=fNameValue,width='30',font='ar 12 bold')
cnicEntery = Entry(root, textvariable=cnicValue,width='30',font='ar 12 bold')
cityEntery = Entry(root, textvariable=cityValue,width='30',font='ar 12 bold')
marksEntery = Entry(root, textvariable=marksValue,width='30',font='ar 12 bold')

sNameEntery.grid(row=2,column=1,pady=15)
fNameEntery.grid(row=3,column=1,pady=15)
cnicEntery.grid(row=4,column=1,pady=15)
cityEntery.grid(row=5,column=1,pady=15)
marksEntery.grid(row=6,column=1,pady=15)

Button(text="CLEAR",command=ClearRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=7,column=0)
Button(text="FIRST",command=FirstRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=7,column=1)
Button(text="NEXT",command=NextRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=7,column=2)
Button(text="PREVIOUS",command=PreviousRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=9,column=0)
Button(text="LAST",command=LastRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=9,column=1)
Button(text="INSERT",command=InsertRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=9,column=2)
Button(text="UPDATE",command=UpdateRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=11,column=0)
Button(text="DELETE",command=DeleteRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=11,column=1)
Button(text="SEARCH",command=SearchRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=11,column=2)

root.mainloop()
