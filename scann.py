from email.mime import image
from tkinter import *
from tkinter.font import BOLD
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import MySQLdb
from pyfingerprint.pyfingerprint import PyFingerprint

root = Tk()
root.title("page 01")
root.geometry("1024x600")

def thisdatabase():
    global ourdatabase
    class ourdatabase:
        def __init__ (self,code,command,page,command2,command3):
            self.code = code
            self.command = command
            self.page = page
            self.command2 = command2
            self.command3 = command3
            # self.key = key
                

        def sendname(self):
            global hasil2
            try:
                db_connection= MySQLdb.connect("localhost","root","","ouruser")
            except:
                print("Can't connect to database")
                return 0
            print("Connected")
            insertdt2 = db_connection.cursor()
            try:
                my_sql2 = self.command2
                insertdt2.execute(my_sql2)
                hasil2 = insertdt2.fetchone()
                my_sql3 = self.command3
                insertdt2.execute(my_sql3)
                hasil3 = insertdt2.fetchall()
            except:
                print("error")
            db_connection.commit()
            db_connection.close()
            cek = "('sudah memilih',)"
            tampilan02(hasil2[0])
            if(str(hasil3[0])== cek):
                info2=Label(fr02 ,text="Sudah melakukan pemilihan", font='Arial 20 ',bg="#2172bd",fg="white")
                info2.place(relx=0.5, rely=0.6, anchor=CENTER)
            else:
                info2=Label(fr02 ,text="Belum melakukan pemilihan", font='Arial 20 ',bg="#2172bd",fg="red")
                info2.place(relx=0.5, rely=0.6, anchor=CENTER)

        def mysqlconnect(self):
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
                my_sql = self.command
                insertdt.execute(my_sql)
                hasil = insertdt.fetchall()
                
            except:
                print("error")

            db_connection.commit()
            db_connection.close()

            str_get = "(("+self.code+",),)"
            if (str(hasil) == str_get):

                if (self.page == 1):
                    self.sendname()
                else:
                    tampilan03()
       
            else:
                print("falsees")
                info=Label(fr01 ,text="data belum terdaftar", font='Arial 20 ',bg="#5ac14e",fg="red")
                info.place(relx=0.5, rely=0.5, anchor=CENTER)


def firstdata(x):
    thisdatabase()
    resultdata= ourdatabase(data_ent.get(),"select code from data_user where code="+data_ent.get(),1,"select name from data_user where code="+data_ent.get(),"select status from data_user where code="+data_ent.get())
    resultdata.mysqlconnect()

def tampilan01():
    global fr01,data_ent
    root.configure(bg="#5ac14e")
    fr01 = Frame(root,width=900,height=600,bg="#5ac14e")
    fr01.place(relx=0.5, rely=0.5, anchor=CENTER)

    label=Label(fr01, text="SELAMAT DATANG\nSILAHKAN SCAN E-KTP ANDA",bg="#5ac14e", fg="white",font='Arial 25 bold')
    label.place(relx=0.5, rely=0.2, anchor=CENTER)
    data_ent = Entry(fr01,width=30,font="arial 19")
    data_ent.bind('<Return>',firstdata)
    data_ent.place(relx=0.5, rely=0.4, anchor=CENTER)
    logos = Label(fr01,text="E-Voting Machine",font="arial 20",bg="#5ac14e",fg="white")
    
    logos.place(relx=0.2, rely=0.9, anchor=CENTER)
    
def tampilan02(hsl):
    fr01.place_forget() 
    root.configure(bg="#2172bd")
    global fr02,data_ent2,img
    fr02 = Frame(root,width=900,height=600,bg="#2172bd")
    fr02.place(relx=0.5, rely=0.5, anchor=CENTER)

    tlt=Label(fr02, text="SILAHKAN SCAN JARI ANDA",bg="#2172bd",fg="white", font='Arial 25 bold')
    tlt.place(relx=0.5, rely=0.1, anchor=CENTER)

    img = PhotoImage(file="D:/coding/2022/python/fingerprint2.png")
    finger_lbl = Label(fr02,image=img,bg="#2172bd")
    finger_lbl.place(relx=0.5,rely=0.3,anchor=CENTER)

    data_ent2 = Entry(fr02,width=25,font="arial 19")
    data_ent2.insert(0,hsl)
    data_ent2.place(relx=0.5, rely=0.45, anchor=CENTER)
    logos = Label(fr02,text="E-Voting Machine",fg="white",font="arial 20",bg="#2172bd")
    
    logos.place(relx=0.2, rely=0.9, anchor=CENTER)


def tampilan03():
    fr02.place_forget() 
    root.configure(bg="#ff5f01")
    global fr03,data_ent,img
    fr03 = Frame(root,width=900,height=600,bg="#ff5f01")
    fr03.place(relx=0.5, rely=0.5, anchor=CENTER)

    tlt=Label(fr03, text="SILAHKAN MEMASUKI BILIK SUARA",bg="#ff5f01", font='Arial 25 bold')
    tlt.place(relx=0.5, rely=0.3, anchor=CENTER)
    logos = Label(fr03,text="E-Voting Machine",font="arial 20")
    
    logos.place(relx=0.2, rely=0.9, anchor=CENTER)

tampilan01()


root.mainloop()
