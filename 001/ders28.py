# import time 
# from sklearn.linear_model import LinearRegression, LogisticRegression
# #saat(0-23), bant hızı(0-100), çalışan makine sayısı -> tüketim (kwh)
# enerji_X = [[8, 20, 5], [10, 80, 15], [14, 100, 20], [18, 50, 10], [22, 10, 2], [3, 5, 1]]
# enerji_y = [200, 850, 1200, 550, 150, 50]
# enerji_model = LinearRegression().fit(enerji_X,enerji_y)
# # trafo ısısı, anlık yük(%lik),nem -> (0: stabil, 1 tehlike)
# sebeke_X = [[40, 50, 30], [85, 95, 60], [65, 75, 45], [92, 99, 70], [45, 40, 35]]
# sebeke_y = [0, 1, 0, 1, 0]
# sebeke_model = LogisticRegression().fit(sebeke_X,sebeke_y)

# def enerji_hesapla(saat,hiz,makine):
#     tahmin = enerji_model.predict([[saat,hiz,makine]])[0]
#     return max(0,tahmin)

# def maliyet_analizi(kwh):
#     birim_fiyat = 3.45
#     return kwh*birim_fiyat

# def smart_grid_sistemi():
#     print(f"\n{' SMARTGRID-X ENERJİ YÖNETİM SİSTEMİ ':#^60}")
#     while True:
#         print("\n --- Yeni Veri Girişi (LÜTFEN İSTENİLEN ARALIK DIŞINA ÇIKMAYINIZ) ---")
       
#         while True:
#             st = int(input("Günün Saati(0-23): "))
#             if st >= 0 and st <= 23:
#                 break
#             print("Hatalı giriş! Saat 0 ile 23 arasında olmalıdır.")
        
#         while True:
#             hz = int(input("Üretim Hattı Hızı(0-100): "))
#             if hz >= 0 and hz <= 100:
#                 break
#             print("Hatalı giriş! Hız 0 ile 100 arasında olmalıdır.")
        
#         while True:
#             ms = int(input("Aktif makine sayısı(0-50): "))
#             if ms >= 0 and ms <= 50:
#                 break
#             print("Hatalı giriş makine sayısı 0 ile 50 arasında olmalıdır. ")  

#         while True:
#             sicaklik = float(input("Trafo Isısı(0-120): "))
#             if sicaklik >= 0 and sicaklik <=120:
#                 break
#             print("Hatalı giriş! Isı 0 ile 120 arasında olmalıdır.")

#         while True:
#             yuk = int(input("Şebeke yüklenmesi(0-100 %): "))
#             if yuk >= 0 and yuk <= 100:
#                 break 
#             print("Hatalı giriş! Yük 0 ile 100 arasında olmalıdır")
        
#         tuketim = enerji_hesapla(st,hz,ms)
#         maliyet = maliyet_analizi(tuketim)
#         risk = sebeke_model.predict([[sicaklik,yuk,40]])[0]
#         print("\n [AI ANALİZİ YÜRÜTÜLÜYOR...]")
#         time.sleep(1.5)
#         print("-" * 40)
#         print(f"| Beklenen Tüketim: {tuketim:.2f} KWh")
#         print(f"| Tahmini Maliyet: {maliyet:.2f} TL")

#         if risk == 1:
#             print(f"| ŞEBEKE ALARMI: [!] Trafo soğutma sistemlerini açın.")
#         else:
#             print(f"| ŞEBEKE ALARMI: [OK] Stabil çalışma.")
#         print("-"*40)
#         secim = input("Veri girişine devam mı? (e/h): ").lower()
#         if secim == 'h':
#             print("Sistemden çıkılıyor...")
#             break
# smart_grid_sistemi()

from sklearn.linear_model import LinearRegression, LogisticRegression

verim_ai = LinearRegression().fit([[98,45,6], [85,60,8], [70,75,10], [95,42,5], [60,80,12]], [1000,750,400,1050,200])
kalite_ai = LogisticRegression().fit([[0.1,0.01], [0.8,0.5], [0.2,0.05], [0.9,0.7], [0.3,0.1]], [0,1,0,1,0])

def fabrika_yonetimi():
    print(f"\n{' ÜRETİM TAKİP SİSTEMİ ':=^40}")
    while True:
        saflik = float(input("Hammadde Saflığı (0-100): "))
        if 0 <= saflik <= 100: break
        print("Hata: Değer 0-100 arasında olmalı!")

    while True:
        isi = float(input("Makine Isısı (20-150): "))
        if 20 <= isi <= 150: break
        print("Hata: Isı 20-150 arasında olmalı!")

    while True:
        basinc = float(input("Hat Basıncı (1-20): "))
        if 1 <= basinc <= 20: break
        print("Hata: Basınç 1-20 arasında olmalı!")

    tahmin = max(0, verim_ai.predict([[saflik, isi, basinc]])[0])

    # Kullanıcıdan kalite testi için de input alalım 
    while True:
        kusur = float(input("Ürün Kusur Skoru (0.0 - 1.0): "))
        if 0 <= kusur <= 1: break
        print("Hata: Skor 0 ile 1 arasında olmalı!")
    durum = kalite_ai.predict([[kusur, 0.05]])[0] # Sapma sabit 0.05 alındı

    print("\n" + "-"*40)
    print(f"| Beklenen Üretim: {int(tahmin)} Adet")
    print(f"| Kalite Sonucu  : {' SAĞLAM' if durum == 0 else ' KUSURLU'}")
    print("-"*40)

fabrika_yonetimi()