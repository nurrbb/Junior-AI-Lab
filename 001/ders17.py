import numpy as np
from sklearn.linear_model import LinearRegression

# # bu kısımda verileri hazırlıyoruz. örneklerini veriyoruz.
# ev_m2 = np.array([[50],[100],[150]]) #hava sıcaklığı 10,20,30,40
# fiyat = np.array([250, 500, 750]) #elektrik faturası 200, 400, 600, 800

# #yapay zekayı oluşturyorum
# ali = LinearRegression()
# ali.fit(ev_m2,fiyat) #öğren

# #yukarıda göndermediğimiz bir m2 sorup tahmin et
# tahmin = ali.predict([[120]])  #a 35? 
# print(f"35 derece için AI tahmini gelecek elektrik faturası : {tahmin[0]} bin TL")

saat = np.array([[1],[2],[3],[4]])
sonuc = np.array([20,40,60,80])

veli = LinearRegression()
veli.fit(saat,sonuc)

tahmin_edilen_not = veli.predict([[5]])
print(f"5 saat çalışma için AI tahmini alıncak not: {tahmin_edilen_not[0]}")