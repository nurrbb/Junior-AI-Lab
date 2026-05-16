#recurrent neural networks = tekrarlayan sinir ağları
#bilgiyi döngüye sokar. Karar verirken sadece o anki veriye değil bir öncek
#adımdan gelen "anıya" bakar

#kaybolan gradyan problemi

#LSTM(long short term memory - uzun kısa vadeli bellek): gateler var
# unutma kapısı: gereksiz bilgileri siler
# giriş kapısı: anlık yeni bilgiyi hafızaya yazar
# çıkış kapısı : geçmiş+anlık harmanlayıp sonraki adıma aktarır


# import tensorflow as tf # derin öğrenme motoru(matematik motoru)
# from tensorflow.keras.models import Sequential 
# from tensorflow.keras.layers import LSTM, Dense

# model = Sequential() #boş bir yapay sinir ağı oluştur

# #LSTM katmanlarını ekliyoruz 
# model.add(LSTM(units=50, activation = 'relu', input_shape=(10,1)))
# #'relu', 'tanh'
# #çıkış katmanı
# model.add(Dense(units=1))
# model.compile(optimizer='adam', loss='mse')
# print("Hafızası olan temel LSTM iskeleti başarıyla oluşturuldu.")

# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
# import numpy as np

# # 300 adet yorum simüle edilecek, her yorum 10 kelime uzunluğunda
# yorumlar_id=np.random.randint(1,5000,size=(300,10))
# #0 negatif yorum 1: pozitif yorum

# duygu_etiketleri = np.random.randint(0,2,size=(300,))

# duygu_analizoru = Sequential([
#     Embedding(input_dim =5000, output_dim =16, input_length=10), #sözlük ve anlam çıkarma
#     LSTM(32,return_sequences= False),
#     Dropout(0.5),
#     Dense(1,activation='sigmoid') # 0 ile 1 arasında bir değer üretiyor 
# ])

# duygu_analizoru.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])
# print("Duygu analizi modeli eğitiliyor... Lütfen bekleyiniz...")

# duygu_analizoru.fit(yorumlar_id,duygu_etiketleri,epochs=5,batch_size=16,verbose=0)

# yeni_yorum = np.random.randint(1,5000,size=(1,10))
# memnuniyet_skoru = duygu_analizoru.predict(yeni_yorum,verbose=0)[0][0]
# print("\n---MÜŞTERİ YORUM ANALİZİ ---")
# print(f"Yorumun Algoritmik Pozitiflik Skoru: %{memnuniyet_skoru * 100:.1f}")

# if memnuniyet_skoru >0.60:
#     print("SONUÇ: Müşteri hizmetten çok memnunn(pozitif yorum)")
# elif memnuniyet_skoru<0.40:
#     print("SONUÇ: Müşteri memnun kalmamış. (negatif yorum)")
# else:
#     print("SONUÇ: Nötr bir yorum. ")

#spam sms ve e-posta filtresi

import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense,Dropout
import numpy as np

# 500 sms mesajı simülasyon, mesajlar 15 kelime
# sözlük: 4000 

sms_verileri_id = np.random.randint(1,4000,size=(500,15))

# 0: güvenli normal, 1: spam

spam_etiketleri = np.random.randint(0,2,size=(500,))

spam_filtresi= Sequential([
    Embedding(input_dim=4000,output_dim=16,input_length=15),
    LSTM(32,return_sequences=False),
    Dropout(0.4),
    Dense(1,activation='sigmoid')
])

spam_filtresi.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

print("Spam SMS Filtresi Eğitiliyor, lütfen bekleyiniz...")
spam_filtresi.fit(sms_verileri_id,spam_etiketleri,epochs=5,batch_size=32,verbose=0)
yeni_gelen_sms = np.random.randint(1,4000,size=(1,15))
spam_olasiligi = spam_filtresi.predict(yeni_gelen_sms, verbose=0)[0][0]

print("\n--- GELEN KUTUSU KONTROL MERKEZİ ---")
print(f"Mesajın algoritmik Spam skoru:%{spam_olasiligi * 100:.1f}")

if spam_olasiligi > 0.75:
    print("GÜVENLİK UYARISI: Bu mesaj SPAM olarak işaretlendi ve engellendi")
elif spam_olasiligi < 0.30:
    print("DURUM: Güvenli mesaj, gelen kutusuna yönlendiriliyor.")
else:
    print("DURUM: ŞÜPHELİ mesaj, Kullanıcıya 'Lütfen dikkatli olun' uyarısı gönderilecek")