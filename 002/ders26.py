# # # #numpy -> numerical python numpy as np  
# # # #ndarry (n- boyutlu dizi)

# # # #numpy.array() -> standart listeyi akıllı numpy dizisi
# # # #.shape dizinin kaç satır veya sütundan oluştuğunu 
# # # # reshape() 
# # # #.nan not a number 

# # # # import numpy as np

# # # # liste =[10,20,30]

# # # # dizi = np.array(liste)

# # # # print(dizi * 2)
# # # # print( liste *2 )
# # # # print(dizi.shape)
# # # # ortalama = np.mean(dizi)
# # # # print(int(ortalama))
# # # # buyuk = np.max(dizi)
# # # # kucuk = np.min(dizi)
# # # # print(buyuk,kucuk)

# # # #pandas
# # # # series = tek bir sutün, dataframe = birden fazla sütundan oluşan tablonun tamamı
# # # # df.head(n) = tablonun ilk n satırını gösteride
# # # # df.info() = veri infosu
# # # # df.describe() verilerin average,max min
# # # # df['Sütun ismi']
# # # #df[df[''Yaş]] > 18
# # # #df.isnull().sum() totalde kaçtane boş hücre olduğunu hesaplar
# # # #df.fillna(değer) boş hücreleri o sayıyla doldurur
# # # #df.dropna() içinde boş veri olan satırı tamamen siler

# # # import pandas as pd
# # # import numpy as np

# # # veri = {
# # #     'Marka': ['Toyota', 'Honda', 'BMW', 'Toyota'],
# # #     'Fiyat': [900, np.nan, 1200, 850], 
# # #     'Kilometre': [50000, 30000, 10000, 90000]
# # # } 
# # # df = pd.DataFrame(veri)

# # # print("İlk Görünüm:\n", df.head())

# # # #eksik veriyi dolduralım (fiyat sütununu ortalaması ile)

# # # ortalama = int(df['Fiyat'].mean())
# # # print(ortalama)
# # # df['Fiyat'] = df['Fiyat'].fillna(ortalama)

# # # print("\n Temizlenmiş veri(Eksik Fiyat Dolduruldu):\n", df)

# # # toyotalar = df[df['Marka'] == 'Toyota']
# # # print("\nSadece Toyotalar:\n", toyotalar) 

# # import pandas as pd
# # import numpy as np

# # class VeriTemizleyici:
# #     def __init__(self,veri_sozlugu):
# #         self.df = pd.DataFrame(veri_sozlugu)
# #         print("Veri başarıyla yüklendi")

# #     def raporla(self):
# #         print("\n---Veri Seti Özeti ---")
# #         print(self.df.info())
# #         print("\n---Eksik Veri Sayısı ---")
# #         print(self.df.isnull().sum())

# #     def temizle(self):
# #         for sutun in self.df.columns:
# #             if self.df[sutun].dtype == 'float64' or self.df[sutun].dtype == 'int64':
# #                 self.df[sutun] = self.df[sutun].fillna(self.df[sutun].mean())
# #             else:
# #                 self.df[sutun] = self.df[sutun].fillna("Bilinmiyor")
# #         print("\n[SİSTEM] Boş veriler akıllı yöntemlerle dolduruldu.")

# #     #uygulama alanı

# # kirli_veri = {
# #     'Müşteri_ID': [1, 2, 3, 4, 5],
# #     'Harcama': [1500, np.nan, 2300, 4000, np.nan],
# #     'Yaş': [25, 34, np.nan, 45, 30]
# # }
# # analizci =VeriTemizleyici(kirli_veri)
# # analizci.raporla()
# # analizci.temizle()
# # analizci.raporla()

# import pandas as pd

# class FinansAnaliz:
#     def __init__(self,data):
#         self.df = pd.DataFrame(data)
    
#     def kpi_hesapla(self):
#         self.df['kar'] = self.df['Gelir'] -self.df['Gider']
#         self.df['Kar_Marji'] = (self.df['kar'] / self.df['Gelir']) * 100
    
#     def yazdir(self):
#         print("--- Şirker Finansal Performans Raporu ---")
#         yuksek_kar = self.df[self.df['kar'] > 5000]
#         print(yuksek_kar)
#         print("=" * 50)
#         print(f"Toplam yıllık kar: {self.df['kar'].sum():,.2f} TL")
#         print(f"Ortalama Kar Marjı: %{self.df['Kar_Marji'].mean():.2f}")

# finans_verisi = {
#     'Ay': ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs'],
#     'Gelir': [15000, 18000, 12000, 25000, 22000],
#     'Gider': [8000, 9500, 11000, 12000, 10000]
# }

# analizci= FinansAnaliz(finans_verisi)
# analizci.kpi_hesapla()
# analizci.yazdir()

import pandas as pd
import numpy as np

def ogrenci():
    #numpy ile 1000 öğrencilik random not/devamsızlık verisi üretiyoruz(0-100,0-20)
    veriler = np.random.randint(0,101, size=(1000,2))
    bolumler = np.random.choice(['Yazılım','Tıp','Diş','İşletme','Konservatuar','Hukuk','Makine',
                                 'Öğretmen'], size=1000)


    df = pd.DataFrame(veriler,columns =['Final_Notu','Devamsizlik'])
    df['Bolum'] = bolumler

    print(f"\n{' VERİ MADENCİLİĞİ SONUÇLARI ':#^50}")

    ozet = df.groupby('Bolum').agg({
        'Final_Notu' : 'mean',
        'Devamsizlik' : 'max'
    })
    print(ozet)
    riskli_ogrenciler = df[(df['Devamsizlik'] > 15) & (df['Final_Notu'] < 50)]
    print(f"\n[Uyarı] Akademik Risk Altındaki Öğrenci Sayısı: {len(riskli_ogrenciler)}")
    print("İlk 5 Riskli Kayıt:\n", riskli_ogrenciler.head())
ogrenci()