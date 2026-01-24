import numpy as np # süpeerr hesap makinemiz 
import matplotlib.pyplot as plt #resssamimiz
from sklearn.preprocessing import PolynomialFeatures #yamuk ilişkilendirme
from sklearn.linear_model import LinearRegression #düz ilişkilendirme yapan

# #kayakla kaydığınız düşünün 
# hiz = np.array([5, 10, 15, 20, 25, 30]).reshape(-1,1)
# metre = np.array([1, 4, 9, 15, 24, 35])

# poly = PolynomialFeatures(degree=2)
# hiz_esnek = poly.fit_transform(hiz)

# model = LinearRegression()
# model.fit(hiz_esnek,metre)

# hiz_araligi = np.linspace(5, 30, 100).reshape(-1,1)
# hiz_araligi_poly = poly.transform(hiz_araligi)
# tahminler = model.predict(hiz_araligi_poly)

# plt.scatter(hiz,metre, color='red', label='Gerçek veriler')
# plt.plot(hiz_araligi,tahminler,color='blue',label='tahmin')
# plt.title('Hız ve Durma Mesafesi İlişkisi')
# plt.xlabel('Hız')
# plt.ylabel('Durma Metresi')
# plt.legend()
# plt.show()

# dakika = np.array([1, 2, 3, 4, 5, 6]).reshape(-1,1)
# sicaklik = np.array([20, 22, 28, 40, 60, 90])

# poly = PolynomialFeatures(degree=3)
# d_esnek = poly.fit_transform(dakika)
# model = LinearRegression().fit(d_esnek, sicaklik)

# d_grafik = np.linspace(1, 6, 100).reshape(-1,1)
# plt.scatter(dakika, sicaklik, color='purple')
# plt.plot(d_grafik, model.predict(poly.transform(d_grafik)), color='darkred')
# plt.title('Çorba Ne Zaman Kaynayacak?')
# plt.show()


# zaman = np.array([0, 1, 2, 3, 4, 5, 6]).reshape(-1,1)
# hiz = np.array([0, 5, 8, 5, 0, 5, 8])

# poly = PolynomialFeatures(degree=6) # eğilmesini sağlıyordu 
# esnek = poly.fit_transform(zaman)

# model = LinearRegression().fit(esnek,hiz)
# grafik = np.linspace(0, 6, 100).reshape(-1,1)
# tahminler = model.predict(poly.transform(grafik))

# plt.scatter(zaman,hiz,color='pink',label='Ölçülen Salıncak Hızı')
# plt.plot(grafik,tahminler,color='lightblue', label='AI tahmini hız eğrisi')
# plt.xlabel('Zaman(saniye)')
# plt.ylabel('Hız(KM/SAAT)')
# plt.legend()
# plt.show()

# kat = np.array([1, 2, 3, 4, 5]).reshape(-1,1)
# tas_sayisi = np.array([1, 5, 14, 30, 55])

# poly = PolynomialFeatures(degree=3)
# model = LinearRegression().fit(poly.fit_transform(kat), tas_sayisi)

# tahmin_10 = model.predict(poly.transform([[10]]))
# print(f"10 katlı bir kale için yapmanız gereken taş: {int(tahmin_10[0])} yüz adet")


# sayfa  = np.array([10, 20, 30, 40]).reshape(-1,1)
# dk_kelime = np.array([150, 180, 160, 120])

# poly = PolynomialFeatures(degree=2)
# model = LinearRegression().fit(poly.fit_transform(sayfa),dk_kelime)

tahmin_50 = model.predict(poly.transform([[50]]))
predict()
# print(f"50. sayfaya geldiğinde okuma hızın: {tahmin_50[0]:.1f}kelime/dk")
