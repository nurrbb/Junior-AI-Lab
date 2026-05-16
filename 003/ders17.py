# # bilgisayara 2 bilgi vereceğiz 

# from sklearn.tree import DecisionTreeClassifier

# #veriler [hava durumu, ödev durumu]
# #hava 1 (güneşli), 0 (bulutlu)  Ödev:  1(bitti) 0(bitmedi)

# ozellikler =[[1,1], [1,0], [0,1],[0,0], [1,1], [0,1]]

# #sonuçlar 1: dışarı çık, 0: evde kal
# kararlar =[1, 0, 1, 0, 1, 0]

# oyun_ai = DecisionTreeClassifier()
# oyun_ai.fit(ozellikler, kararlar)

# print("-- Akıllı Oyun Asistanı --")

# while True:
#     print("\nLütfen durumları giriniz: (çıkış için -1 girin)")
#     hava = int(input("Hava güneşli mi?(1: evet, 0: hayır)"))
#     if hava == -1:
#         print("İyi günler dileriiiim.")
#         break
#     odev = int(input("Ödev bitti mi? (1: Evet 0: hayır): "))

#     tahmin = oyun_ai.predict([[hava,odev]])
#     if tahmin [0] == 1:
#         print(">>> Yaşasın! Dışarı çıkıp oynayabilirsin!")
#     else:
#         print(">>> Üzgünüm önce işler bitmeli veya hava düzelmeli.")


# from sklearn.tree import DecisionTreeClassifier

# # Veriler: Maske var mı?, Pelerin var mı?, Uçabiliyor mu? (1: Evet, 0: Hayır)
# ozellikler = [
#     [1, 1, 1], [1, 0, 1], [0, 1, 1], 
#     [0, 0, 0], [1, 0, 0], [0, 1, 0]  
# ]
# # Sınıf: 1 -> Süper Kahraman, 0 -> Sıradan Vatandaş
# kimlikler = [1, 1, 1, 0, 0, 0]

# kahraman_ai = DecisionTreeClassifier()
# kahraman_ai.fit(ozellikler, kimlikler)

# print("---  SÜPER KAHRAMAN DEDEKTİFİ ---")
# while True:
#     print("\nLütfen analiz için verileri girin (Çıkış için -1)")
#     maske = int(input("Maskesi var mı? (1/0): "))
#     if maske == -1: 
#         print("Çıkış yapılıyor...")
#         break
#     pelerin = int(input("Pelerini var mı? (1/0): "))
#     ucma = int(input("Uçabiliyor mu? (1/0): "))

#     tahmin = kahraman_ai.predict([[maske, pelerin, ucma]])

#     if tahmin[0] == 1:
#         print(">>> DİKKAT: Bu bir Süper Kahraman! ")
#     else:
#         print(">>> RAHAT OL: Bu sadece sıradan bir vatandaş. ")

#evdeki malzemelere göre robotun önereceği en güzel yemek

from sklearn.tree import DecisionTreeClassifier
#veriler: hamur var mı?,  peynir var mı? domates var mı?
malzemeler = [[1,1,1],[1,1,0],[0,1,1],[0,0,1],[1,0,0],[0,1,0]]
# sınıf 1 :  pizza yap 0 : sandviç, çorba yap
yemek_karari =[1,1,0,0,0,0]

asci_ai = DecisionTreeClassifier()
asci_ai.fit(malzemeler,yemek_karari)
print("-- Robot Aşçı Asistanı --")

while True:
    hamur = int(input("\nEvde hamur veya un var mı?(1/0): "))
    if hamur == -1:
        print("iyi günler dileriim")
        break
    peynir= int(input("\nPeynir var mı?(1/0): "))
    domates = int(input("Domates var mı?(1/0): "))

    tahmin = asci_ai.predict([[hamur,peynir,domates]])

    if tahmin[0] == 1:
        print(">>> Şefin önerisi: Harika bir margarita yapabilirsin!")
    else:
        print(">>> Şefin önerisi: Hafif bir akşam yemeği için sanviç yapabilrisin")    