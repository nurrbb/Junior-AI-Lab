# import time
# from sklearn.linear_model import LinearRegression
# from sklearn.tree import DecisionTreeClassifier

# #yıl,km,motor hacmi -> fiyat bin tl
# X_fiyat = [[2020, 50000, 1.6], [2015, 120000, 1.4], [2023, 10000, 2.0], [2010, 200000, 1.2], [2018, 80000, 1.5]]
# y_fiyat = [950, 600, 1600, 400, 800]

# #değişen parça, boyalı parça, tramer kaydı -> durum (0- kusursuz, 1 orta hasarlı, 2 ağır hasarlı)
# X_hasar = [[0, 0, 0], [1, 2, 5000], [3, 5, 45000], [0, 1, 1500], [4, 6, 80000]]
# y_hasar = [0, 1, 2, 0, 2]

# fiyat_botu = LinearRegression(). fit(X_fiyat,y_fiyat)
# ekspertiz_botu = DecisionTreeClassifier().fit(X_hasar,y_hasar)

# def oto_ekspertiz_robotu():
#     print(f"\n{'AI-EKSPERTİZ SİSTEME BAĞLANTI TAMAMLANDI ':=^60}")
    
#     while True:

#         print(">>> ARAÇ BİLGİLERİ <<<")
#         yil = int(input(" ÜRETİM YILI: "))
#         km =  int(input(" KİLOMETRE: "))
#         motor = float (input(" MOTOR HACMİ: "))

#         print("\n>>> HASAR SORGULAMASI <<<")
#         degisen = int(input(" DEĞİŞEN PARÇA SAYISI: "))
#         boya = int(input(" BOYALI PARÇA SAYISI: "))
#         tramer = int(input(" TRAMER KAYDI TOPLAM(TL): "))

#         print("\n" + "*" * 50 )
#         print("[sistem] Araç dyno testine alınıyor...")
#         time.sleep(1.5)
#         print("[sistem] Kaporta mikron değerleri ölçülüyor...")
#         time.sleep(1.5)
#         print("[sistem] Şase numarası veri tabanından sorgulanıyor...")
#         time.sleep(1.5)
#         print("\n"  + "*" * 50)

#         tahmini_fiyat = fiyat_botu.predict([[yil,km,motor]])[0]
#         hasar_durumu = ekspertiz_botu.predict([[degisen,boya,tramer]])[0]

#         if hasar_durumu == 0:
#             durum_metni = "[KUSURSUZ ] -> Bulmuşken kaçırma, hemen notere gidin"
#         elif hasar_durumu == 1:
#             durum_metni = "[ORTA HASARLI] -> Pazarlık gerekli, fiyatta düşülürse okey."
#         else:
#             durum_metni = "[AĞIR HASARLI] -> Olay yerinden uzaklaşmanı tavsiye ederim."

#         print("<<< EKSPERTİZ RAPORU >>>")
#         print(f"| Genel Durum: {durum_metni}")
#         print(f"| Adil Piyasa: {tahmini_fiyat:^10.2f} BİN TL")
#         print("="*50)

#         if input("\nSırada başka araç var mı?(evet/hayır): ").lower() == 'hayır':
#             print("\n[Sistem kapatılıyor] Kazasız sürüşler...")
#             break

# oto_ekspertiz_robotu()



# from sklearn.linear_model import LinearRegression
# from sklearn.tree import DecisionTreeClassifier
# import time


# #trafik yoğunlu(1-10), yolcu sayısı -> durağa varış süresi(dk)
# X_sure = [[2, 10], [8, 45], [5, 25], [10, 60], [1, 5]]
# y_sure = [5, 25, 12, 40, 2]

# #hava durumu(1-5), kaza raporu(0:yok 1: var) -> sefer durumu(0: zamanında, 1: gecikmeli, 2: iptal)
# X_sefer = [[1, 0], [3, 1], [5, 1], [2, 0], [4, 0]]
# y_sefer = [0, 1, 2, 0, 1]

# sure_ai = LinearRegression().fit(X_sure,y_sure)
# sefer_ai = DecisionTreeClassifier().fit(X_sefer,y_sefer)

# def akilli_radar():
#     print(f"\n{'AKILLI FİLO RADARI':#^50}")

#     while True:
#         print("\n[VERİ GİRİŞİ BEKLENİYOR]")
#         trafik = int(input(">Radardaki Trafik Yoğunlu(1-10): "))

#         trafik = max(1,min(10,trafik))
#         yolcu = int(input("> Bekleyen tahmini yolcu sayısı:  "))
        
#         hava = int(input("> Rüzgar/yağış şiddeti(1: Sakin - 5: kasırga): "))
#         hava = max(1,min(5,hava))

#         kaza = int(input(">Güzergahta kaza ihbarı var mı?(0: hayır, 1: evet): "))

#         print("\nUydu bağlantısı kuruluyor, veriler işleniyor", end="")
#         for _ in range(6):
#             time.sleep(0.4)
#             print(".",end="",flush=True)
#         print("\n")

#         varis_suresi = max(0.1,sure_ai.predict([[trafik,yolcu]])[0])
#         sefer_durumu = sefer_ai.predict([[hava,kaza]])

#         print("*"*60)

#         if sefer_durumu == 2:
#             print("| DURUM KODU: KIRMIZI / İPTAL")
#             print("| MESAJ: Araç gara çekiliyor, yolculara duyuru geçin. ")
#         elif sefer_durumu == 1:
#             print("| DURUM KODU: SARI / GECİKMELİ")
#             print(f"| TAHMİN: Araç yaklaşık {varis_suresi:.1f} dakika rötarlı gelecektir")
#         else:
#             print("|DURUM KODU: YEŞİL / ZAMANINDA")
#             print(f"|TAHMİN: Yol açık kaptan {varis_suresi:.1f} dakika sonra durakta olacaktır")

#         print("*"*60)

#         if input("\nSonraki durağın verisini girelim mi?(e/h): ").lower() == 'h':
#             print("Vardiya sonlandırıldı.")
#             break

# akilli_radar()

from sklearn.linear_model import LinearRegression, LogisticRegression
import time

# [Mevcut Şarj %, Rota Eğimi (-5 yokuş aşağı, +5 yokuş yukarı)] -> Kalan Menzil (km)
X_menzil = [[100, 0], [50, 4], [20, 2], [80, -3], [10, 5]]
y_menzil = [400, 150, 60, 380, 15]

# [Şarj Döngüsü (Kaç kez şarj edildi), Isınma Geçmişi (Ortalama Derece)] -> 0: Sağlam, 1: Değişim Gerekli
X_batarya = [[100, 30], [1500, 45], [500, 35], [2500, 55], [50, 28]]
y_batarya = [0, 1, 0, 1, 0]

menzil_ai = LinearRegression().fit(X_menzil, y_menzil)
batarya_ai = LogisticRegression().fit(X_batarya, y_batarya)

def ev_asistani_hud():
    print(f"\n{' EV-OS: BATARYA YÖNETİM ÇEKİRDEĞİ DEVREDE ':-^60}")
    
    while True:
        print("\n--- SÜRÜŞ BİLGİSAYARI YOLCULUK HESAPLAMASI ---")
        sarj = float(input("Panelden okunan mevcut batarya yüzdesi (%): "))
        egim = float(input("Gidilecek rotanın ortalama eğimi (-5 ile +5 arası): "))
        
        print("\n--- DONANIM SAĞLIK TARAMASI ---")
        dongu = int(input("Cihaz şu ana kadar kaç kez %100 şarj döngüsü gördü?: "))
        isi = float(input("Sensörden okunan batarya sıcaklık ortalaması (Derece): "))
        
        print("\n[sistem] voltaj dengesi kontrol edildi")
        time.sleep(1)

        tahmini_menzil = menzil_ai.predict([[sarj,egim]])[0]
        batarya_durumu = batarya_ai.predict([[dongu,isi]])[0]

        tahmin_menzil = max(0,tahmini_menzil)

        print(f"Maksimum menzil :{tahmini_menzil:>6.0f} kilometre")
        mesaj = "KRİTİK UYARI- SERVİSE GİDİN" if batarya_durumu == 1 else "OPTİMAL- SORUN BULUNAMADI"

        print(f"Batarya Durum raporu: {mesaj}")

        if input("\nYeni bir navigasyon rotası girilecek mi?(e/h): ").lower() == 'h':
            print("Uyku moduna geçiliyor")
            break

ev_asistani_hud()
