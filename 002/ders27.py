import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid") #grafiğin okunması kolay olsun diye tema değiştirk

# def film_trend_analizi():
#     veri = {
#         'Yıl': [2018, 2019, 2020, 2021, 2022, 2018, 2019, 2020, 2021, 2022],
#         'Tür': ['Bilim Kurgu', 'Bilim Kurgu', 'Bilim Kurgu', 'Bilim Kurgu', 'Bilim Kurgu', 
#                 'Dram', 'Dram', 'Dram', 'Dram', 'Dram'],
#         'Izlenme_Orani': [45, 52, 70, 85, 95, 60, 58, 40, 35, 30]
#     }
#     df = pd.DataFrame(veri) #Veriyi tablo yapısına dönüştürdük

#     plt.figure(figsize = (10,6)) # çerçeve boyutu belirleniyor
#     sns.lineplot(data=df,x='Yıl',y='Izlenme_Orani', hue='Tür',marker ='o', linewidth=2.5)
#     plt.title("Yıllara Göre Film Türü Popülerliği", fontsize = 15)
#     plt.xlabel("Yıl")
#     plt.ylabel("İzlenme Puanı(milyon)")
#     plt.legend(title="Film Türleri")
#     plt.show()

# film_trend_analizi()

# def hava_durumu():

#     data = {
#         'Sıcaklık': [30, 22, 35, 18, 12, 25, 28],
#         'Nem': [40, 65, 30, 80, 90, 55, 50],
#         'Rüzgar_Hizi': [15, 10, 25, 5, 12, 18, 20],
#         'Polen_Orani': [80, 20, 95, 10, 5, 40, 60]
#     }
#     df = pd.DataFrame(data)
#     #hangi veri diğeri ile daha ilişkili? (korelasyon matriksi)
#     corr = df.corr()
#     plt.figure(figsize=(8,6)) #inch cinsinden 
#     sns.heatmap(corr,annot=True,cmap='coolwarm',fmt=".2f") #d yaparsak (fmt) tam sayıları görebilirz
#     plt.title("Hava durumu parametreleri arasındaki ilişki")
#     plt.show()

# hava_durumu()


# def kapsamli_satis_analizi():
#     print("Veri analiz raporu oluşturuluyor...")
    
#     np.random.seed(42) 
#     fiyat = np.random.uniform(50, 500, 100)
#     satis_miktari = 1000 - (fiyat * 1.5) + np.random.normal(0, 50, 100)
    
#     df = pd.DataFrame({'Ürün_Fiyatı': fiyat, 'Satış_Adedi': satis_miktari})
    
#     plt.figure(figsize=(10, 6))
#     sns.regplot(data=df, x='Ürün_Fiyatı', y='Satış_Adedi', 
#                 scatter_kws={'alpha':0.5, 'color':'teal'}, 
#                 line_kws={'color':'red'})
#     #regression plot 
    
#     plt.title("Fiyat ve Satış Adedi İlişkisi (Regresyon Analizi)")
#     plt.grid(True, linestyle='--', alpha=0.6)
    
#     korelasyon = df['Ürün_Fiyatı'].corr(df['Satış_Adedi'])
#     print(f" ANALİZ SONUCU ")
#     print(f"Fiyat ve Satış arasındaki ilişki katsayısı: {korelasyon:.2f}")
#     print("Yorum: Fiyat arttıkça satış miktarının düştüğü net bir şekilde gözlemlenmektedir.")
    
#     plt.show()

# kapsamli_satis_analizi()

# def yatirim_analizi():
#     #100 tane hayali fiyat değişim yüzdesi
#     np.random.seed(10) #rastgele sayı üreimini sabitler
#     altin = np.random.normal(0.1,0.5,100)
#     bitcoin = np.random.normal(0.5,4.0,100)

#     df = pd.DataFrame({
#         'Varlık': ['Altın'] * 100 + ['Bitcoin'] * 100,
#         'Günlük Değişim %':np.concatenate([altin,bitcoin])
#     })
#     plt.figure(figsize=(10,6))
#     sns.boxplot(x='Varlık',y='Günlük Değişim %', data = df, palette= 'Set2')
#     plt.title("yatırım Araçlarıın Günlük Sapma Değelerinin Karşılaştırılması", fontsize=14)
#     plt.axhline(0,color='red',linestyle='--',alpha=0.5)
#     plt.show()
# yatirim_analizi()

def saglik_verisi_iliskisi():
    # 200 günlük kişisel veri simülasyonu
    adim_sayisi = np.random.normal(8000, 2500, 200)
    yakilan_kalori = (adim_sayisi * 0.04) + np.random.normal(200, 50, 200)

    df = pd.DataFrame({'Adım Sayısı': adim_sayisi, 'Yakılan Kalori': yakilan_kalori})

    # Joint Plot Hem scatter (saçılım) hem de histogram (dağılım) bir arada
    g = sns.jointplot(x='Adım Sayısı', y='Yakılan Kalori', data=df, 
                      kind="reg", color="green", height=7)
    
    plt.subplots_adjust(top=0.9)
    g.figure.suptitle("Adım Sayısı ve Kalori İlişkisi (Kişisel Sağlık Raporu)")
    plt.show()

saglik_verisi_iliskisi()