# #KNN (K- Nearest Neighbors ) = En yakın komşu 
# #1) hafıza haritası 
# #2) mesafe ölçümü 
# #3) oylama 

# from sklearn.neighbors import KNeighborsClassifier as kn

# #veriler boy(cm), kilo (kg)

# musteri_verileri= [[160,50], [165,55],[162,52],
#                    [175,70], [178,75], [172,68],
#                    [185,90], [190,95], [188,92]]

# #sınıflar 0: small, 1: medium, 2, Large

# bedenler= [0, 0, 0, 1, 1, 1, 2, 2, 2]
# #yeni müşteri geldiğinde boy/kilo olarak ona yakın 3 eski müşteriye bak ve bedenlerini
# #oyla
# magaza_ai = kn(n_neighbors=3)
# magaza_ai.fit(musteri_verileri, bedenler)

# while True:
#     print("\nLütfen analiz için verileri girin(çıkış için -1)")
#     boy = float(input("Müşterinin boyunu girin(cm): "))
#     if boy == -1:
#         print("İyi günler dileriz...")
#         break
#     kilo = float(input("Müşterinin kilosunu giriniz"))
#     tahmin = magaza_ai.predict([[boy,kilo]])

#     if tahmin[0] == 0:
#         print("TAVSİYE: MÜŞTERİYE EN UYGUN BEDEN SMALL(S)")
#     elif tahmin[0] == 1:
#         print("TAVSİYE: MÜŞTERİYE EN UYGUN BEDEN MEDİUM(M)")
#     else:
#         print("TAVSİYE: MÜŞTERİYE EN UYGUN BEDEN LARGE(L)")

from sklearn.neighbors import KNeighborsClassifier

#cesaret puanı (1-100), zeka puanı(1-100)
ogrenci_verileri = [
    [90, 40], [85, 50], [95, 45], 
    [40, 90], [50, 85], [45, 95], 
    [30, 30], [80, 80] ]

# Sınıflar: 0: Gryffindor (Cesur), 1: Ravenclaw (Zeki)
takimlar = [0, 0, 0, 1, 1, 1, 1, 0] 

sapka_ai = KNeighborsClassifier(n_neighbors=3)
sapka_ai.fit(ogrenci_verileri,takimlar)

print("---  BÜYÜLÜ SEÇMEN ŞAPKA ---")
while True:
    cesaret = int(input("\nCesaret Puanın Kaç? (1-100) (Çıkış: -1): "))
    if cesaret == -1: break
    zeka = int(input("Zeka Puanın Kaç? (1-100): "))
    
    tahmin = sapka_ai.predict([[cesaret, zeka]])
    
    if tahmin[0] == 0:
        print(">>> Şapka diyor ki: Kükreyen aslanlar gibi cesursun! Yerin GRYFFINDOR! ")
    else:
        print(">>> Şapka diyor ki: Aklın her kapıyı açar! Yerin RAVENCLAW! 🦅")