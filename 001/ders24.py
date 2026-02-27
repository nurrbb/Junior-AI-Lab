import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.tree import DecisionTreeClassifier

veri_reg = {
    'sicaklik': [20, 25, 30, 35, 10, 15, 5, 0],
    'nem': [30, 40, 50, 60, 20, 25, 15, 10],
    'hissedilen': [19, 26, 32, 40, 8, 14, 4, -2]
}
df_reg = pd.DataFrame(veri_reg)

veri_sinif = {
    'hava_durumu': [0, 0, 1, 2, 2, 1, 0, 2],
    'ruzgar': [0, 1, 0, 0, 1, 1, 0, 1],
    'uygunluk': [1, 1, 1, 0, 0, 1, 1, 0]     
}
df_tree = pd.DataFrame(veri_sinif)


veriler = df_reg[['sicaklik','nem']]
sonuc = df_reg['hissedilen']
tahmin_ai = LinearRegression()
tahmin_ai.fit(veriler, sonuc)

veriler2 = df_tree[['hava_durumu', 'ruzgar']]
sonuc2 = df_tree['uygunluk']
karar_ai = DecisionTreeClassifier()
karar_ai.fit(veriler2, sonuc2)

def hava_durumu_tahmin_et(sicaklik, nem):
    yeni_veri = pd.DataFrame([[sicaklik, nem]], columns=['sicaklik', 'nem'])
    tahmin = tahmin_ai.predict(yeni_veri)
    return tahmin[0]

def etkinlik_oneri(hava_tipi, ruzgar_durumu):
    yeni_veri_karar = pd.DataFrame([[hava_tipi, ruzgar_durumu]], columns=['hava_durumu', 'ruzgar'])
    tahmin = karar_ai.predict(yeni_veri_karar)
    
    if tahmin[0] == 1:
        return "DIŞARI ÇIKMAK İÇİN HARİKA BİR GÜN"
    else:
        return "EVDE KALIP ETKİNLİK YAPMAK DAHA İYİ OLABİLİR"

#  ANA PROGRAM
print("--- AI DESTEKLİ HAVA ANALİZ SİSTEMİNE HOŞ GELDİNİZ ---")

devam_etsin_mi = "evet"

while devam_etsin_mi == "evet":
    print("\nLütfen güncel verileri giriniz: ")

    sicaklik = float(input("Hava sıcaklığı kaç derece?: "))
    nem = float(input("Nem oranı yüzde kaç? (ör 45): "))

    hissedilen = hava_durumu_tahmin_et(sicaklik, nem)

    print("-" * 50)
    print(f"AI analizi: Bugün hava {sicaklik} derece ama nemle birlikte {hissedilen:.1f} derecedir")
    print("Etkinlik planı için ek bilgi: ")

    print("Hava nasıl? (0: güneşli, 1: bulutlu, 2: yağmurlu)")
    hava = int(input("Seçiminiz: "))
    print("Rüzgar var mı? (0: hayır az, 1: evet/çok)")
    ruzgar = int(input("Seçiminiz: "))
    
    sonuc_tavsiye = etkinlik_oneri(hava, ruzgar)
    print(f"AI Tavsiye: {sonuc_tavsiye}")
    print("-" * 50)
    
    devam_etsin_mi = input("Başka bir tahmin yapmak ister misiniz? (evet/hayır): ").lower()

print("\nProgram kapatılıyor. İyi günler!")