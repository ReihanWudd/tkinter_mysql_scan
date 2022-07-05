from tkinter import *
from tkinter.font import BOLD
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# from PIL import Image, ImageTk
import time
import MySQLdb
from pyfingerprint.pyfingerprint import PyFingerprint



root = ttk.Window(themename="superhero")
root.title("page 01")
root.geometry("1024x600")

def thisdatabase():
    class ourdatabase:
        def __init__ (self,code):
            self.code = code

def mysqlconnect(x):
    global info
    #Trying to connect
    try:
        db_connection= MySQLdb.connect("localhost","root","","ouruser")
    # If connection is not successful
    except:
        print("Can't connect to database")
        return 0
    # If Connection Is Successful
    print("Connected")
    insertdt = db_connection.cursor()
    
    try:
        my_sql = "select code from data_user where code="+data_ent.get()
        insertdt.execute(my_sql)
        hasil = insertdt.fetchall()
    except:
        print("error")
    db_connection.commit()
    db_connection.close()
    str_get = "(("+data_ent.get()+",),)"
    if (str(hasil) == str_get):
        tampilan02()
        
    else:
        print("falsees")
        info=ttk.Label(fr01 ,bootstyle="danger",text="data belum terdaftar", font='Arial 20 ')
        info.place(relx=0.5, rely=0.5, anchor=CENTER)
        info2=ttk.Label(fr01 ,bootstyle="danger",text="sudah melakukan pemilihan", font='Arial 20 ')
        info2.place(relx=0.5, rely=0.6, anchor=CENTER)
 
 
# Function Call For Connecting To Our Database


def tampilan01():
    global fr01,data_ent
    fr01 = Frame(root,width=900,height=600)
    fr01.place(relx=0.5, rely=0.5, anchor=CENTER)

    label=Label(fr01, text="SELAMAT DATANG\nSILAHKAN SCAN E-KTP ANDA",bg="#52dd5d", font='Arial 25 bold')
    label.place(relx=0.5, rely=0.2, anchor=CENTER)
    data_ent = ttk.Entry(fr01,bootstyle='info',width=30,font="arial 19")
    data_ent.bind('<Return>',mysqlconnect)
    data_ent.place(relx=0.5, rely=0.4, anchor=CENTER)
    logos = ttk.Label(fr01,bootstyle='secondary',text="E-Voting Machine",font="arial 20")
    
    logos.place(relx=0.1, rely=0.9, anchor=CENTER)
    

# def scann(x):
#     if(data_ent)


def tampilan02():
    fr01.place_forget() 
    global fr02,data_ent,img
    fr02 = Frame(root,width=900,height=600)
    fr02.place(relx=0.5, rely=0.5, anchor=CENTER)

    tlt=Label(fr02, text="SILAHKAN SCAN JARI ANDA",bg="#52dd5d", font='Arial 25 bold')
    tlt.place(relx=0.5, rely=0.1, anchor=CENTER)
    
    # label=Label(fr02, text="SILAHKAN SCAN JARI ANDA",bg="#52dd5d", font='Arial 30 bold')
    # label.place(relx=0.5, rely=0.2, anchor=CENTER)
    img = PhotoImage(file="D:/coding/2022/python/fingerprint2.png")
    finger_lbl = Label(fr02,image=img)
    finger_lbl.place(relx=0.5,rely=0.3,anchor=CENTER)

    data_ent = ttk.Entry(fr02,bootstyle='info',width=25,font="arial 19")
    data_ent.bind('<Return>',scann)
    data_ent.place(relx=0.5, rely=0.45, anchor=CENTER)
    logos = ttk.Label(fr02,bootstyle='secondary',text="E-Voting Machine",font="arial 20")
    
    logos.place(relx=0.1, rely=0.9, anchor=CENTER)
def tampilan03():
    # fr02.place_forget() 
    global fr03,data_ent,img
    fr03 = Frame(root,width=900,height=600)
    fr03.place(relx=0.5, rely=0.5, anchor=CENTER)

    tlt=Label(fr03, text="SILAHKAN MEMASUKI BILIK SUARA",bg="#52dd5d", font='Arial 25 bold')
    tlt.place(relx=0.5, rely=0.3, anchor=CENTER)
    logos = ttk.Label(fr03,bootstyle='secondary',text="E-Voting Machine",font="arial 20")
    
    logos.place(relx=0.1, rely=0.9, anchor=CENTER)

tampilan03()


root.mainloop()
