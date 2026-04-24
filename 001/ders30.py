# import time
# from sklearn.linear_model import LinearRegression, LogisticRegression

# #Yaş, VKİ, Kronik Hastalık (0:Yok, 1:Var) -> Tahmini Yıllık Harcama (TL)
# maliyet_X = [[25, 22.5, 0], [45, 28.0, 1], [60, 31.5, 1], [30, 24.0, 0], [55, 29.0, 0], [70, 35.0, 1]]
# maliyet_y = [5000, 25000, 45000, 7000, 18000, 60000]
# maliyet_modeli = LinearRegression().fit(maliyet_X, maliyet_y)

# # Kolesterol, Sigara (0:İçmiyor, 1:İçiyor -> 0: Düşük Risk, 1: Yüksek Risk
# risk_X = [[180, 0], [250, 1], [210, 0], [280, 1], [190, 1], [160, 0]]
# risk_y = [0, 1, 0, 1, 1, 0]
# risk_modeli = LogisticRegression().fit(risk_X, risk_y)

# def sigorta_analiz_sistemi():
#     print(f"\n{' AKTİF SİGORTA YAPAY ZEKA ASİSTANI ':#^60}")
    
#     while True:
#         print("\n--- Müşteri Veri Girişi ---")
        
#         while True:
#             yas = int(input("Müşterinin Yaşı (18-100): "))
#             if 18 <= yas <= 100: break
#             print("Hata: Lütfen geçerli bir yaş giriniz.")
            
#         while True:
#             vki = float(input("Vücut Kitle İndeksi (VKİ) (15-50): "))
#             if 15 <= vki <= 50: break
#             print("Hata: VKİ 15 ile 50 arasında olmalıdır.")
            
#         kronik = int(input("Kronik Rahatsızlık Var mı? (0: Hayır, 1: Evet): "))
#         kolesterol = int(input("Kolesterol Seviyesi (100-400): "))
#         sigara = int(input("Sigara Kullanımı (0: Hayır, 1: Evet): "))
        
#         print("\n[AI] Veriler işleniyor, poliçe hesaplanıyor...")
#         time.sleep(1.5)
        
#         tahmini_harcama = max(0, maliyet_modeli.predict([[yas, vki, kronik]])[0])
#         risk_durumu = risk_modeli.predict([[kolesterol, sigara]])[0]
        
#         print("\n" + "="*45)
#         print(f"TAHMİNİ YILLIK SAĞLIK HARCAMASI: {tahmini_harcama:,.2f} TL") #binleri ayırıyo 1,000.66
#         if risk_durumu == 1:
#             print("RİSK GRUBU: [!] YÜKSEK RİSKLİ MÜŞTERİ")
#             print("SİSTEM ÖNERİSİ: Poliçe primine %25 risk sürprimi ekleyiniz.")
#         else:
#             print("RİSK GRUBU: [OK] Düşük Riskli Müşteri")
#             print("SİSTEM ÖNERİSİ: Standart tarife uygulanabilir.")
#         print("="*45)
        
#         if input("\nYeni müşteri analizi yapılsın mı? (e/h): ").lower() != 'e': 
#             print("Sistemden çıkılıyor...")
#             break

# sigorta_analiz_sistemi()

import time
from sklearn.linear_model import LinearRegression, LogisticRegression

#MODEL: Regresyon (
# Veri: [Saat (0-23), Mevsim (1:Kış,2:İlkb,3:Yaz,4:Sonb), Salgın (0:Yok, 1:Var)] -> Gelecek Hasta Sayısı
yogunluk_X = [[2, 1, 1], [14, 3, 0], [20, 1, 1], [9, 2, 0], [23, 4, 1], [5, 3, 0]]
yogunluk_y = [45, 15, 80, 25, 60, 5]
yogunluk_modeli = LinearRegression().fit(yogunluk_X, yogunluk_y)

# Sınıflandırma
# Veri: [Nabız, Ateş, Tansiyon] -> 0: Yeşil Alan, 1: Sarı Alan, 2: Kırmızı Alan
triyaj_X = [[75, 36.5, 120], [130, 39.5, 90], [95, 37.8, 140], [150, 35.0, 70], [80, 37.0, 115]]
triyaj_y = [0, 2, 1, 2, 0]
triyaj_modeli = LogisticRegression(max_iter=1000).fit(triyaj_X, triyaj_y)

def acil_servis_yonetimi():
    print(f"\n{' SMART-ER ACİL SERVİS YÖNETİM SİSTEMİ ':#^60}")
    
    while True:
        islem = input("\n[1] Yoğunluk Tahmini\n[2] Hasta Triyajı\nSeçiminiz (1/2): ")
        
        if islem == '1':
            print("\n--- Acil Servis Kapasite Planlama ---")
            saat = int(input("Bulunulan Saat (0-23): "))
            mevsim = int(input("Mevsim (1:Kış, 2:İlkbahar, 3:Yaz, 4:Sonbahar): "))
            salgin = int(input("Bölgede Salgın/Pandemi var mı? (0:Hayır, 1:Evet): "))
            
            tahmini_hasta = yogunluk_modeli.predict([[saat, mevsim, salgin]])[0]
            print(f"\n>>> [AI BEKLENTİSİ] Önümüzdeki 1 saat içinde acil servise yaklaşık {int(tahmini_hasta)} hasta girişi beklenmektedir.")
            if tahmini_hasta > 50:
                print(">>> [ALARM] Yoğunluk kapasite sınırında! Yedek doktor çağrılması önerilir.")
                
        elif islem == '2':
            print("\n--- Anlık Hasta Triyajı ---")
            nabiz = int(input("Hastanın Nabzı (BPM): "))
            ates = float(input("Hastanın Ateşi (°C): "))
            tansiyon = int(input("Sistolik Tansiyon (Büyük Tansiyon): "))
            
            print("\n[SİSTEM] Vitaller analiz ediliyor...")
            time.sleep(1)
            
            durum = triyaj_modeli.predict([[nabiz, ates, tansiyon]])[0]
            
            print("-" * 40)
            if durum == 0:
                print("TRİYAJ SONUCU: [YEŞİL ALAN] - Ayakta tedavi, aciliyeti yok.")
            elif durum == 1:
                print("TRİYAJ SONUCU: [SARI ALAN] - Müşahade gerekli, stabil değil.")
            else:
                print("TRİYAJ SONUCU: [KIRMIZI ALAN] - KRİTİK! Derhal müdahale odasına alın.")
            print("-" * 40)
            
        else:
            print("Hatalı seçim yaptınız.")
            
        if input("\nSistemi kullanmaya devam etmek istiyor musunuz? (e/h): ").lower() != 'e': break

acil_servis_yonetimi()