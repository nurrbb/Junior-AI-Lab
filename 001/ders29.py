# from sklearn.linear_model import LinearRegression, LogisticRegression

# spor_X = [[1, 2, 1], [1.5, 1.8, 1.2], [8, 10, 9], [7, 12, 11], [3, 5, 15], [4, 6, 18]]
# spor_y = [0, 0, 1, 1, 2, 2] # 0: Yürüyor, 1: Koşuyor, 2: Bisiklet
# spor_siniflandirici = LogisticRegression().fit(spor_X, spor_y)

# # [Ortalama Kalp Ritmi, Süre] -> Yakılan Kalori
# kalori_X = [[80, 30], [100, 60], [150, 45], [170, 30], [120, 20]]
# kalori_y = [150, 400, 550, 500, 200]
# kalori_tahminci = LinearRegression().fit(kalori_X, kalori_y)

# def spor_asistani():
#     print(f"\n{' AKTİF YAŞAM ASİSTANI BAŞLATILDI ':#^60}")
    
#     while True:
#         print("\n--- Sensör Verileri Okunuyor ---")
#         x = float(input("X Ekseni İvme (0-20): "))
#         y = float(input("Y Ekseni İvme (0-20): "))
#         z = float(input("Z Ekseni İvme (0-20): "))
        
#         hareket_tahmini = spor_siniflandirici.predict([[x, y, z]])[0]
#         spor_turleri = {0: "Yürüyor", 1: "Koşuyor", 2: "Bisiklet Sürme"}
#         su_an_yapilan = spor_turleri[hareket_tahmini]
        
#         print(f"[BİLGİ] Algılanan Aktivite: {su_an_yapilan}")
        
#         nabiz = int(input("Anlık Kalp Ritmi (BPM): "))
#         sure = int(input("Aktivite Süresi (Dakika): "))
        
#         # Kalori tahmini yap
#         yakilan_kalori = kalori_tahminci.predict([[nabiz, sure]])[0]
        
#         print("\n" + "-"*30)
#         print(f"SONUÇ: {su_an_yapilan} modunda {sure} dakikada yaklaşık {yakilan_kalori:.1f} kalori yaktınız.")
#         print("-"*30)
        
#         if input("Yeni analiz yapılsın mı? (e/h): ").lower() != 'e': break

# spor_asistani()

from sklearn.linear_model import LinearRegression, LogisticRegression
# Hareket 0/1, CO2 Seviyesi - 0: Boş/Uyku, 1: Dolu/Aktif
ev_durum_X = [[0, 400], [0, 450], [1, 800], [1, 1200], [0, 500]]
ev_durum_y = [0, 0, 1, 1, 0]
ev_sinif_ai = LogisticRegression().fit(ev_durum_X, ev_durum_y)

#Dış Sıcaklık, Kişi Sayısı -> İdeal İç Sıcaklık
iklim_X = [[35, 4], [30, 2], [25, 1], [10, 3], [0, 2]]
iklim_y = [21, 22, 24, 23, 24]
iklim_reg_ai = LinearRegression().fit(iklim_X, iklim_y)

def akilli_ev_yonetimi():
    print(" SMART-HOME İKLİMLENDİRME SİSTEMİ ")
    
    while True:
        hareket = int(input("Hareket Var mı? (1Evet 0Hayır): "))
        co2 = int(input("CO2 Seviyesi (ppm): "))
        
        durum = ev_sinif_ai.predict([[hareket, co2]])[0]
        
        if durum == 0:
            print("\n[SİSTEM] Ev boş veya herkes uyuyor. Klima 'Ekonomik/Uyku' moduna alındı.")
        else:
            print("\n[SİSTEM] Evde yaşam algılandı. İdeal sıcaklık hesaplanıyor...")
            dis_isi = float(input("Dış ortam sıcaklığı : "))
            kisi = int(input("Evdeki kişi sayısı: "))
            
            ideal_isi = iklim_reg_ai.predict([[dis_isi, kisi]])[0]
            print(f">>> Klima Hedef Sıcaklığı: {ideal_isi:.1f} olarak ayarlandı.")
            
        if input("\nGüncelleme yapılsın mı? (e/h): ").lower() != 'e': break
akilli_ev_yonetimi()