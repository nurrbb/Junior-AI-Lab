# import time 
# from sklearn.linear_model import LinearRegression
# from sklearn.tree import DecisionTreeClassifier

# #yıl,km,motor hacmi -> fiyat bin tl

# X_fiyat = [[2020, 50000, 1.6], [2015, 120000, 1.4], [2023, 10000, 2.0], [2010, 200000, 1.2], [2018, 80000, 1.5]]
# y_fiyat = [950, 600, 1600, 400, 800]

# #değişen parça, boyalı parça, tramer kaydı(TL) - 0-> kusursuz, 1-> orta has. 2-> ağır has

# X_hasar = [[0, 0, 0], [1, 2, 5000], [3, 5, 45000], [0, 1, 1500], [4, 6, 80000]]
# y_hasar = [0, 1, 2, 0, 2]

# fiyat_botu = LinearRegression().fit(X_fiyat, y_fiyat)
# ekspertiz_botu = DecisionTreeClassifier().fit(X_hasar, y_hasar)

# def oto_ekspertiz_robotu():
#     print(f"\n {'YZ-EKSPERTİZ v2.0 SİSTEMİNE BAĞLANILDI ':=^60}")
    
#     while True:
#         print(">>> ARAÇ BİLGİLERİ: ")
#         yil = int(input(" Üretim yılı: "))
#         km = int(input("Kilometre: "))
#         motor = float(input( "Motor hacmi (örn: 1.6): "))

#         print("\n>>> HASAR SORGULAMASI: ")
#         degisen = int(input("Değişen Parça Sayısı: "))
#         boya = int(input("Boyalı Parça Sayısı: "))
#         tramer = int(input("Tramer Kaydı Toplam (TL): "))

#         print("\n" + "*"*40)
#         print("[sistem] araç dyno testine alınıyor...")
#         time.sleep(1.5)
#         print("[sistem] Kaporta boya mikron değerleri lazele ölçülüyor...")
#         time.sleep(1.5)
#         print("[sistem] Şase numarası veri tabanından sorgulanıyıor")
#         time.sleep(1.5)
#         print("\n" + "*"*40)

#         tahmini_fiyat = fiyat_botu.predict([[yil,km,motor]])[0]
#         hasar_durumu = ekspertiz_botu.predict([[degisen,boya,tramer]])[0]

#         if hasar_durumu == 0:
#             durum_metni = "[KUSURSUZ] -> Bulmuşken kaçırma"
#         elif hasar_durumu == 1:
#             durum_metni = "[ORTA HASARLI] -> Pazarlık masasına otur, fiyatta anlaşırsanız ok."
#         else:
#             durum_metni = "[AĞIR HASARLI] -> Olay yerinden usulca uzaklaş!"
        
#         print("<<< EKSPERTİZ RAPORU >>>")
#         print(f"|Genel Durum: {durum_metni}")
#         print(f"|Adil Piyasa: {tahmini_fiyat:^10.2f} Bin TL")
#         print("="*70)

#         if input("\nSırada başka araç var mı?(evet/hayır): ").lower != 'evet':
#             print("\n[SİSTEM KAPATILIYOR] kazasız sürüşler dileriz...")
#             break
# oto_ekspertiz_robotu()
                  

from sklearn.linear_model import LinearRegression, LogisticRegression
import time

#veri setleri: [sarj,eğim] -> menzil, döngü,ısı -> durum

X_m, y_m = [[100,0], [50,4], [20,2], [80,-3], [10,5]], [400, 150, 60, 380, 15]
X_b, y_b = [[100,30], [1500,45], [500,35], [2500,55], [50,28]], [0, 1, 0, 1, 0]

menzil_ai = LinearRegression().fit(X_m,y_m)
batarya_ai = LogisticRegression().fit(X_b,y_b)

while True:
    print("\n BATARYA VE NAVİGASYON ANALİZİ")
    sarj = float(input("Şarj (%): "))
    egim = float(input("Eğim(-5/+5): "))
    dongu = int (input("Sarj Döngüsü: "))
    isi = float(input("Sıcaklık(c): "))

    print("\n[SİSTEM] Veriler işleniyor...")
    time.sleep(1)

    km = max(0,menzil_ai.predict([[sarj,egim]]))[0]
    risk = batarya_ai.predict([[dongu,isi]])[0]

    durum = "KRİTİK - SERVİS!" if risk == 1 else "OPTİMAL - SORUN YOK"
    print(f"\nTahmini menzil: {km:.0f} km\nSAĞLIK RAPORU: {durum}")

    if input("\nYeni rota girilsin mi?(e/h): ").lower() != 'e':
        print("Sistem kapatıldı");break