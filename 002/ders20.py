# #airbnb --> ev kiralama sistemi

# import numpy as np
# from sklearn.linear_model import LinearRegression, LogisticRegression
# from sklearn import tree

# # veri setleri 
# #lineer regresyon -> fiyatlandırma verisi
# #özellikler : m2,merkeze uzaklık(km), oda sayısı, klima(1/0)

# emlak = np.array([ [40, 1, 1, 1], [45, 1.5, 1, 0], [120, 8, 3, 1],
#                    [85, 4, 2, 1], [30, 0.5, 1, 1], [200, 15, 5, 1], 
#                    [70, 6, 2, 0], [150, 10, 4, 1], [55, 3, 1, 0], 
#                    [95, 5, 2, 1], [110, 7, 3, 1], [35, 2, 1, 0] ])

# #hedef -> fiyat
# fiyat = np.array([1100, 950, 2400, 1900, 1300, 4800, 1400, 3600, 1050, 2100, 2500, 800])

# # tree -> kategori  verisi
# #havuz(1/0), bahçe m2, lüks mutfak(1/0)

# kategori = [
#     [1, 150, 1], [0, 0, 0], [0, 50, 1], [1, 80, 1],
#     [0, 5, 0], [1, 300, 1], [0, 20, 0], [1, 120, 0]
# ]

# #sonuçlar 0: standart 1: doğa evi 2:ultra lüks 

# kategori_sonuc = [2,0,1,2,0,2,0,1]

# #güvenlik verisi -> lojistik regresyon 
# #özelliikler: kullanıcı puanı(1-5), önceki iptal sayısı,doğrulanmış profil(1/0)

# misafir = np.array([
#     [4.9, 0, 1], [2.1, 5, 0], [4.5, 1, 1], [3.0, 2, 0],
#     [4.8, 0, 1], [1.5, 8, 0], [3.5, 1, 1], [5.0, 0, 1]
# ])

# #1: onaylıyoruz 0: reddet (yüksek risk)

# onay =[1,0,1,0,1,0,1,1]

# #modellerin eğitilmesi

# fiyat_ai = LinearRegression().fit(emlak,fiyat)
# kategori_ai = tree.DecisionTreeClassifier().fit(kategori,kategori_sonuc)
# guvenlik_ai = LogisticRegression().fit(misafir, onay)

# #uygulama

# def nomad_ai():
#     print("*"*40)
#     print("Nomad ai yönetim paneli")
#     print("*"*40)

#     print("Ev bilgilerini giriniz:")
#     m2 = float(input("Metrekare: "))
#     uzaklik = float(input("Merkeze uzaklığı km cinsinden giriniz: "))
#     oda = int(input("Oda sayısı: "))
#     klima = int(input("Klima mevcutsa 1 e yoksa 0 a basınız: "))

#     print("Ek özellikler")
#     havuz = int(input("Havuz(var=1 yok=0): "))
#     bahce = int(input("Bahçe büyüklüğü(m2): "))
#     mutfak = int(input("Lüks mutfak (var=1 yok=0): "))

#     tahmin_fiyat = fiyat_ai.predict([[m2,uzaklik,oda,klima]])[0]
#     tahmin_tip_id = kategori_ai.predict([[havuz,bahce,mutfak]])[0]

#     tipler = {0: "Standart Şehir dairesi", 1: "Huzurlu Doğa Evi",2:"Lüks villa"}

#     print("Analiz sonucu:")
#     print(f"Mülk kategorisi: {tipler[tahmin_tip_id]}")
#     print(f"Belirlenen fiyat: {round(tahmin_fiyat,2)}")

# def misafir_denetim():
#     print("-"*50)
#     print("REZERVASYON GÜVENLİK KONTROLÜ")
#     puan= float(input("Misafir Puanı(1-5): "))
#     iptal= int(input("Geçmiş İptal sayısı: "))
#     onay = int(input("Profil doğrulanmış mı(1: evet, 0:hayır): "))

#     karar = guvenlik_ai.predict([[puan,iptal,onay]])[0]

#     print("GÜVENLİK RAPORU")
#     if karar == 1:
#         print("Durum onaylandı")
#         print("Misafir güvenilir gözüküyor, anahtarı teslim edebilirsiniz")
#     else:
#         print(f"Durum reddedildi")
#         print("Uyarı: Bu misafir yüksek risk taşıyor")
#     print("-"*50) 

# misafir_denetim()

#hibrit ai çalışmaları:

#Ödül avcısı (bounty) hesaplayıcı

from sklearn.linear_model import LinearRegression, LogisticRegression

#suç puanı -> ödül(bin $)

veriler = [[10],[50],[100],[200]]
odul = [5,25,60,150]
model1 = LinearRegression().fit(veriler,odul)

#veriler mesafe, zırh seviyesi ; 1- başarılı 0 ölümcül risk

veriler2 = [[5,2],[50,10],[10,8],[100,1]]
basari = [1,1,1,0]
model2 = LogisticRegression().fit(veriler2,basari)

print("Night City Ödül Hesaplayıcı")
suc = int(input("Hedefin suç puanı (1-200): "))
zırh = int(input("Senin zırh seviyen(1-10): "))


odul = model1.predict([[suc]])[0]
risk = model2.predict_proba([[suc/2,zırh]])[0][1]

print(f"Brüt Ödül: {odul:.2f} bin $. Başarı Şansın: % {risk*100:.1f}")
