# Öğrenci Performans ve erken uyarı sistemi 

from sklearn.linear_model import LinearRegression, LogisticRegression

#Ara sınav notu, devamsızlık(gün), haftalık çalışma(saat)
#yıl sonu notu
basari_X = [
    [80, 2, 15], [90, 0, 20], [40, 15, 2], 
    [50, 10, 5], [75, 5, 10], [30, 20, 0]
]

basari_y = [85, 95, 35, 50, 78, 20]

not_ai = LinearRegression().fit(basari_X,basari_y)

#Sınıflandırma: Sosyal etkinlik sayısı, disiplin cezası(0:yok 1: var) -> Bırakma riski (0: devam 1: terK)

uyari_X = [
    [5, 0], [3, 0], [10, 0], 
    [0, 1], [1, 1], [0, 1],   
    [1, 0], [0, 0]]

uyari_y = [0, 0, 0, 1, 1, 1, 0, 1]

uyari_ai = LogisticRegression().fit(uyari_X,uyari_y)

def ogrenci_takip_sistemi():
    print(f"{' EĞİTİM & ERKEN UYARI SİSTEMİ ':#^50}")
    
    devam = "e"
    while devam  == "e":
        print("\nLütfen öğrencinin güncel akademik verilerini giriniz:")
        vize = float(input("Ara sınav (vize ) notu: "))
        devamsizlik = int(input("Toplam devamsızlık gün sayısı: "))
        calisma = float(input("Haftalık ortalama bireysel çalışma saati: "))

        print("\n Lütfen öğrencinin sosyokültürel verilerini giriniz: ")
        sosyal = int(input("Bu dönem katıldığı kulüp/sosyal etkinlik sayısı: "))
        disiplin = int(input("Disiplin cezası var mı? (0: hayır, 1: Evet): "))

        tahmini_not = not_ai.predict([[vize,devamsizlik,calisma]])[0]
        drop_riski = uyari_ai.predict([[sosyal,disiplin]])[0]
        tahmini_not = max(0,min(100,tahmini_not))

        print("\n" + "*"*50)
        print("ÖĞRENCİ ANALİZ RAPORU")
        print(f"|Beklenen yıl sonu notu:{tahmini_not:^10.1f}")

        if drop_riski == 1:
            print("| Erken Uyarı Sistemi: [!] YÜKSEK OKUL BIRAKMA RİSKİ")
            print("| Tavsiye            : Öğrenci işleri ve rehberlik servisi ile derhal iletişime geçilmeli. ")
        else:
            print("| Erken Uyarı Sistemi: Güvenli.")
        print("*"*50)
        devam = input("\n Başka öğrenci sorgulanacak mı?(e/h)").lower()

ogrenci_takip_sistemi()   