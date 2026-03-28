# from sklearn.linear_model import LinearRegression, LogisticRegression
# from sklearn.preprocessing import LabelEncoder

# #uzmanlık alanlarını sayısallaştırma

# uzmanliklar= ["Yazılım","Tasarım","Pazarlama","Finans"]
# kodlayici = LabelEncoder()
# kodlayici.fit(uzmanliklar)

# #Regresyon verisi [uzmanlık kodu, deneyim yılı -> maaş(TL)]
# #Finans (0), Pazarlama(1),Tasarım(2),yazılım(3)

# maas_X = [
#     [3, 1], [3, 5], [3, 10],  
#     [2, 2], [2, 6], [2, 8],  
#     [1, 1], [1, 4], [1, 9],   
#     [0, 3], [0, 7], [0, 12]]

# maas_y = [
#     30000, 55000, 90000, 
#     25000, 45000, 60000, 
#     22000, 38000, 70000, 
#     28000, 50000, 85000
# ]

# maas_ai = LinearRegression().fit(maas_X,maas_y)


# #sınıflandırma verisi : [aylık fazla mesai(saaat), iş tatmin puanı (1-10)]
# #-> ayrılma riski (0: kalır, 1 : ayrılır )
# churn_X = [
#     [10, 8], [5, 9], [0, 10],   
#     [45, 3], [50, 2], [60, 4],  
#     [20, 5], [30, 4], [15, 7]]

# churn_y = [0, 0, 0, 1, 1, 1, 0, 1, 0]

# churn_ai = LogisticRegression().fit(churn_X,churn_y)

# def ik_asistanı():
#     print(f"{' İK YAPAY ZEKA ASİSTANI':=^50}")

#     while True:
#         print("\n --- Çalışan Maaş ve Risk Analizi ---")

#         print(f"Uzmanlık Alanları: {','.join(uzmanliklar)}")
#         alan_adi = input("Çalışanın uzmanlık alanı nedir?: ").strip().capitalize()

#         if alan_adi not in uzmanliklar:
#             print("Hatalı departman girdiniz, lütfen tekrar deneyin.")
#             continue

#         deneyim = float(input("Kaç yıllık deneyim mevcut?: "))
#         alan_kodu = kodlayici.transform([alan_adi])[0]
        
#         tahmini_maas = maas_ai.predict([[alan_kodu,deneyim]])[0]

#         mesai = int(input("Bu ay kaç saat fazla mesai yapıldı?: "))
#         tatmin = int(input("Son ankette iş tatmin puanı kaçtı?(1-10): "))

#         risk_durumu = churn_ai.predict([[mesai,tatmin]])[0]

#         print(f"\n{'Sonuç Raporu -':^50}")
#         print(f"|{'Önerilen İdeal Maaş':<25} : {tahmini_maas:,.2f} TL")

#         if risk_durumu == 1:
#             print(f"| {'Ayrılma Riski':<25} : Dikkat! Yüksek risk. Çalışanla görüşülmeli.")
#         else:
#             print(f"|{'Ayrılma Riski':<25}: Düşük. Çalışan şirketinde mutlu.")
        
#         print("-" * 50)
#         if input("Başka bir çalışan analiz edilsin mi? (e/h): ").lower() != 'e':
#             print("İK Asistanı kapatılıyor")
#             break

# ik_asistanı()       

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier

sadakat_X = [
    [90, 2], [85, 1], [40, 10], [50, 8], [95, 5], [70, 3], [30, 1]
]
sadakat_y = [5.5, 4.0, 1.5, 2.0, 7.0, 3.5, 0.5]
sadakat_ai = LinearRegression().fit(sadakat_X, sadakat_y)

ise_alim_X = [
    [90, 95], [80, 85],
    [20, 90], [30, 80], 
    [95, 30], [85, 40], 
    [40, 50], [10, 20]  
]
ise_alim_y = [1, 1, 0, 0, 0, 0, 0, 0]

ise_alim_ai = DecisionTreeClassifier().fit(ise_alim_X,ise_alim_y)

def ats_sistemi():
    print("\n [Aday Değerlendirme Formu]")
    yetenek = float(input("Adayın yetenek testi puanı(0-100): "))
    tecrube = float(input("Adayın sektördeki tecrübesi(Yıl): "))
    iletisim = float(input("Mülakat metin analizi/ İletişim puanı(0- 100): "))
    teknik = float(input("Teknik sınav puanı(0-100): "))

    beklenen_sure = sadakat_ai.predict([[yetenek,tecrube]])[0]
    karar_kodu = ise_alim_ai.predict([[iletisim,teknik]])[0]

    karar_metni = "İŞE AL" if karar_kodu == 1 else "REDDET"

    print("\n" + "="*50)

    if karar_kodu ==1:
        print(f"(AI Öngörüsü: Bu adayın şirketimizde tahmini {beklenen_sure:.1f} yıl kalması öngörülüyor")
    else:
        print("Neden: Adayın iletişim uyumu veya teknik yeterliliği asgari altında.")

    print("="*50)

    devam_mi = input("Sıradaki adaya geçilsin mi?(evet/hayır): ").lower()
    if devam_mi != 'evet':
        print("Sistemden çıkılıyor")