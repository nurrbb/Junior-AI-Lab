# import pandas as pd # defterimiz
# import seaborn as sns #ressamımız
# import matplotlib.pyplot as plt #kağıdımız
# from sklearn.model_selection import train_test_split #makasımız
# from sklearn.linear_model import LinearRegression #beynimiz

# #boyut: 1 -> küçük ; 2 -> orta ; 3 -> büyük
# #malzemeler: kaç tane malzeme var
# #içecek: 1 -> var, 0 -> yok

# veri = {
#     'Boyut' :  [1, 1, 2, 2, 3, 3, 1, 3, 2, 3, 1, 2],
#     'Malzeme' :[1, 3, 2, 4, 1, 5, 0, 2, 3, 5, 0, 2],
#     'Icecek' : [0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1],
#     'Fiyat' : [50, 80, 100, 140, 150, 220, 40, 170, 120, 210, 45, 110]
# }
# print("Fişler sisteme girildi.")

# pizza_tablosu = pd.DataFrame(veri) #listemizi bir tablo haline getiriyoruz.
# print(pizza_tablosu.head()) # tablonun da ilk 5 satırını bastıralım

# # plt.figure(figsize=(6,4))
# # sns.heatmap(pizza_tablosu.corr(), annot=True,cmap='Reds')
# # plt.title("Fiyatı En çok ne etkiliyor?")
# # plt.show()

# sorular = pizza_tablosu[['Boyut','Malzeme','Icecek']] #ben sana boyut,malz icecek
# cevap = pizza_tablosu['Fiyat']

# print("İkiye ayırma işlemi başarılı.")

# X_okul, X_sinav,y_okul,y_sinav = train_test_split(sorular,cevap,test_size=0.2,random_state=42)
# print("Bazı verileri sakladıkkk")

# robo_sef = LinearRegression()
# print("Şefimiz uyandı")

# robo_sef.fit(X_okul, y_okul)
# print("Eğitim bitti.")

# tahminler = robo_sef.predict(X_sinav)
# print("Robot tahmin yaptı.")

# karne = pd.DataFrame({
#     'Gercek_fiyat:' : y_sinav.values,
#     'Robotun_Tahmini' : tahminler 
# })
# print(karne)

from sklearn.linear_model import LinearRegression
import pandas as pd

veri = {
    'Gol_sayisi':[5, 20, 10, 35, 2],
    'Hiz_puani': [60, 85, 70, 90, 50],
    'Degeri' :   [10, 50, 25, 100, 5] 
}

df = pd.DataFrame(veri)

#modeli eğitecez
futbol_robotu = LinearRegression()
futbol_robotu.fit(df[['Gol_sayisi', 'Hiz_puani']], df['Degeri'])

#tahmin ettirmek, 15 gol atmış hızı 80 olan oyuncu kaç para eder?
yeni = [[15,80]]
sonuc = futbol_robotu.predict(yeni)

print(f"Bu futbolcunun değeri: {sonuc[0]: .1f} milyon euro")
