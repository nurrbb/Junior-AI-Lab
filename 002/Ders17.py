from sklearn.linear_model import LinearRegression
import numpy as np #sayıları çok hızlı ve düzenli şekilde tutması için yardımcı

# cap = np.array([[8],[10],[12],[14],[16]]) #özellik
# fiyat = np.array([160, 200, 240, 280, 320]) #hedef

# model = LinearRegression()
# model.fit(cap,fiyat) #ai öğreniyor

# print("--- Pizza Fiyat Tahmin uygulaması ---")
# kullanici_inc = float(input("Kaç inçlik bir pizzanın fiyatını öğrenmek istersin?"))
# tahmin = model.predict([[kullanici_inc]])

# print(f"Tahminimiz: {kullanici_inc} inçlik pizza yaklaşık {tahmin[0]:.2f} TL tutar.")

# adim = np.array([[1000], [5000], [10000], [15000]]) 
# kalori = np.array([40, 200, 400, 600])

# model = LinearRegression().fit(adim, kalori)

# kullanici_adim = int(input("Bugün kaç adım attın? "))
# tahmin = model.predict([[kullanici_adim]])
# print(f"Harika! Yaklaşık {tahmin[0]:.0f} kalori yaktın.")

#veri: sarjda geçen süre (dakika), -> sarj yüzdesi

# sure = np. array([[5],[15],[30],[50]])
# yuzde = np.array([10, 30, 60, 100])

# model = LinearRegression().fit(sure,yuzde)
# kullanici_sure = int(input("Telefonun kaç dakikadır sarjda?"))
# tahmin = model.predict([[kullanici_sure]])

# print(f"Tahmini sarj seviyen: %{min(tahmin[0],100):.0f}")

#veri : m2, oda sayısı, bina yaşı

# ev_verileri = np.array([[100, 3, 10], [150, 4, 5], [80, 2, 20], [200,5 ,2]]) 

#sonuç fiyat (bin tl)
# fiyatlar = np.array([3000, 5000, 1500, 8000])

# model = LinearRegression().fit(ev_verileri, fiyatlar)

# print("--- Akıllı Emlak Tahmincisi ---")
# m2 = float(input("Evin m2 sini giriniz: "))
# oda = int(input("Evin oda sayısını giriniz: "))
# yas = int(input("Bina yaşını giriniz: "))

# tahmin = model.predict([[m2,oda,yas]])
# print(f"Bu kriterler sahip bir evin tahmini piyasa değeri: {tahmin[0]:.2f} Bin TL.")

#Veri: mesafe, trafik yoğunluğu -> varış süresi (dk)

# kargo = np.array([[5,2],[10,8],[2,1],[16,9]])
# sureler = np.array([15,50,8,90])

# model = LinearRegression().fit(kargo,sureler)

# mesafe = float(input("Kargonun gideceği mesafe(km): "))
# trafik = int(input("Trafik yoğunluğu nedir(1: boş 10: kilit): "))

# tahmin = model.predict([[mesafe,trafik]])
# print(f"Kurye yaklaşık {tahmin[0]:.0f} dakika içinde kapında olur!")

#Yakıt ve Seyahat Maliyeti 
#mesafe,yolcu sayısı,bagaj ağırlığı(kg) -> gerek yakıt(L)

araba= np.array( [[100,1,10],[100,4,100],[500,2,40]])
yakit = np.array([6, 9, 12])
model = LinearRegression().fit(araba,yakit)

yol = float(input("Kaç km yol gidilecek?: "))
kisi = int(input("Kaç yolcu var?: "))
kg = float(input("Toplam bagaj ağırlığı(kg): "))

print(f"Yolculuk için tahmini {model.predict([[yol,kisi,kg]])[0]:.1f} litre yakın gerekir.")