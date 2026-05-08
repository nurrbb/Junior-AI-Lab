# import time
# from sklearn.linear_model import LinearRegression, LogisticRegression

# # Gelir Bin TL ve Yaş -> Maksimum Kredi Limiti 
# limit_X = [[30, 25], [80, 45], [120, 50], [45, 30], [200, 60], [50, 28]]
# limit_y = [50000, 250000, 500000, 100000, 1000000, 120000]
# limit_modeli = LinearRegression().fit(limit_X, limit_y)

# # SINIFLANDIRMA: Gecikmiş Borç Sayısı ve Aylık Gider (Bin TL) -> 0: Red, 1: Onay
# risk_X = [[0, 15], [3, 40], [0, 20], [5, 60], [1, 30], [0, 10]]
# risk_y = [1, 0, 1, 0, 1, 1]
# risk_modeli = LogisticRegression().fit(risk_X, risk_y)

# def kredi_onay_sistemi():
#     print(f"\n{' NEO-BANK AKILLI KREDİ SİSTEMİ ':#^60}")
#     while True:
#         print("\n--- Kredi Başvuru Analizi ---")
#         gelir = int(input("Aylık Gelir (Bin TL): "))
#         yas = int(input("Müşteri Yaşı: "))
#         gecikme = int(input("Son 1 Yıldaki Gecikmiş Borç Sayısı: "))
#         gider = int(input("Aylık Ortalama Gider (Bin TL): "))
        
#         print("\n[AI] Kredi risk skoru hesaplanıyor...")
#         time.sleep(1)
        
#         onay_durumu = risk_modeli.predict([[gecikme, gider]])[0]
        
#         if onay_durumu == 1:
#             tahmini_limit = max(0, limit_modeli.predict([[gelir, yas]])[0])
#             print("SONUÇ: [ONAYLANDI] Müşteri düşük riskli.")
#             print(f"SİSTEM ÖNERİSİ MAKSİMUM LİMİT: {tahmini_limit:,.2f} TL")
#         else:
#             print("SONUÇ: [REDDEDİLDİ] Yüksek riskli müşteri profili.")
#             print("SİSTEM ÖNERİSİ: Kredi tahsisi uygun görülmemiştir.")
            
#         if input("\nYeni başvuru yapılsın mı? (e/h): ").lower() != 'e': break

# kredi_onay_sistemi()


