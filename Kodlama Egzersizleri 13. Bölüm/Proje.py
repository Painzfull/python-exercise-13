import kutuphane
from kutuphane import *

print("""*********************

Kütüphane Programına Hoşgeldiniz.

işlemler:


1. Kitapları göster

2. Kitap sorgulama

3. Kitap ekle 

4. Kitap sil

5. Baskı yükselt 

Çıkmak için q ya basın.


*********************""")

kütüphane = kutuphane.Class1()


while True:
    işlemler = input("Yapacağınız işlemi Seçiniz ==>")
    if(işlemler == "q"):
        print("Program Sonlandırılıyor....")
        time.sleep(1)
        break
    elif(işlemler == "1"):
        kütüphane.kitapları_göster()
        
    elif(işlemler == "2"):
        isim = input("Lütfen bir kitap ismi giriniz:")
        print("kitap sorgulanıyor..")
        time.sleep(1)
        kütüphane.kitap_sorgu(isim)
        
    elif(işlemler == "3"):
        isim = input("Lütfen Eklemek İstediğiniz Kitabın İsmini Giriniz:")
        yazar = input("Lütfen Eklemek İstediğiniz Kitabın Yazarını Giriniz:")
        yayınevi = input("Lütfen Eklemek İstediğiniz Kitabın Yayınevini Giriniz:")
        tür = input("Lütfen Eklemek İstediğiniz Kitabın Türünü Giriniz:")
        baskı = int(input("Lütfen Eklemek İstediğiniz Kitabın Baskısını Giriniz:"))
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap ekleniyor....")
        time.sleep(1)
        print("İstenilen Kitap Listeye Eklendi...")
        time.sleep(1)
    elif(işlemler == "4"):
        isim = input("Silmek İstediğiniz Kitabın ismin Giriniz:")
        cevap = input("Bu işlem Geri Alınamaz? (E/H) :")
        if(cevap == "E"):
            kütüphane.kitap_sil(isim)
            time.sleep(1)
            print("Kitap Siliniyor...")
            time.sleep(1)
            print("Kitap Silindi...")
            time.sleep(1)
        else:
            print("Geçersiz işlem")
            time.sleep(1)
        pass
    elif(işlemler == "5"):
        isim = input("Baskısı Yükseltilmek İstenen Kitap Adı:")
        kütüphane.baskı_yükselt(isim,)
        time.sleep(1)
        print("Baskı Yükseltiliyor...")
        time.sleep(1)
        print("Baskı Yükseltildi.")
        time.sleep(1)
    else:
        print("Geçersiz İşlem")
        time.sleep(1)

