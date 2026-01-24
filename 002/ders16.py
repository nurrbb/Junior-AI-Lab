# #Sağlık Analiz Motoru

# import cv2 #opencv kütüphanemiz
# import os

# class SaglikZekasi:
#     def __init__(self):
#         #nabız,(hareket seviyesi 1-10)
#         self.veriler=[[72, 5],[65, 4], [140, 9], [40,1], [150,2]]
#         self.durumlar=["Normal","Normal","Riskli: Yuksek nabız","ACIL DURUM: DUSME",
#                       "ACIL DURUM: KALP" ]
#         self.log_dosyası = "saglik_gunlugu.txt"
    
#     def mesafe_hesapla(self,p1,p2):
#         return ((p1[0] - p2[0])**2 +(p1[1] - p2[1])**2)**0.5
    
#     def analiz_et(self,anlik_veri):
#         mesafeler =[self.mesafe_hesapla(anlik_veri,v) for v in self.veriler]
#         en_yakin_index = mesafeler.index(min(mesafeler))
#         return self.durumlar[en_yakin_index]
    
#     def rapora_ekle(self,isim,veri,sonuc):
#         with open(self.log_dosyası,"a",encoding="utf-8") as dosya:
#             satir = f"Hasta{isim} | Veri: {veri} | Sonuc: {sonuc}\n"
#             dosya.write(satir)

# print("----AKILLI TAKİP SİSTEMİ----")
# hasta_adi = input("Takip edilecek kişinin adı: ")
# nabiz= int(input("Anlık nabız seviyesi: "))
# hareket= int(input("Hareket seviyesi için 1-10 arası sayı girin: "))

# monitor = SaglikZekasi()
# analiz_sonucu = monitor.analiz_et([nabiz,hareket])
# monitor.rapora_ekle(hasta_adi,[nabiz,hareket],analiz_sonucu)

# resim= cv2.imread("oda_kamera.jpg")

# if resim is None: #eğer resim yoksa boş bir oda görüntüsü simüle ettirebiliriz
#     import numpy as np
#     resim = np.zeros((600, 800, 3), dtype="uint8")
#     cv2.putText(resim, "KAMERA BAĞLANTISI YOK", (200,300),  cv2.FONT_HERSHEY_SIMPLEX, 1,
#                 (255, 255, 255), 2 )
    
# if "ACIL DURUM" in analiz_sonucu:
#         resim = cv2.GaussianBlur(resim, (35,35),0)
#         cv2.rectangle(resim,(10,10), (790,590), (0,0,255),10)
#         renk=(0,0,255)
# else:
#         cv2.circle(resim,(40,40),15,(0,255,0),-1)
#         renk = (0,255,0)
 
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(resim,f"HASTA: {hasta_adi}",(70,50), font, 1, (255,255,255),2)
# cv2.putText(resim, f"DURUM: {analiz_sonucu}", (70, 100), font, 1, renk, 2)

# print(f"\nSistem Yanıtı: {analiz_sonucu}")
# cv2.imshow("Akilli Saglik Monitoru", resim)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

class DenizTemizleyici:
    def __init__(self):
        self.egitim_verisi = [[80, 8], [75, 9], [20, 3], [30, 2]]
        self.turler = ["Plastik Atik", "Plastik Atik", "Deniz Canlisi", "Deniz Canlisi"]
        self.rapor_dosyasi = "deniz_temizlik_raporu.txt"

    def mesafe_hesapla(self, p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

    def nesne_tani(self, veri):
        mesafeler = [self.mesafe_hesapla(veri, v) for v in self.egitim_verisi]
        return self.turler[mesafeler.index(min(mesafeler))]

    def veriye_yaz(self, nesne, durum):
        with open(self.rapor_dosyasi, "a", encoding="utf-8") as f:
            f.write(f"Tespit Edilen: {nesne} | Islem: {durum}\n")

robot = DenizTemizleyici()
print("---SUALTI TARAMA BASLATILDI")
parlaklik= int(input("Nesne parliklik oranı:(0-100) "))
form = int(input("Nesne yuvarlik skoru(1-10)"))

tespit = robot.nesne_tani([parlaklik,form])
islem = "TOPLANDI" if tespit == "Plastik Atik"else "SERBEST BIRAKILDI"
robot.veriye_yaz(tespit,islem)

kamera = cv2.imread("denizalti.jpg")
if kamera is None:
    kemara = np.zeros((500,700,3), dtype = "uint8")

kamera = cv2.GaussianBlur(kamera,(5,5),0)

if tespit == "Plastik Atik":
    cv2.rectangle(kamera, (150, 150), (450, 400), (0, 0, 255), 5)
    cv2.putText(kamera, "TEHLIKE: ATIK", (160, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
else:
    cv2.circle(kamera, (350, 250), 100, (0, 255, 0), 4)
    cv2.putText(kamera, "CANLI: GUVENLI", (160, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow("Akilli Deniz Temizleme Robotu", kamera)
print(f"Tespit: {tespit} -> {islem}")
cv2.waitKey(0)
cv2.destroyAllWindows()