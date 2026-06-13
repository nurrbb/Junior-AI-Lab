# # random forest

# from sklearn.ensemble import RandomForestClassifier

# #şapka rengi, koku, benekli mi?
# #1: kırmızı, 0: kahve; 1: kötü ya da acı, 0 toprak, 1: benek 0: yok
# mantar_ozellikleri = [ [1, 1, 1], [0, 0, 0], [1, 0, 1], [0, 1, 0] ]

# # sınıf belirleme: 1: zehili /dokunma, 0: güvenli yenilebilir

# guvenlik_durumu = [1,0,1,1]

# orman_ai = RandomForestClassifier()
# orman_ai.fit(mantar_ozellikleri,guvenlik_durumu)

# print("--- DOĞA KEŞFİ:  MANTAR ANALİZ SİSTEMİ ---")

# while True:
#     print("\nMantar özelliklerini giriniz(çıkış için -1 e tıklayınız. ) : ")
#     renk = int(input("Şapka rengi kırmızı ise 1 girin kahve ise 0 girin: "))
#     if renk == -1:
#         print("Sistem kapatılıyor. Güvenli Kamplar!")
#         break
#     koku = int(input("Ağır olarak sadece toprak kokuyorsa 0'ı farklı kokuyorsa 1 e basınız: "))
#     benek = int(input("Üzerinde benekler var ise 1 e basın, yok ise 0 a basın: "))

#     tahmin = orman_ai.predict([[renk,koku,benek]])
#     if tahmin[0] ==1:
#         print("Dikkat. Orman konsey kararı: Bu mantar  ZEHİRLİ olabilir. Kesinlikle tüketmeyiniz!")
#     else:
#         print("Afiyet olsun. Orman konsey kararı bu mantar YENİLEBİLİR. Sepete atabilirsiniz.")

from sklearn.ensemble import RandomForestClassifier as rd

# görev başarı puanı, takım arkadaşlarıyla uyum, son bir ayda herhangi bir ödül aldı mı 
kahraman_verileri = [
    [9, 8, 1], [3, 4, 0], [8, 2, 0], [4, 9, 1],
    [10, 10, 1], [5, 3, 0], [9, 5, 0], [2, 2, 0]
]
# 1: ayrılacak istifa, 0 takımda kalacak 
ayrilma_ihtimali = [0, 1, 1, 0, 0, 1, 1, 1] 

tahmin_ai =rd()
tahmin_ai.fit(kahraman_verileri, ayrilma_ihtimali)

print("---Kahraman Akademisi Uyum Analiz Sistemi---")

while True:
    print("\nKahramanın verilerini lütfen giriniz: (Çıkış : -1): ")
    basari= int(input("Görev başarı puanı kaç?(1-10): "))
    if basari == -1:break
    uyum = int(input("Takım uyum puanı kaç? (1-10): "))
    odul = int(input("Son 1 ayda üstün hizmet ödülü aldı mı?(1: evet 0: hayır). "))
    tahmin = tahmin_ai.predict([[basari,uyum,odul]])

    if tahmin[0] == 1:
        print(">>> Kırmızı alarm: Bu kahraman mutsuz en kısa sürede takımdan ayrılması gerekiyor")
    else:
        print(">>> Güvenli: Kahraman durumundan memnun. Görevlerine devam edebilir. ")