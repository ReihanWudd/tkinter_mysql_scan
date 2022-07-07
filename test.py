from tkinter import *
import MySQLdb

def sendname(st,nm,nim,cls):
    global hasil2
    try:
        db_connection= MySQLdb.connect("localhost","root","","ektp")
    except:
        print("Can't connect to database")
        return 0
    print("Connected")
    insertdt2 = db_connection.cursor()
    try:
        my_sql2 = "INSERT INTO `t_vote`(`status` ,`nama`, `nim`, `class`) VALUES ('%s','%s','%s','%s')"%(st,nm,nim,cls)
        insertdt2.execute(my_sql2)
        print("data insert successfully")
    except:
        print("error")
    
    db_connection.commit()
    db_connection.close()

inp_status =input("ENTER status =")
inp_nama = input( "ENTER nama   =")
inp_nim = input(  "ENTER nim    =")
inp_class= input( "ENTER class  =")

sendname(inp_status,inp_nama,inp_nim,inp_class)

