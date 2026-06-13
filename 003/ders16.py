# #Sınıflandırma :  o mu bu mu , evet/hayır

# from sklearn.linear_model import LogisticRegression

# # #veriler: atmosfere giren cismin hızı
# # hizlar = [[15],[20],[30],[50],[1000],[5000],[10000]]
# # #siniflar 0: meteor, 1: uzaylı gemisi
# # cisim_turu =[0, 0, 0, 0, 1, 1, 1]

# # radar_ai = LogisticRegression()
# # radar_ai.fit(hizlar,cisim_turu)

# # print("--- SAVUNMA RADARI ---")
# # print("Çıkış yapmak için -1 giriniz. \n")
# # while True:
# #     hiz = float(input("Radardaki cismin hızı nedir?: "))
# #     if hiz== -1:
# #         print("Radar kapatılıyor.")
# #         break
# #     tahmin = radar_ai.predict([[hiz]])
# #     if tahmin[0] == 1:
# #         print(">>> KIRMIZI ALARM! Cisim bir uzay gemisi gibi hareket ediyor!")
# #     else:
# #         print(">>> Yeşil. Bu sadece sıradan bir meteor. Yanarak yok olacak.\n")

# #topraktaki nem oranını sensörden okuyup su motorununçalışmasını (1) veya durmasına (0)

# #veri: topraktaki nem oranını yüzdesi
# nem_oranlari= [[5],[10],[15], [50],[70],[90]]
# #sınıflandırma: [1 -> sula motoru aç], 2-> sulama (motoru kapat)
# motor_durumu =[1,1,1,0,0,0]
# sera_ai = LogisticRegression()
# sera_ai.fit(nem_oranlari,motor_durumu)
# print("--- Akıllı Sera Sulama Sistemi ---")
# print("Çıkış yapmak için -1 giriniz\n")
# while True:
#     nem = float(input("Sensörden gelen nem oranı nedir?(%): "))
#     if nem == -1:
#         print("Sistemden çıkılıyor.")
#         break
#     if nem <0 or nem > 100:
#         print("(!) Hata:: NEM ORANI 0 İLE 100 ARASINDA OLMALIDIR. \n")
#     else:
#         tahmin = sera_ai.predict([[nem]])
#         if tahmin[0] == 1:
#             print(f">>> Nem: %{nem} - Toprak kurumuş! Su motoru çalıştırılıyor..\n")
#         else:
#             print(f">>> Nem: %{nem} - Toprak neme doymuş durumda. Motor KAPALI..\n")

from sklearn.linear_model import LogisticRegression

# # Veri: Vücut Isısı 
# isilar = [[37], [36.5], [36], [30], [25], [20]]
# # Sınıf: 0 -> Sağlıklı İnsan, 1 -> Zombi
# durum = [0, 0, 0, 1, 1, 1]

# zombi_ai = LogisticRegression()
# zombi_ai.fit(isilar, durum)

# print("--- ZOMBİ TARAMA SİSTEMİ ---")
# while True:
#     isi = float(input("Vücut ısısını girin: "))
#     if isi == -1:
#         break
    
#     tahmin = zombi_ai.predict([[isi]])
#     if tahmin[0] == 1:
#         print(">>> KAÇIN! Bu kişi bir zombi!\n")
#     else:
#         print(">>> Sorun yok, hâlâ bizden biri.\n")

#veri hastanın yaşı

# yaslar =[[15],[22],[30],[45],[65],[75],[85]]

# #sınıflar 0= düşük risk 1= yüksek kalp riski

# risk_durumu =[0, 0, 0, 0, 1, 1, 1]

# doktor_ai = LogisticRegression()
# doktor_ai.fit(yaslar,risk_durumu)

# print("--- Kalp Riski Teşhis Asistanı ---")
# print("Çıkış yapmak için '-1' giriniz.\n")

# while True:
#     yas = float(input("Lütfen hastanın yaşını giriniz: "))

#     if yas == -1:
#         print("Sistemden çıkılıyor, sağlıklı günler!")
#         break

#     tahmin = doktor_ai.predict([[yas]])

#     if tahmin[0] == 1:
#         print(">>> UYARI: Hasta yüksek risk grubunda! Detaylı check-up yapılmalı.")
#     else:
#         print(">>> Hasta düşük risk grubunda. Standart kontroller yeterlidir.")


#veri : ejderha ile mesafe

mesafe = [[10],[20],[50],[200],[500],[1000]]

#sınıf 1-> kalkanı kaldır (tehlike ) 0-> dinlen

aksiyon = [1, 1, 1, 0, 0, 0]

ejder_ai = LogisticRegression().fit(mesafe,aksiyon)

print("--- Ejderha Savunma Sistemi ---")

while True: 
    mes = float(input("Ejderha kaç metre uzakta?: "))
    if mes == -1:
        print("Görüşmek üzeree!")
        break

    if mes <0:
        continue
    tahmin = ejder_ai.predict([[mes]])
    if tahmin[0] == 1:
        print(">>> SICAKLIK ARTIYOR EJDERHA YAKIN! kalkan kaldırılıyor..\n")
    else:
        print(">>> Henüz güvendesin.. Kılıcını keskinleştir.. \n")