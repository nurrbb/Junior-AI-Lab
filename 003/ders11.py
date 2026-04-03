# fonksiyon tanımlarken "def"  ile başlarız

# #tanımla
# def motivasyon():
#     print("Unutma:  Bugün iyi bir gün.")

# #çağır
# motivasyon()

# def sistem_kontrol():
#     print("Batarya: %100 ok.")
#     print("Sensörler: Aktif")

# sistem_kontrol()   

#tanımla
# def karsila(isim):
#     print(f"Merhaba {isim} sisteme başarıyla giriş yaptı")

# isim = input("İsminizi girin: ")

# çağır
# karsila(isim)

# def radar_kontrol(hiz):
#     if hiz > 120:
#         print("Hız sınırı aşıldı. Ceza yazıldı")
#     else:
#         print("Hızınıız normal.")

# hiz = input("Güncel hızınız: ")

# radar_kontrol(hiz)

# def topla(a,b):
#     print(a+b)

# def carp(a,b):
#     print( a*b)

# def cıkar (a,b):
#     if a>b:
#         print(a-b)
#     else:
#         print(b-a)

# def bol(a,b):
#     if b == 0:
#         print("Bir sayı sıfıra bölünemez")
#     else:
#         print(a/b)

# while True:
#     islem = input("İşlem(+,*,-,/) çıkmak için '0' tuşlayınız")
#     if islem == 0:
#         break
#     sayi1, sayi2 = int(input("1. Sayı: ")), int(input("2. Sayı: "))

#     if islem == "+":
#         topla(sayi1,sayi2)
#     elif islem == "*":
#         carp(sayi1,sayi2)
#     elif islem == "-":
#         cıkar(sayi1,sayi2)
#     elif islem == "/":
#         bol(sayi1,sayi2)
#     else:
#         print("Geçersiz seçim.")


# def topla(a,b):
#     toplam = a+b
#     print(toplam)
#     return toplam 

# sonuc = topla(10,5) 
# print(sonuc)
# print(sonuc * 2)

# def indirim(fiyat):
#     return fiyat * 0.8

# yeni = indirim(100) #80
# print("indirimli:" , yeni)
# toplam = yeni + 59 # kargo ekledik
# print("kargo dahil: ",toplam)

# def karesi(sayi):
#     return sayi * sayi

# def ikiye_bol(sayi):
#     return sayi / 2

# sayi1 = int (input("İlk karesi alınıp sonra ikiye bölünecek sayı: "))
# sonuc = ikiye_bol(karesi(sayi1))
# print(sonuc)

# def indirimli(tutar):
#     return tutar * 0.9 if tutar > 200 else tutar

# def kargo(tutar):
#     return tutar + 20 if tutar < 150 else tutar

# while True:
#     fiyat = float(input("ütünün fiyatı (çıkmak için 0 )"))
#     if fiyat == 0:
#         break
#     ara = indirimli(fiyat)
#     son = kargo(ara)
#     print(f"Ödemeniz gereken net tutar: {son} TL")

# def doyur(seviye, yemek):
#     return seviye + yemek

# def aciktir(seviye):
#     return seviye - 10

# evcil_hp = 50

# while evcil_hp > 0:
#     print(f" Evcil Hayvan açlık: {evcil_hp}")
#     islem = input("1: yemek ver, 2: bekle")

#     if islem == "1":
#         evcil_hp = doyur(evcil_hp,20)
#     else:
#         evcil_hp = aciktir(evcil_hp)
    
#     if evcil_hp > 100:
#         evcil_hp = 100


def seviye_atla(mevcut,yeni):
    toplam = mevcut + yeni
    return toplam // 100, toplam %100

xp, seviye = 0,1 

while seviye <10:
    print(f"Seviye: {seviye}, | XP: {xp}/100")
    gelen_xp = int(input("Kazanılan XP: "))

    ek_seviye, kalan_xp = seviye_atla(xp,gelen_xp) 
    seviye += ek_seviye
    xp= kalan_xp

print("Tebrikler! Maksimum seviyeye ulaştınız!")