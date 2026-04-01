#Veri manipülasyonu:

#plaka sistemi 01: adana 02: adıyaman .... (label encoding)

# from sklearn.preprocessing import LabelEncoder #kelimeleri --> sayılara çevirir

# sehirler =["İstanbul", "Ankara","İzmir","Bursa"]
# kodlayici = LabelEncoder() # boş bir çevirmen makinesi oluşturduk
# sehir_kodlari = kodlayici.fit_transform(sehirler)
# print(f"Şehir Kodları: {sehir_kodlari} ")

#Oyun karakter sınıfı:
# siniflar =["Savaşçı", "Büyücü", "Okçu", "Şifacı"]
# kodlayici = LabelEncoder()
# sinif_kodlari = kodlayici.fit_transform(siniflar)
# print(f"Karakter Kodları: {sinif_kodlari}")

#hibrit tahminleme

#araba tahmini(fiyat/segment)
# from sklearn.linear_model import LinearRegression, LogisticRegression
# import numpy as np

#motor gücü (HP), yaş

# veriler= [[100,5],[200,2],[80,10],[300,1]]
# fiyat = [500,1200,300,2500]  #fiyatlandırma x1000
# segment = [0,1,0,1] #0: Standart 1: spor

# fiyat_ai = LinearRegression().fit(veriler,fiyat)
# segment_ai = LogisticRegression().fit(veriler,segment)

# beygir = int(input("Beygir gücü?"))
# yas = int(input("Araba kaç yaşında?"))

# yeni_veri = [[beygir,yas]]
# fiyat = fiyat_ai.predict(yeni_veri)
# segment = segment_ai.predict(yeni_veri)
# print(f"Tahmini Fiyat: {fiyat[0]} bin tl")
# print(f"Segment(0: Standart, 1: Spor): {segment[0]}")

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib
import time

emlak_arsivi = {
    'mahalle': [
        'Kadıköy', 'Beşiktaş', 'Esenyurt', 'Kadıköy', 'Beşiktaş', 'Esenyurt', 
        'Şişli', 'Şişli', 'Bakırköy', 'Bakırköy', 'Pendik', 'Pendik',
        'Beşiktaş', 'Kadıköy', 'Şişli', 'Esenyurt', 'Bakırköy', 'Pendik'
    ],
    'oda_sayisi': [2, 3, 1, 3, 4, 2, 3, 1, 2, 4, 1, 3, 5, 1, 2, 3, 2, 4],
    'merkeze_uzaklik': [5, 2, 20, 4, 1, 15, 3, 7, 10, 8, 25, 22, 0.5, 6, 4, 18, 11, 28],
    'gercek_fiyatlar': [
        5000, 8500, 1800, 7200, 13000, 2200, 9000, 4500, 6000, 11000, 2000, 4000,
        18000, 3800, 7500, 2800, 6500, 3500
    ],
    'segment_etiketleri': [1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0] 
    # 1: Lüks, 0: Standart
}

emlak_tablosu = pd.DataFrame(emlak_arsivi)

mah_cevirici = LabelEncoder()
emlak_tablosu['mahalle_id'] = mah_cevirici.fit_transform(emlak_tablosu['mahalle'])

ozellik = emlak_tablosu[['mahalle_id','oda_sayisi','merkeze_uzaklik']]

hedef_fiyat = emlak_tablosu['gercek_fiyatlar']
hedef_segment = emlak_tablosu['segment_etiketleri']

fiyat_ai = LinearRegression()
fiyat_ai.fit(ozellik,hedef_fiyat)

segment_ai = LogisticRegression()
segment_ai.fit(ozellik,hedef_segment)

joblib.dump(fiyat_ai,"fiyat_ai.pkl") #.pkl = pickle 
joblib.dump(segment_ai,"kategori_ai.pkl")
joblib.dump(mah_cevirici,"mahalle_rehberi.pkl")

print(" >>> tüm veriler analiz edildi,modeller kaydedildi <<<")

def emlak_asistani():
    print("-"*40)
    print("     AKILLI EMLAK ASİSTANI    ")
    print("-"*40)

    bilinen_mahalleler = mah_cevirici.classes_
    print(f"Hizmet verdiğim bölgeler: {', '.join(bilinen_mahalleler)}")
    mahalle = input("Mahalle adı: ").capitalize()

    if mahalle in bilinen_mahalleler:
        oda = int(input("Oda: "))
        uzaklik = float(input("Uzaklık(km): "))
        m_id =mah_cevirici.transform([mahalle])[0]
        tahmin_fiyat = fiyat_ai.predict([[m_id,oda,uzaklik]])[0]
        tahmin_seg = segment_ai.predict([[m_id,oda,uzaklik]])[0]

        durum = "LÜKS" if tahmin_seg == 1 else "STANDART"

        print("--- SONUÇ ---")
        print(f"Önerilen Fiyat: {tahmin_fiyat:.2f} TL")
        print(f"Ev Kategorisi: {durum}")

    else:
        print(f"[UYARI]: '{mahalle}' mahallesi verilerimizde bulunamadı")

emlak_asistani()

