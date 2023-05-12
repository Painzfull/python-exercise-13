import sqlite3
import time 

class Kitap():
    def __init__(self,isim,yazar,yayınevi,tür,baskı):

        self.isim = isim 
        self.yazar = yazar 
        self.yayınevi = yayınevi
        self.tür = tür 
        self.baskı = baskı


    def __str__(self):

        return "Kitap İsmi: {}\nKitabın Yazar: {}\nKitabın Yayınevi: {}\nKitabın Türü: {}\nKitabın Baskısı: {}\n".format(self.isim,self.yazar,self.yayınevi,self.tür,self.baskı)

class Class1():
    def bağlantı_oluştur(self):
        self.bağlantı = sqlite3.connect("Kütüphane.db")
        self.cursor = self.bağlantı.cursor()
        sorgu ="Create Table If Not Exists kitaplar (isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT)"
        self.cursor.execute(sorgu)
        self.bağlantı.commit()

    def __init__(self):
        self.bağlantı_oluştur()


    def bağlantıyı_kes(self):
        self.bağlantı.close()    

    def kitapları_göster(self):
        sorgu = "Select * From kitaplar" 
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Kütüphane İçerisinde Herhangi Bir Kitap Bulunamamıştır...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)
    def kitap_sorgu(self,isim):
        sorgu = "Select * From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()
        if(len(kitaplar) == 0):
            print("Böyle bir kitap sistemde görüntülenemiyor...")
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)
    def kitap_ekle(self,kitap):
        sorgu = "insert into kitaplar Values (?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.baskı))
        self.bağlantı.commit()

    def kitap_sil(self, isim):
        sorgu = "Delete From kitaplar where isim = ?"
        self.cursor.execute(sorgu, (isim,))
        self.bağlantı.commit()

    def baskı_yükselt(self,isim):
        sorgu = "Select * From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))   
        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Sistemde böyle bir kitap bulunmamakta...")
        else:
            baskı = kitaplar[0][4]
            baskı += 1

            sorgu2 = "Update kitaplar set baskı = ? where isim = ?"  
            self.cursor.execute(sorgu2,(baskı,isim))
            self.bağlantı.commit()  
