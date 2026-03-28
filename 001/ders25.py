#f-string (formatted string literals): değişkenleri metin içe gömüyor

# yas = 25

# print("yas", yas)

# print(f"yas {yas}")

# #sayı biçimlendirme 436.274230

# maas = 23452.3274

# print(f"Net maaş {maas: .2f}")

# meyve = "Elma"

# print(f"|{meyve:<10}|") #<x  10 karakter sola yasla
# print(f"|{meyve:>10}|") # sağa yaslar
# print(f"|{meyve:^10}|") #ortala

# print(f"{meyve:-^30}")

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

#====================================
#Proje 1: E-Ticaret Müşteri Davranışı
#====================================

# veri_satis = { 
#     'fiyat': [100, 150, 200, 250, 300, 350, 400, 500],
#     'indirim_orani': [10, 20, 5, 15, 30, 10, 40, 5],
#     'satis_adedi': [50, 75, 30, 45, 110, 40, 150, 20]
# }

# df_satis = pd.DataFrame(veri_satis)

# model_satis = LinearRegression().fit(df_satis[['fiyat','indirim_orani']], df_satis['satis_adedi'])

# veri_iade = {
#     'yas': [25, 45, 18, 35, 50, 22, 30, 40],
#     'kategori_id': [0, 1, 1, 0, 1, 0, 1, 0], # 0:Elektronik, 1:Giyim
#     'iade_eder_mi': [0, 1, 1, 0, 1, 0, 0, 0] # 0:Hayır, 1:Evet
# }
# df_iade = pd.DataFrame(veri_iade)

# model_iade = LogisticRegression().fit(df_iade[['yas','kategori_id']], df_iade['iade_eder_mi'])

# def eticaret():
#     print("Proje 1: E-Ticaret Analiz Paneli")

#     fiyat = float(input("Ürün fiyatını giriniz (TL): "))
#     indirim = float(input("Uygulanacak indirim oranı (%): "))

#     input_df = pd.DataFrame([[fiyat, indirim]], columns=['fiyat', 'indirim_orani'])
#     tahmin_adet = model_satis.predict(input_df)[0]

#     yas = int(input("Müşteri yaşı: "))
#     kat = input("Kategori (Elektronik/Giyim): ").strip().title() 
#     kat_id = 0 if kat == "Elektronik" else 1

#     input_iade = pd.DataFrame([[yas, kat_id]], columns=['yas', 'kategori_id'])
#     tahmin_iade = model_iade.predict(input_iade)[0]

#     print("-" * 50)
#     print(f"Sonuç: Bu şartlarda tahmini {round(tahmin_adet)} adet satış bekleniyor")
#     print(f"İADE RİSKİ: {'Yüksek(Dikkat!)' if tahmin_iade == 1 else 'Düşük'}")

# eticaret()
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier

# Stok Modeli
df_stok = pd.DataFrame({
    'gecmis': [50, 60, 100, 40, 90, 30],
    'hava': [0, 0, 1, 1, 0, 1], # 0:Güneş, 1:Yağmur
    'talep': [55, 62, 115, 42, 95, 35]
})

ai_stok = LinearRegression().fit(df_stok[['gecmis', 'hava']].values, df_stok['talep'])

# Risk Modeli
df_risk = pd.DataFrame({
    'gun': [1, 2, 5, 1, 3],
    'isi': [4, 8, 15, 20, 25],
    'durum': [0, 0, 1, 1, 1] # 0:Taze, 1:Bozuk
})
ai_risk = DecisionTreeClassifier().fit(df_risk[['gun', 'isi']].values, df_risk['durum'])

print("--- MARKET ANALİZ SİSTEMİ ---")

while True:
    print("\n[STOK TAHMİNİ]")
    dun = float(input("Dünkü satış (kg): "))
    hava = int(input("Hava (0:Güneş, 1:Yağmur): "))
    
    tahmin_kg = ai_stok.predict([[dun, hava]])[0]
    print(f">> Öneri: {tahmin_kg:.1f} kg ürün hazırla.")

    print("\n[RİSK ANALİZİ]")
    gun = int(input("Rafta kaçıncı günü?: "))
    isi = float(input("Sıcaklık: "))
    
    risk = ai_risk.predict([[gun, isi]])[0]
    print(f">> Durum: {'İMHA ET!' if risk == 1 else 'TAZE'}")

    if input("\nDevam? (e/h): ").lower() != 'e': break

print("Güle güle!")