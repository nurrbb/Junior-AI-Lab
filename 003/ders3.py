mesaj = "merhaba" # bu bir string veri tipindedir, "" içinde kalan her şey
isim = "nur"
meyve = "nar"
tahmin = "12" # bu da string veri tipindedir

yas = 26 # bu bir integer veri tipidir çünkü tam sayıdır
fen_notu = 93
can = 35

boy = 1.65 # bu bir float veri tipidir çünkü virgüllüdür. (ondalık sayı)
bakiye = 325.65

oyun_bitti_mi = True # boolean(doğru/yanlış) soru soruyormuşuz gibi isim veririz
gecti_mi = False #true= doğru; false= yanlış
ogrenci_mi = False 

#print("Ad: Nur \nSoyad: Bozbey") 
# \n : next line: sonraki satıra geçer.

# ad = input("isminizi giriniz: ") #input() 
# print("Merhaba, "+ ad) # print -> output 

# isim = input("İsim: ")
# sehir =input("Sehir: ")
# meslek = input("Meslek: ")
# print("\n ---Kartvizit--- \nİsim:" + isim +"\nŞehir: "+ sehir + "\nMeslek: "+ meslek)

# sayi1 = int(input("Birinci:")) #int() -> interger(tam sayı) veri tipine dönüştürür.
# sayi2 = int(input("İkinci:")) 
# print("Toplam: ", sayi1+sayi2)


# dogum = int(input("Doğum yılı: ")) # dogum = 2002 - int koymazsak dogum = "2002"
# yil = 2026
# yas = yil-dogum
# print("Yaşınız: ", yas)

# fiyat = float(input("ürünün fiyatı: "))
# kdvli = fiyat * 1.20
# print("Kdv dahil fiyat: ", kdvli)

# yaricap = float(input("Dairenin yarıçapını giriniz: "))
# pi = 3.14
# alan = pi * (yaricap **2)
# print("Dairenin alanı: ", alan)

# kelime = input("Tekrar edilmesini istediğiniz kelimeyi giriniz: ")
# tekrar = int(input("Peki kaç kere tekrar edilmesini istiyorsunuz?: "))
# #print(kelime*tekrar)
# print((kelime+"\n")*tekrar)

kısa = int(input("Kısa kenar:"))
uzun = int(input("Uzun kenar: "))
alan = kısa* uzun
print("Alan", alan)

hesap = float(input("Hesap: "))
yuzde = int(input("Bahşiş yüzdesi: "))
bahsis = hesap * (yuzde/100)
print("ödenecek bahşiş: ", bahsis)