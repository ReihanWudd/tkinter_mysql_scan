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

#ini untuk menampung class untuk memanggil database nya
def thisdatabase():
    #class saya global agar bisa di panggil di function firstdata()
    global ourdatabase
    class ourdatabase:
        #ini untuk menampung value paramater yang diberikan
        def __init__ (self,code,command,page,command2,command3):
            self.code = code
            self.command = command
            self.page = page
            self.command2 = command2
            self.command3 = command3
        
        #ini untuk mengirimkan data nama dari pengguna dan juga status pemilihan
        def sendname(self):
            global hasil2
            try:
                db_connection= MySQLdb.connect("localhost","root","","ouruser")
            except:
                print("Can't connect to database")
                return 0
            print("Connected")
            insertdt2 = db_connection.cursor()
            #ini untuk mengeksekusi select nama dan juga status
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

            #ini hanya variabel penampung string pengecekan
            cek = "('sudah memilih',)"
            #tampilan02() fungsinya untuk berpindah ke page 2 dengan mengirim parameter hasil2[0]
            tampilan02(hasil2[0])
            #ini pengeeckan untuk status dari pengguna
            if(str(hasil3[0])== cek):
                #ini label fungsinya untuk menampilkan tulisan di windownya
                info2=Label(fr02 ,text="Sudah melakukan pemilihan", font='Arial 20 ',bg="#2172bd",fg="white")
                info2.place(relx=0.5, rely=0.6, anchor=CENTER)
            else:
                #sama
                info2=Label(fr02 ,text="Belum melakukan pemilihan", font='Arial 20 ',bg="#2172bd",fg="red")
                info2.place(relx=0.5, rely=0.6, anchor=CENTER)


        def mysqlconnect(self):
            global info
            #koneksi database, untuk alamat,user,database nya bisa disesuaikan 
            try:
                db_connection= MySQLdb.connect("localhost","root","","ouruser")
            # If connection is not successful
            except:
                print("Can't connect to database")
                return 0
            # If Connection Is Successful
            print("Connected")
            insertdt = db_connection.cursor()
            #ini untuk mengeksekusi pengecekan codenya
            try:
                my_sql = self.command
                insertdt.execute(my_sql)
                hasil = insertdt.fetchall()
            except:
                print("error")

            db_connection.commit()
            db_connection.close()
            #ini fungsi nya variabel penampung string untuk di cek
            str_get = "(("+self.code+",),)"
            #pengecekan berdasarkan inputan code dari user dan juga code pada database
            if (str(hasil) == str_get):
                #ini untuk menjalankan function send name diatas
                self.sendname()
       
            else:
                #untuk menghapus isi dari entrynya
                data_ent.delete(0,END)
                #menampilkan labelnya 
                info=Label(fr01 ,text="data belum terdaftar", font='Arial 20 ',bg="#5ac14e",fg="red")
                info.place(relx=0.5, rely=0.5, anchor=CENTER)


def firstdata(x):
    #untuk menjalankan fungsi class nya
    thisdatabase()
    #untuk memanggil class ourdatabse dan juga nilai di dalam kurung akan di kirim ke parameter class secara berurutan
    resultdata= ourdatabase(data_ent.get(),"select code from data_user where code="+data_ent.get(),1,"select name from data_user where code="+data_ent.get(),"select status from data_user where code="+data_ent.get())
    #untuk memanggil fungsi mysqlconnect() pada class ourdatabase
    resultdata.mysqlconnect()

def tampilan01():
    #global agar variable bisa diakses dimanapun
    global fr01,data_ent
    #root ini untuk mengganti warnanya background
    root.configure(bg="#5ac14e")
    #frame ini fungsinya untuk menampung widged2 nya agar jika didelete sekali menghapus frame bisa menghapus semuanya
    fr01 = Frame(root,width=900,height=600,bg="#5ac14e")
    #untuk posisi bisa merubah relx/y max nilai 1 jadi bisa 0.1 / 0.5 dst
    fr01.place(relx=0.5, rely=0.5, anchor=CENTER)

    label=Label(fr01, text="SELAMAT DATANG\nSILAHKAN SCAN E-KTP ANDA",bg="#5ac14e", fg="white",font='Arial 25 bold')
    label.place(relx=0.5, rely=0.2, anchor=CENTER)
    data_ent = Entry(fr01,width=30,font="arial 19")
    #untuk bind ini fungsinya agar saat di enter langsung menjalankan function firstdata
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

    # bck_btn = Button(fr02,text="<< back" ,command=tampilan01)

    tlt=Label(fr02, text="SILAHKAN SCAN JARI ANDA",bg="#2172bd",fg="white", font='Arial 25 bold')
    tlt.place(relx=0.5, rely=0.1, anchor=CENTER)
    #fungsinya untuk memanggil file gambarnya bisa di edit directory filenya
    img = PhotoImage(file="D:/coding/2022/python/fingerprint2.png")
    finger_lbl = Label(fr02,image=img,bg="#2172bd")
    finger_lbl.place(relx=0.5,rely=0.3,anchor=CENTER)

    #untuk fungsi dari perpindahan halaman sebernarnya cuma memanggil function tampilan03() saja karena sudah otomatis ganti halaman
    #contoh jika memakai button
    # btn_page3 = Button(fr02,text="next >>" ,command=tampilan03)
    # btn_page3.place(relx=0.5, rely=0.53, anchor=CENTER)
    #jadi perpindahannya hanya menggunakan command=tampilan03 saja
    
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
    fr03.place(relx=0.5, rely=0.6, anchor=CENTER)

    tlt=Label(fr03, text="SILAHKAN MEMASUKI BILIK SUARA",bg="#ff5f01",fg="white", font='Arial 25 bold')
    tlt.place(relx=0.5, rely=0.3, anchor=CENTER)
    logos = Label(fr03,text="E-Voting Machine",font="arial 20",fg="white",bg="#ff5f01")
    
    logos.place(relx=0.2, rely=0.7, anchor=CENTER)

#untuk memanggil halaman pertama
tampilan01()


root.mainloop()
