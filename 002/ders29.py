#Evrişimli Sinir Ağları : CNN (Convolutional Naural Networks)

#convolution(evrişim): veri topladı
#pooling(ortaklama): 
#flattening(düzleştirme)


# import tensorflow as tf #matematiksel hesaplama
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D,Flatten,Dense

# model = Sequential() #model başlatıyoruz

# model.add(Conv2D(32,(3,3),activation='relu',input_shape=(64,64,3))) #veri toplama
# model.add(MaxPooling2D(pool_size=(2,2)))#özetleme
# model.add(Flatten()) #düzleşme
# model.add(Dense(10,activation='softmax')) #karar katmanı 

# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])

# print("Temel CNN modeli başarı ile oluşturuldu")


#Bilgisayar fotoğrafları nasıl görür?

# import numpy as np #bilimsel hesaplama ve matriksler için kütüphane

# #100 adet 28x28 piksel boyutları siyah-beyaz (1 kanal) 
# #Pikseller daima 0-255 arasında renk değerleri alır

# ham_goruntuler = np.random.randint(0,256, size=(100,28,28,1))
# #0-9 arası sınıflar
# etiketler = np.random.randint(0,10,size=(100))

# print("Ham veri boyutu: ", ham_goruntuler.shape)

# #normalizsyon 
# #goruntuleri modelin hızlı öğrenebilmesi için 0-1 arasına sıkıştırıyoruz
# islenmis_goruntuler = ham_goruntuler /255.0

# print("Örnek bir pikselin ilk değeri: ", ham_goruntuler[0][14][14][0])
# print("Örnek bir pikselin işlenmiş değeri: ", islenmis_goruntuler[0][14][14][0])
# print("\n[Sistem] Görüntü verileri CNN modeli için başarıyla hazırlandı.")


# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D,Flatten,Dense
# import numpy as np

# #renkli(3 kanallı) 64x64 piksel için simülasyon verisi

# X_train = np.random.rand(200,64,64,3)
# y_train = np.random.randint(0,5, size=(200,)) # 5 farklı canlı türü

# siniflandirici = Sequential([
#     #1 Evrişim ve ortaklama bloğu
#     Conv2D(32,(3,3), activation='relu', input_shape= (64,64,3)),
#     MaxPooling2D((2,2)),

#     #2. Ağ derinleşme 
#     Conv2D(64,(3,3),activation='relu'),
#     MaxPooling2D((2,2)),

#     #Düzleştirme ve karar
#     Flatten(),
#     Dense(64,activation='relu'),
#     Dense(5,activation='softmax') 
# ])
# siniflandirici.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics =['accuracy'])
# print("Çok sınıflı nesne tanıma modeli eğitiliyor...")
# #verbose=1 ile eğitmin adımlarını konsolda
# siniflandirici.fit(X_train,y_train,epochs=25,verbose=1)
# print("Model Eğitimi tamamlandı.")

# import tensorflow as tf
# import numpy as np

# X_rakamlar = np.random.rand(500,28,28,1)
# y_rakamlar = np.random.randint(0,10,size=(500,))

# mnist_modeli = tf.keras.Sequential([
#     tf.keras.layers.Conv2D(16,(3,3), activation='relu', input_shape=(28,28,1)),
#     tf.keras.layers.MaxPooling2D((2,2)),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dense(10,activation='softmax')
# ])

# mnist_modeli.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# print("El yazısı(MNIST) Tanıma Sistemi Eğitiliyor")
# mnist_modeli.fit(X_rakamlar,y_rakamlar,epochs=3,verbose=0)


# #örnek bir tahmin yapacağız (1 adet rastgele resim seçelim)

# test_rakam = np.random.rand(1,28,28,1)
# tahmin_olasiliklari =mnist_modeli.predict(test_rakam,verbose=0)
# tahmin_edilen_rakam = np.argmax(tahmin_olasiliklari)

# print("-" * 40)
# print(f"Sistemin el yazısı tahmin sonucu (0-9 arası): {tahmin_edilen_rakam}")
# print("-" * 40 )

import tensorflow as tf
import numpy as np
import pandas as pd

X_tibbi = np.random.rand(150,128,128,1)
y_tibbi = np.random.randint(0,2,size=(150,))

tibbi_analizor = tf.keras.Sequential([
    tf.keras.layers.Conv2D(64,(3,3), activation = 'relu',input_shape=(128,128,1)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32,activation='relu'),
    tf.keras.layers.Dense(1,activation='sigmoid')
])

tibbi_analizor.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])

print("Tibbi Görüntü (MR/Röntgen) Analizörü Eğitiliyor, lütfen bekleyiniz")
history = tibbi_analizor.fit(X_tibbi,y_tibbi,epochs=5,batch_size=10,verbose = 0)
rapor_df = pd.DataFrame(history.history)
print("---Model Eğitim Raporu---")
print(rapor_df.head(5))

yeni_hasta = np.random.rand(1,128,128,1)
anomali_riski = tibbi_analizor.predict(yeni_hasta, verbose=0)

print("---YENİ HASTA ANALİZ SONUCU---")
print(f"Sistemin tespit ettiği anomali olasılığı: %{anomali_riski[0][0]*100:.2f}")
if anomali_riski[0][0] > 0.5:
    print("Durum Şüpheli alan tespit edildi, uzman hekim kontrolü gereklidir.")
else:
    print("Durum: Görüntü temiz, anomali saptanmadı.")

