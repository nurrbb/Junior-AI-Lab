# from sklearn.linear_model import LinearRegression

# kafe_verileri = [
#     [5, 2, 2], 
#     [20, 5, 2], 
#     [30, 8, 1], 
#     [10, 1, 3], 
#     [15, 4, 2]
# ]

# #hedef değerler
# hazirlanma_sureleri = [6, 12, 25, 4, 10]

# kafe_ai = LinearRegression()
# kafe_ai.fit(kafe_verileri,hazirlanma_sureleri)

# print("---Akıllı Kafe bekleme sistemi")
# print("çıkış yapmak için müşteri sayısına -1 giriniz")

# while True:
#     musteri = int(input("İçerideki müşteri saysı nedir?:"))

#     if musteri == -1:
#         print("sistemde çıkılıyor. iyi günler")
#         break

#     siparis = int(input("Sipariş adedi nedir?: "))
#     barista = int(input("Çalışan barista sayısı nedir?: "))

#     tahmin = kafe_ai.predict([[musteri,siparis,barista]])
#     print(f"Kahveniz yaklaşık {int(tahmin[0])} dakikada hazır olacak" )


# from sklearn.linear_model import LinearRegression as lr
# from sklearn.preprocessing import PolynomialFeatures as pl

# #veri hazırlığı : gün sayısı

# gunler = [ [1] ,[2],[3],[4],[5] ]

# #hedef: vaka sayısı

# vakalar = [2, 4, 8, 16, 32]

# poly = pl(degree=2)  # poly = PolynomialFeatures(degree=2)
# gunler_poly = poly.fit_transform(gunler)

# salgin_ai = lr()
# salgin_ai.fit(gunler_poly,vakalar)

# print("---Salgın Hastalık Vaka Tahmin Sistemi")
# print("Sistemden çıkmak için gün sayısına '0' yazınız \n")
# while True:
#     girdi = float(input("Kaçıncı gündeki vaka sayısını merak ediyorsun?: "))
   
#     if girdi == 0:
#         print("Simülasyon kapatılıyor")
#         break
    
#     tahmin_edilecek_gun = poly.transform([[girdi]])
#     tahmin = salgin_ai.predict(tahmin_edilecek_gun)
#     print(f"\n {int(girdi)}. Gün beklenen ttoplam vaka sayısı {int(tahmin[0])}")

# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures

# # Veri Hazırlığı Karakterin Mevcut Seviyesi
# seviye_verileri = [
#     [1], [5], [10], [15], [20]
# ]
# # Hedef Değerler: [Bir Sonraki Seviye İçin Gereken XP Puanı]
# xp_verileri = [100, 1500, 8000, 25000, 60000]

# poly = PolynomialFeatures(degree=3) 
# seviye_poly = poly.fit_transform(seviye_verileri)

# oyun_ai = LinearRegression()
# oyun_ai.fit(seviye_poly, xp_verileri)

# print("--- Oyun İçi XP Dengeleme Yapay Zekası ---")
# print("Çıkış yapmak için Seviye olarak '0' giriniz.\n")

# while True:
#     level = float(input("Karakterinizin seviyesini giriniz: "))
#     if level == 0:
#         print("Sistemden çıkılıyor.")
#         break
        
#     level_cevrilmis = poly.transform([[level]])
#     tahmin = oyun_ai.predict(level_cevrilmis)
    
#     print(f"\n>>> {int(level)}. Seviyeden bir sonrakine geçmek için gereken XP: {int(tahmin[0])} Puan\n")

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

seviye_verileri = [ [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
maas_verileri = [  17000, 20000, 25000, 35000, 50000,75000, 110000, 160000, 250000, 400000]

poly= PolynomialFeatures(degree=3)
seviye_poly = poly.fit_transform(seviye_verileri)
ik_ai = LinearRegression()
ik_ai.fit(seviye_poly,maas_verileri)

while True:
    seviye= float(input("Maaşı tahmin edilecek çalışnaın seviyesi 1-10 arası nedir?: "))
    if seviye == 0:
        print("Sistemden çıkılıyor")
        break
    
    seviye_cevrilmis = poly.transform([[seviye]])
    tahmin = ik_ai.predict(seviye_cevrilmis)
    print(f"\n >>> Bu seviye için yapay zekanın önerdiği maaş: {int(tahmin[0]):,} TL \n")