import imp
from tkinter import *
import MySQLdb
import time
from pyfingerprint.pyfingerprint import PyFingerprint

def fingerscan ():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    # Tries to enroll new finger
    try:
        print('Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        # Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

    # Checks if finger is already enrolled
        result = f.searchTemplate()
        positionNumber = result[0]

        if ( positionNumber >= 0 ):
            print('Template already exists at position #' + str(positionNumber))
            exit(0)

        print('Remove finger...')
        time.sleep(2)

        print('Waiting for same finger again...')

        # Wait that finger is read again
        while ( f.readImage() == False ):
            pass

        # Converts read image to characteristics and stores it in charbuffer 2
        f.convertImage(0x02)

        # Compares the charbuffers
        if ( f.compareCharacteristics() == 0 ):
            raise Exception('Fingers do not match')

        # Creates a template
        f.createTemplate()

        # Saves template at new position number
        positionNumber = f.storeTemplate()
    
        print('Finger enrolled successfully!')
        
    
        f.loadTemplate(positionNumber, 0x01)
        char_store = str (f.downloadCharacteristics(0x01))
        char_store1= char_store.translate(None, ',[]')
    
        return positionNumber, char_store1
        
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)

def sendname(id,st,nm,jk,idfgr,tmpid):
    global hasil2
    try:
        db_connection= MySQLdb.connect("localhost","root","","ektp")
    except:
        print("Can't connect to database")
        return 0
    print("Connected")
    insertdt2 = db_connection.cursor()
    try:
        my_sql2 = "INSERT INTO `t_user`(`id_user`, `fullname`, `jk`, `status`, `id_finger`, `temp_finger`) VALUES ('%s', '%s', '%s', '%i', '%s','%s)"%(id,nm,jk,st,idfgr,tmpid)
        insertdt2.execute(my_sql2)
        print("data insert successfully")
    except:
        print("error")
    
    db_connection.commit()
    db_connection.close()

print("Type DONE to exit!")
fullname="kosong" 
while (fullname!='DONE'):
        inp_id= input    ("ENTER id         =")
        inp_status =input("ENTER status     =")
        inp_nama = input ("ENTER fullname   =")
        inp_gdr = input  ("ENTER kelamin L/P=")

        print('Scan Jari Anda!')
        result = fingerscan()
        id_finger=result[0]
        print('ID Fingerprint: %i' %id_finger)
        print(' \n')
        templ_finger=result[1]
        sendname(inp_id,inp_status,inp_nama,inp_gdr,id_finger,templ_finger)
        fullname=input("Nama Lengkap   : ")

