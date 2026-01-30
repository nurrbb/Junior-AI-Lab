# #Hava durumu robotu

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# #nem arttıkça sıcaklığın düştüğü bir senaryo üzerine konuşuyoruz
# nem_verisi = np.array([20, 35, 50, 65, 80, 95]).reshape(-1,1)
# sicaklik_verisi = np.array([25, 30, 25, 18, 12, 5])

# meteorolog_ai = LinearRegression()
# meteorolog_ai.fit(nem_verisi,sicaklik_verisi)

# print("--- AI METEOROLOG SİSTEMİ ---")
# gelen_nem = float(input("Şu an nem yüzde kaç? (0-100): "))
# tahmin_derece = meteorolog_ai.predict([[gelen_nem]])[0]

# print(f"AI Tahmini: Hava yaklaşık {tahmin_derece:.1f} derece olacak")

# if tahmin_derece > 25:
#     print("Tavsiye:  Güneş gözlüğünü unutma hava çok sıcak.")
# elif tahmin_derece >15:
#     print("Tavsiye: Hafif bir hırka yeterli")
# else:
#     print("Tavsiye: kalın montunu giy, zira hasta olabilirsin!")

# kisi_sayisi = np.array([1, 3, 5, 8, 12, 15, 20]).reshape(-1,1)
# bekleme_suresi = np.array([2, 5, 9, 1, 22, 28, 48])

# kantin_sefi = LinearRegression()
# kantin_sefi.fit(kisi_sayisi,bekleme_suresi)

# print("---KANTİN SIRA ASİSTANI ---")
# sira = int(input("Önünde kaç kişi sıra bekliyor? "))
# sure_tahmini = kantin_sefi.predict([[sira]])[0]

# print(f"Robot Tahmini: Tostuna kavuşmana {int(sure_tahmini)} dakika var!")
# if sure_tahmini > 15:
#     print("Uyarı: Sıra çok uzun, o sırada biraz oyun oynayabilirsin!")
# else:
#     print("Uyarı: Sıradan ayrılma, neredeyse sıra sende! ")

saniye = np.array([[1],[5],[10],[20]])
yol = np.array([100, 500, 1000, 2000])

kahraman_ai = LinearRegression()
kahraman_ai.fit(saniye,yol)

print("--- Süper Kahraman Radarı ---")
sn = float(input("Kahraman kaç saniye boyunca koştu?"))
tahmin_yol = kahraman_ai.predict([[sn]])[0]
print(f"Vay Canına! Kahramanımız tam {tahmin_yol/1000:.1f} km/yol kat etti!")