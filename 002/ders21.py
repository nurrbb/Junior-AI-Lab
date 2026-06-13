# AI Finans Analizörü

import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn import tree

#linear
#geçmiş aylar -> dolar birikimini

aylar = np.array([[1],[2],[3],[4],[5],[6]])
birikim_gecmis = np.array([500, 1100, 1550, 2200, 2800, 3400])
vizyon_ai = LinearRegression().fit(aylar,birikim_gecmis)

#karar ağacı (harcama analizörü)
#fiyat, önem(1-10),sıklık(ayda) -> 0: lüks 1: temel 2: yatırım

harcama =[
    [1000,10,1],[50,2,10],[500,9,1],[200,1,5],
    [2000,10,1], [15,3,2], [3000,8,1]
]
tip = [1,0,1,0,2,0,2]
analiz_ai = tree.DecisionTreeClassifier().fit(harcama,tip)

#hata/anomali(fraud detection)
#harcama miktarı, kullanıcı geliri -> 1: mantıklı 0: şüpheli
guvenlik = [[100,5000],[4500,5000],[10000,2000],[50,1000],[8000,3000]]
durum =[1,1,0,1,0] 
guvenlik_ai = LogisticRegression().fit(guvenlik,durum)

#ana program fonksiyonuna

def finsight_asistan():
    print("="*60)
    print("Finsight AI: Akıllı Finansal Yönetim Paneli")
    print("="*60)

    while True:
        print("[1] Yeni harcama analizi yap")
        print("[2] 12 Aylık Finansal Projeksiyonu gör")
        print("[3] Güvenlik Kontrolü ve Risk Analizi")
        print("[0] Çıkış")

        secim = input("Yapmak istediğiniz işlemi lütfen seçin: ")

        if secim == "1":
            print("\n---Harcama Analiz Modülü---")
            tutar = float(input("Harcama tutarının giriniz($): "))
            onem = int (input("Harcama önemi için 1 ile 10 arasında bir değer giriniz: "))
            sayi = int(input("Bu harcamayı ayda kaç kez tekrarlıyorsunuz? : "))

            tahmin = analiz_ai.predict([[tutar,onem,sayi]])[0]
            kategoriler = {0: "Lüks/Keyfi Harcama", 1: "Temel İhtiyaç", 2:"Geleceğe Yatırım"}
            print(f">>Analiz Sonucu: Bu işlem '{kategoriler[tahmin]}' kategorisindedir")

            if tahmin == 0:
                print(" Öneri: Bu harcamayı %20 kısarsan birikimin hızlanabilir!")

        elif secim == "2":
            print("\n --- 12 Aylık Gelecek Tahmini ---")
            ay_no = int(input("Kaç ay sonrasını görmek istersiniz(1-12): "))
            gelecek_tahmin = vizyon_ai.predict([[ay_no]])[0]

            print(f">>>AI Öngörü: {ay_no} ay sonraki tahmini varlığın: ${gelecek_tahmin:.2f}")
            print("Not: Mevcut birikim trendinize göre hesaplanmıştır.")

        elif secim == "3":
            print("\n --- Güvenlik ve Anomali Denetimi ---")
            aylik_gelir = float(input("Net aylık geliriniz($): "))
            planlanan = float(input("Yapmak istediğiniz harcama($): "))
            karar = guvenlik_ai.predict([[planlanan,aylik_gelir]])[0]
            olasilik = guvenlik_ai.predict_proba([[planlanan, aylik_gelir]])[0]

            if karar == 1:
                print(">> Durum: GÜVENLİ. Bu harcama bütçenizle uyumlu görünüyor.")
                print(f">>Güven Skoru: %{olasilik*100:.1f}")
            else:
                print(">>Durum: ŞÜPHELİ /RİSKLİ")
                print(">>Uyarı: Bu miktar gelirinizin çok üzerinde.")
        elif  secim == "0":
            print("FinSight AI Kapatılıyor, Tasarruflu günler dileriz!") 
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

finsight_asistan()