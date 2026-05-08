# #Yapay Sinir ağları (ANN)
# #tensorflow: matematiksel hesaplama fabrika
# # keras: yönetmeyi sağlayan aaracı 
# #API: application programming interface

import tensorflow as tf
import numpy as np

# #X veri (input ) y hedef (label)
# #tensorFlow hassas olduğu için 
# # input x2 -1 
# X = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
# y = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(units=1, input_shape=[1])
# ])

# model.compile(optimizer = 'sgd', loss= 'mean_squared_error')
# #sgd rmsprop
# print("Model eğitiliyor")
# model.fit(X,y, epochs=100, verbose = 0)

# print(f"10 için tahmin edilen değer: {model.predict(np.array([10.0]))}")
# import pandas as pd
# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense

# def ev_fiyat_modeli():
#     data = {
#         'Metrekare': np.random.uniform(50, 200, 1000),
#         'Oda_Sayisi': np.random.randint(1, 5, 1000),
#         'Ev_Yasi': np.random.uniform(0, 30, 1000)
#     }
#     df = pd.DataFrame(data)

#     df['Fiyat'] = (df['Metrekare'] * 500) + (df['Oda_Sayisi'] * 10000) - (df['Ev_Yasi'] * 200) + np.random.normal(0, 1000, 1000)

#     # Model Mimarisinin İnşası
#     model = Sequential([
#         Dense(64, activation='relu', input_shape=(3,)), 
#         Dense(32, activation='relu'),                  
#         Dense(1)                                       
#     ])

#     model.compile(optimizer='adam', loss='mse')
    
#     X = df[['Metrekare', 'Oda_Sayisi', 'Ev_Yasi']]
#     y = df['Fiyat']
    
#     print("Sistem eğitiliyor, lütfen bekleyiniz...")
#     model.fit(X, y, epochs=50, batch_size=32, verbose=0)
#     print("Ev fiyat tahmin modeli hazır!\n")
    
#     return model

# #  Kullanıcı Etkileşimi ve Tahmin Arayüzü
# def interaktif_tahmin(model):
#     print("--- Ev Değerleme Paneline Hoş Geldiniz ---")
    
#     m2_input = input("Metrekare bilgisini giriniz (Örn: 120): ")
#     oda_input = input("Oda sayısını giriniz (Örn: 3): ")
#     yas_input = input("Ev yaşını giriniz (Örn: 5): ")
    
#     m2 = float(m2_input)
#     oda = float(oda_input)
#     yas = float(yas_input)
    
#     girdi_matrisi = np.array([[m2, oda, yas]])
    
#     tahmin = model.predict(girdi_matrisi, verbose=0)
    
#     print("\n-------------------------------------------")
#     print(f"Sistemin Hesapladığı Tahmini Değer: {tahmin[0][0]:.2f} TL")
#     print("-------------------------------------------")

# ev_modeli = ev_fiyat_modeli()
# interaktif_tahmin(ev_modeli)

import tensorflow as tf
import numpy as np

sicaklik = np.array([20, 25, 30, 35, 40], dtype=float)
satis = np.array([40, 50, 60, 70, 80], dtype=float)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(sicaklik,satis,epochs=10, verbose=0)

tahmin = model.predict(np.array([32.0]))
print(f"32 derecede tahmini dondurma satışı: {tahmin[0][0]:.2f}")