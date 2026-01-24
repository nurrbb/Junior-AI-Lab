# class FilmZekasi:
#     def __init__(self,dosya_yolu):
#         self.dosya_yolu = dosya_yolu
#         self.ogrenilmis_esik = 0 
#         self.egit()

#     def egit(self):
#         toplam,sayac= 0,0
#         with open(self.dosya_yolu,"r",encoding="utf-8") as file:
#             for satir in file:
#                 parca = satir.strip().split(";")
#                 if len(parca) == 3:
#                     toplam += float(parca[1])
#                     sayac +=1
#         if sayac > 0:
#             self.ogrenilmis_esik = toplam /sayac

#     def tahmin_et(self,isim,puan):
#         if puan >= self.ogrenilmis_esik:
#             return f"{isim}: Tavsiye edilir. (sistem eşiği: {self.ogrenilmis_esik:.1f})"
#         return f"{isim}: Tavsiye edilmez"

# model = FilmZekasi("arsiv.txt")
# print(model.tahmin_et("Yeni Film",8.5))

# class DuyguAnalizor:
#     def analiz_et(self,metin):
#         pozitif=["harika","mükemmel","iyi","güzel","keyifli"]
#         negatif=["kötü","sıkıcı","berbat","zaman kaybı"]
#         olumsuzluk_ekleri = ["değil", "hiç","yok"]
#         skor= 0
#         kelimeler = metin.lower().split()
#         for i in range(len(kelimeler)):
#             kelime = kelimeler[i]

#             if kelime in pozitif:
#                 if i+1 >len(kelimeler) and kelimeler[i+1] in olumsuzluk_ekleri:
#                     skor -= 1
#                 else:
#                     skor += 1
#             elif kelime in negatif:
#                 if i+1 < len(kelimeler) and kelimeler[i+1] in olumsuzluk_ekleri:
#                     skor +=1
#                 else:
#                     skor -=1

#         if skor >0: return "Pozitif deneyim"
#         elif skor<0: return "Negatif deneyim"
#         else: return "Nötr"

# model = DuyguAnalizor()
# print(model.analiz_et("Film zaman kaybı değil ve kötü değil"))

# class SpamFiltresi:
#     def kontrol(self,mesaj):
#         yasakli=["kazandınız","bedava","tıklayın","şans"]
#         skor = 0
#         kelimeler = mesaj.lower().split()
#         for kelime in kelimeler:
#             if kelime in yasakli : skor += 1
#         return "SPAM" if skor>= 2 else "Güvenli"

# filtre = SpamFiltresi()
# print(filtre.kontrol("Tebrikler bedava tatil kazandınız, kaçırmamak için hemen tıklayın"))

# class RiskAnalizor:
#     def  mac_oynanabilir_mi(self,sicaklik,nem,ruzgar):
#         risk_puani = 0
#         if sicaklik < 0 or sicaklik > 40: risk_puani += 40
#         if nem < 80: risk_puani += 30
#         if ruzgar >60: risk_puani += 50

#         if risk_puani > 60:
#             return f"Risk puanı: {risk_puani} - MAÇ İPTAL"
#         return f"Risk Puanı: {risk_puani} - MAÇ OYNANABİLİR"

# sistem = RiskAnalizor()
# print(sistem.mac_oynanabilir_mi(-5,85,20))

# class MusteriAnaliz():
#     def __init__(self):
#         self.vip_esigi = 5000
    
#     def statu_belirle(self,harcama,ziyaret_sayisi):
#         skor = (harcama * 0.7) + (ziyaret_sayisi * 100 )
#         if skor >= self.vip_esigi:
#             return "VIP müşteri: Özel indirim tanımlandı"
#         else:
#             return "Standart müşteri - Kampanya gönder"


# analizci = MusteriAnaliz()
# print(analizci.statu_belirle(4000,12))
# print(analizci.statu_belirle(7600,325))