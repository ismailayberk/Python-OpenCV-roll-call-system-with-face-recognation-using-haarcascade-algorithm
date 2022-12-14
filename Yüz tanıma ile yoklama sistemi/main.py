############################################# KULLANILAN KÜTÜPHANELERİ İMPORT ETTİM ################################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time

############################################# FONKSİYONLARIM ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200,tick)

###################################################################################

def contact():
    mess._show(title='Bize Ulaş', message="Lütfen Bize Buradan Ulaş : 'ayberkguns@gmail.com' ")

###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Bazı Dosyalar Eksik', message='Lütfen Yardım İçin Bize Ulaş')
        window.destroy()

###################################################################################

def save_pass():
    assure_path_exists("ResimleriOgretmeBolumu/")
    exists1 = os.path.isfile("ResimleriOgretmeBolumu\Sifre.txt")
    if exists1:
        tf = open("ResimleriOgretmeBolumu\Sifre.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Eski Şifre Bulunamadı', 'Lütfen Önce Yeni Şifreyi Girin', show='*')
        if new_pas == None:
            mess._show(title='Şifre Girilmedi', message='Şifre Ayarlanamadı, Lütfen Tekrar Deneyin!')
        else:
            tf = open("ResimleriOgretmeBolumu\Sifre.txt", "w")
            tf.write(new_pas)
            mess._show(title='Şifre Oluşturuldu', message='Yeni Şifre Başarıyla Oluşturuldu!')
            return
    op = (old.get())
    newp= (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("ResimleriOgretmeBolumu\Sifre.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Hata', message='Yeni Şifreyi Tekrar Doğrulayın!')
            return
    else:
        mess._show(title='Hatali Şifre', message='Eski Şifreniz Hatalı')
        return
    mess._show(title='Şifre Değiştirildi', message='Şifre Başarıyla Değiştirildi!')
    master.destroy()

###################################################################################

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False,False)
    master.title("Şifre Değiştir")
    master.configure(background="white")
    lbl4 = tk.Label(master,text='    Eski Şifrenizi Girin',bg='white',font=('times', 12, ' bold '))
    lbl4.place(x=10,y=10)
    global old
    old=tk.Entry(master,width=25 ,fg="black",relief='solid',font=('times', 12, ' bold '),show='*')
    old.place(x=180,y=10)
    lbl5 = tk.Label(master, text='   Yeni Şifrenizi Girin', bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black",relief='solid', font=('times', 12, ' bold '),show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Yeni Şifrenizi Doğrulayın', bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid',font=('times', 12, ' bold '),show='*')
    nnew.place(x=180, y=80)
    cancel=tk.Button(master,text="Çıkış", command=master.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Kaydet", command=save_pass, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()

#####################################################################################

def psw():
    assure_path_exists("ResimleriOgretmeBolumu/")
    exists1 = os.path.isfile("ResimleriOgretmeBolumu\Sifre.txt")
    if exists1:
        tf = open("ResimleriOgretmeBolumu\Sifre.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Eski Şifre Bulunamadı', 'Lütfen Önce Yeni Bir Şifre Girin', show='*')
        if new_pas == None:
            mess._show(title='Şifre Girilmedi', message='Şifre Ayarlanamadı, Lütfen Tekrar Deneyin')
        else:
            tf = open("ResimleriOgretmeBolumu\Sifre.txt", "w")
            tf.write(new_pas)
            mess._show(title='Şifre Oluşturuldu', message='Yeni Şifre Başarıyla Oluşturuldu!')
            return
    password = tsd.askstring('Şifre', 'Şifre Girin', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Hatalı Şifre', message='Hatalı Şifre Girdiniz')

######################################################################################

def clear():
    txt.delete(0, 'end')
    res = "Önce Fotograf Çek  >>>  Sonra Profili Kaydet"
    message1.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "Önce Fotograf Çek  >>>  Sonra Profili Kaydet"
    message1.configure(text=res)

#######################################################################################

def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    assure_path_exists("OgrenciDetaylari/")
    assure_path_exists("ResimleriOgret/")
    serial = 0
    exists = os.path.isfile("OgrenciDetaylari\OgrenciDetaylari.csv")
    if exists:
        with open("OgrenciDetaylari\OgrenciDetaylari.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("OgrenciDetaylari\OgrenciDetaylari.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()
    Id = (txt.get())
    name = (txt2.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum = sampleNum + 1
                # Çekilen fotoğrafları resimogret klasorüne ekliyorum
                cv2.imwrite("ResimleriOgret\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # Kamerayi açıp fotoğrafları çektiriyorum
                cv2.imshow('Fotograflar Cekiliyor', img)
            # 100 mili saniye bekliyor
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # haarcascade verisetinde 101 fotoğrafa ihtiyacım var bu yüzden 100den sonra programı break yapıyorum.
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Bu Id İçin Fotoğraflar Çekildi : " + Id
        row = [serial, '', Id, '', name]
        with open('OgrenciDetaylari\OgrenciDetaylari.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Doğru İsmi Girin"
            message.configure(text=res)

########################################################################################

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("ResimleriOgretmeBolumu/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("ResimleriOgret")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='Kayıt Mevcut Değil', message='Lütfen Birini Kayıt Edin!')
        return
    recognizer.save("ResimleriOgretmeBolumu\Ogretici.yml")
    res = "Profil Başarıyla Kaydedildi"
    message1.configure(text=res)
    message.configure(text='Şimdiye kadar kaydedilen profil sayısı  : ' + str(ID[0]))

############################################################################################3

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # Yüzlerin fotoğrafı için boş bir liste oluşturdum.
    faces = []
    # ID'ler için boş bir liste oluşturdum.
    Ids = []
    for imagePath in imagePaths:
        # Resmi gri yapıyorum ki seçilebilirliği artsın
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        # Fotoğraftan kimliği belirliyoruz.
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids

###########################################################################################

def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Yoklama/")
    assure_path_exists("OgrenciDetaylari/")
    for k in tv.get_children():
        tv.delete(k)
    msg = ''
    i = 0
    j = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    exists3 = os.path.isfile("ResimleriOgretmeBolumu\Ogretici.yml")
    if exists3:
        recognizer.read("ResimleriOgretmeBolumu\Ogretici.yml")
    else:
        mess._show(title='Veri Eksik', message='Verileri Temizlemek İçin Lütfen Profili Kaydete Tıklayın!')
        return
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    exists1 = os.path.isfile("OgrenciDetaylari\OgrenciDetaylari.csv")
    if exists1:
        df = pd.read_csv("OgrenciDetaylari\OgrenciDetaylari.csv")
    else:
        mess._show(title='Detaylar Eksik', message='Öğrenci Detayları Eksik, Lütfen Kontrol Edin!')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)
                ID = ID[1:-1]
                bb = str(aa)
                bb = bb[2:-2]
                attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]

            else:
                Id = 'Bilinmeyen Kisi'
                bb = str(Id)
            cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('Yoklama Aliniyor', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    exists = os.path.isfile("Yoklama\Yoklama_" + date + ".csv")
    if exists:
        with open("Yoklama\Yoklama_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(attendance)
        csvFile1.close()
    else:
        with open("Yoklama\Yoklama_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(col_names)
            writer.writerow(attendance)
        csvFile1.close()
    with open("Yoklama\Yoklama_" + date + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for lines in reader1:
            i = i + 1
            if (i > 1):
                if (i % 2 != 0):
                    iidd = str(lines[0]) + '   '
                    tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
    csvFile1.close()
    cam.release()
    cv2.destroyAllWindows()

#################################### CANLI TARİH VE SAAT GÖSTERİMİ ################################################
    
global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont={'01':'Ocak',
      '02':'Şubat',
      '03':'Mart',
      '04':'Nisan',
      '05':'Mayıs',
      '06':'Haziran',
      '07':'Temmuz',
      '08':'Ağustos',
      '09':'Eylül',
      '10':'Ekim',
      '11':'Kasım',
      '12':'Aralık'
      }

######################################## TASARIM BÖLÜMÜ ###########################################

window = tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("Yoklama Sistemi")
window.configure(background='#262523')

frame1 = tk.Frame(window, bg="blue")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="blue")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="YÜZ TANIMALI YOKLAMA SİSTEMİ" ,fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"  |  ", fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 18, ' bold '))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame3,fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 18, ' bold '))
clock.pack(fill='both',expand=1)
tick()

head2 = tk.Label(frame2, text="                       Yeni Kayıt İçin                       ", fg="white",bg="#000080" ,font=('times', 20, ' bold ') )
head2.grid(row=0,column=0)

head1 = tk.Label(frame1, text="                       Zaten Kayıtlıysanız                       ", fg="white",bg="#000080" ,font=('times', 20, ' bold ') )
head1.place(x=0,y=0)

lbl = tk.Label(frame2, text="ID'nizi Girin",width=20  ,height=1  ,fg="white"  ,bg="blue" ,font=('times', 17, ' bold ') )
lbl.place(x=80, y=55)

txt = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold '))
txt.place(x=30, y=88)

lbl2 = tk.Label(frame2, text="İsminizi Girin",width=20  ,fg="white"  ,bg="blue" ,font=('times', 17, ' bold '))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frame2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=30, y=173)

message1 = tk.Label(frame2, text="Önce Fotograf Çek  >>>  Sonra Profili Kaydet" ,bg="blue" ,fg="white"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
message1.place(x=7, y=230)

message = tk.Label(frame2, text="" ,bg="blue" ,fg="white"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
message.place(x=7, y=450)

lbl3 = tk.Label(frame1, text="Yoklama",width=20  ,fg="white"  ,bg="blue"  ,height=1 ,font=('times', 17, ' bold '))
lbl3.place(x=100, y=115)

res=0
exists = os.path.isfile("OgrenciDetaylari\OgrenciDetaylari.csv")
if exists:
    with open("OgrenciDetaylari\OgrenciDetaylari.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Şimdiye Kadar Olan Toplam Kayıt  : '+str(res))

##################### YARDIM MENÜSÜ #################################

menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Şifre Değiştir', command = change_pass)
filemenu.add_command(label='Bize Ulaş', command = contact)
filemenu.add_command(label='Çıkış',command = window.destroy)
menubar.add_cascade(label='Yardım',font=('times', 29, ' bold '),menu=filemenu)

################## YOKLAMA LİSTESİ TABLOSU ####################

tv= ttk.Treeview(frame1,height =13,columns = ('name','date','time'))
tv.column('#0',width=82)
tv.column('name',width=130)
tv.column('date',width=133)
tv.column('time',width=133)
tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
tv.heading('#0',text ='ID')
tv.heading('name',text ='ISİM')
tv.heading('date',text ='TARİH')
tv.heading('time',text ='SAAT')

######################################################

scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################### BUTTONLAR ##################################

clearButton = tk.Button(frame2, text="Temizle", command=clear  ,fg="white"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
clearButton.place(x=335, y=86)
clearButton2 = tk.Button(frame2, text="Temizle", command=clear2  ,fg="white"  ,bg="#ea2a2a"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton2.place(x=335, y=172)    
takeImg = tk.Button(frame2, text="Fotoğraf Çek", command=TakeImages  ,fg="white"  ,bg="#000080"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
takeImg.place(x=30, y=300)
trainImg = tk.Button(frame2, text="Profili Kaydet", command=psw ,fg="white"  ,bg="#000080"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trainImg.place(x=30, y=380)
trackImg = tk.Button(frame1, text="Yoklama Al", command=TrackImages  ,fg="white"  ,bg="green"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trackImg.place(x=30,y=50)
quitWindow = tk.Button(frame1, text="Çıkış", command=window.destroy  ,fg="white"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=30, y=450)

###########################################################

window.configure(menu=menubar)
window.mainloop()

####################################################################################################
