#For: kaç kere döneceği belli olduğu durumda kullanılır.
#range(): belirli bir aralıkta sayılar üretir.
# 3 tane argüman alır: başlangıç, bitiş, artış miktarı
# range(1) , ranger(1,10) , range(1,10,-2)

#daima 0 dan başlar, bitiş dahil değildir.

# for i in range(4):
#     print(i , ". tur")

# print("***************")

# for i in range(1,6):
#     print(i , ". tur")

# for i in range (10,0,-1):
#     print(i)

# toplam = 0 

# for i in range(1,6):
#     print(toplam,"+",i)
#     toplam = toplam +i 
#     print(toplam)

# for i in range (1,11):
#     if i%2 == 0 :
#         print(i)

#while şart koşuyor.
# şart doğru olduğu sürece çalış.
#for: genelde kaç tur dönecğeini biliriz
#while daima şart vardır.

# sayac= 1
# while sayac <= 5:
#     print(sayac)
#     sayac = sayac +1

# n = 5 
# while n > 0:
#     print(n)
#     n = n - 1

# enerji = 20

# while enerji > 0:
#     print("Oyun oynuyor, enerji:", enerji)
#     enerji = enerji - 4

# print("Enerji bitti")

# sifre = "benbilmiyorumki1234"
# girilen_sifre = input("Şifreyi gir: ")

# while girilen_sifre != sifre:
#     girilen_sifre = input("Yalnış şifre, tekrar dene: ")

# print("Giriş Başarılı!")

#Fonksiyonlar: bir işi yapan kod bloğu 
#def ile tanımlanıyor
# YAZIYORUZ AMA ÇAĞIRILMADAN ÇALIŞMAZ!
#parametreli ya da paremetresiz olmak üzere 2 tipteydi
# parametre = fonksiyonun dışarıdan aldığı bilgi

# def selamla(isim):
#     print(isim, "Merhaba")

# selamla("deniz") #fonksiyonu çağırmak
# selamla("ali")
# selamla("Ahmet")

# def topla(sayi1,sayi2):
#     print(sayi1+sayi2)

# topla(324,24)
# topla(21,32)

#return: fonksiyonun sonucunun dışarıya "geri verir"
#return olunca fonksiyon biter
#böylece sonucu BİR DEĞİŞKENE KAYITLI KALIR.

# def carp(sayi1,sayi2):
#     return sayi1*sayi2

# #sonucu bir değişkende tutabiliriz

# sonuc = carp(4,5)
# print("Sonuç:", sonuc)

# def gecme_durumu(puan):
#     if puan >= 50:
#         return "Geçti"
#     else:
#         return "Kaldı"
    
# print(gecme_durumu(75))

# def geri_say(sayim):
#     for i in range(sayim,0,-1): 
#         print(i)

# def firlat():
#     print("Fırlatma başarılı")

# geri_say(10)
# firlat()

def mama_ver(mutluluk):
    return mutluluk +1

def kutla(mutluluk):
    print("Mır mır mutluluk seviyesi:", mutluluk)

mutluluk = 0 
tekrar = 3 # sayaç her bir döngüde -1 azalıyor

while tekrar >0:
    mutluluk = mama_ver(mutluluk)
    print("mama verildi. Mutluluk:", mutluluk)
    tekrar = tekrar -1 

kutla(mutluluk)