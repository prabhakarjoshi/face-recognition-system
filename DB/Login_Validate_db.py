from tkinter import *
import tkinter.messagebox
import mysql.connector

# import Dashboard_UI

def Login_Validate_fun(login,name,code,passw):
    
    mydb=mysql.connector.connect(host="localhost",
    user="root",
    password="",
    database="face-recognition")
    cursor = mydb.cursor()
    if not mydb.is_connected:
        tkinter.messagebox.showinfo("Error while connecting to the database!")
    else:
        if login:
            query1 = "SELECT `password` FROM `login` WHERE username='"+name+"'"
            cursor.execute(query1)

            for row in cursor: 
                if row[0]==passw:
                    print("loginn successfull")
                    # Dashboard_UI.Dashboard_UI_Fun()
                    break   

            cursor.close()
            mydb.close()
            
            

            
        else:
            # print("signup ho gya") 
            query1 = "INSERT INTO `login` (`username`, `password`, `Code number`) VALUES ('"+name+"', '"+passw+"', '"+code+"')"
            cursor.execute(query1)
            cursor.execute("commit")   
            cursor.close()
            mydb.close()
