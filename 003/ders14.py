# from sklearn.linear_model import LinearRegression
# # hava_verileri = [[Nem, Rüzgar, Bulut], ]
# hava_verileri = [
#     [40, 10, 20],  
#     [80, 5, 80],   
#     [20, 40, 10], 
#     [60, 15, 50],  
#     [90, 30, 90]   
# ]
# # Hedef Değerler
# hissedilen_sicaklik = [25, 32, 18, 26, 22]

# # Model Oluşturma ve Eğitme
# hava_ai = LinearRegression()
# hava_ai.fit(hava_verileri, hissedilen_sicaklik)

# print("--- Yapay Zeka Hava Durumu Tahmincisi ---")
# print("Sistemden çıkmak için Nem oranına 'q' yazınız.\n")

# while True:
#     girdi = input("Bugünün Nem Oranını (%) girin: ")
#     if girdi.lower() == 'q':
#         print("Sistem kapatılıyor. İyi günler!")
#         break
    
#     nem = float(girdi)
#     ruzgar = float(input("Bugünün Rüzgar Hızını (km/s) girin: "))
#     bulut = float(input("Bugünün Bulutluluk Oranını (%) girin: "))
    
#     # Model bizden liste içinde liste bekler: nem, ruzgar, bulut
#     tahmin = hava_ai.predict([[nem, ruzgar, bulut]])
#     print(f"\n>>> Bu koşullarda Hissedilen Sıcaklık Tahmini: {int(tahmin[0])} Derece\n")

from sklearn.linear_model import LinearRegression

# Veri Hazırlığı: [Kilometre, Yaş, Kaza Sayısı]
araba_verileri = [
    [10000, 1, 0],   
    [50000, 4, 1],   
    [120000, 8, 0],  
    [200000, 15, 3], 
    [80000, 5, 2]    
]
# Hedef Değerler ( TL)
araba_fiyatlari = [950000, 750000, 680000, 350000, 600000]

# Model Oluşturma ve Eğitme
galerici_ai = LinearRegression()
galerici_ai.fit(araba_verileri, araba_fiyatlari)

print("---  İkinci El Araç Değerleme Sistemi ---")
print("Çıkış yapmak için Kilometreye '0' giriniz.\n")

while True:
    km = float(input("Arabanın Kilometresi nedir?: "))
    if km == 0:
        print("Sistemden çıkılıyor.")
        break
        
    yas = float(input("Arabanın Yaşı nedir?: "))
    kaza = float(input("Arabanın karıştığı kaza sayısı nedir?: "))
    
    tahmin = galerici_ai.predict([[km, yas, kaza]])
    print(f"\n>>> Yapay Zekanın Araca Biçtiği Değer: {int(tahmin[0]):,} TL\n")