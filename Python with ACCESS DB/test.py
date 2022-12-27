# import pyodbc

# try:
#     con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Ahmed\Documents\Assign.accdb;'
#     conn = pyodbc.connect(con_string)
#     print("Connected To Database")

#     cursor = conn.cursor()




    # while True:
    #     name  = input("enter the name")
    #     fname  = input("enter the fname")
    #     cnic  = input("enter the cnic")
    #     city  = input("enter the city")
    #     marks  = int(input("enter the marks"))
    #     users = (name, fname, cnic , city , marks)

    #     cursor.execute('INSERT INTO STUDENT VALUES (?,?,?,?,?)', users)
    #     conn.commit()
    #     print('Data Inserted')
    #     more_data_req = input("do you want to enter more data?")
    #     if more_data_req == "yes":
    #         continue
    #     else:
    #         break
 
 

# except pyodbc.Error as e:
#     print("Error in Connection", e)


import pyodbc


try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                 r'DBQ=C:\Users\Ahmed\Documents\Assign.accdb;'
    conn = pyodbc.connect(con_string)

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM STUDENT')


    for row in cursor.fetchall():
            print(row)

except pyodbc.Error as e:
    print("Error in Connection")

# import pyodbc

# try:
#     con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
#                  r'DBQ=C:\Users\Ahmed\Documents\Assign.accdb;'
#     conn = pyodbc.connect(con_string)

#     cursor = conn.cursor()




# except pyodbc.Error as e:
#     print("Error in connection", e)





# cnic = input("enter cnic to pick a row to be updated")
# sname = input("enter new studet name")
# fname = input("enter new studet father name")
# city = input("enter new studet name")
# marks = int(input("enter the marks"))


# cursor.execute('SELECT * FROM STUDENT')
# cur = conn.cursor()
# cur.execute('UPDATE STUDENT SET sname = ?  , fname = ?  , city = ? , marks = ? WHERE cnic = ?', (sname, fname , city , marks , cnic))
# conn.commit()
# print("Data updated")




# import pyodbc



# try:
#     con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
#                  r'DBQ=C:\Users\Ahmed\Documents\Assign.accdb;'
#     conn = pyodbc.connect(con_string)

#     user_cnic = input("enter the cnic of the user  to delete the data")

#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM STUDENT WHERE cnic = ?', (user_cnic))
#     conn.commit()
#     print("Data Deleted ")

# except pyodbc.Error as e:
#     print("Error in connection", e)


