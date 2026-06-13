# class OneriSistemi:
#     def __init__(self):
#         self.film_veritabani = {
#             "Matrix": ["aksiyon", "bilim kurgu", "distopya"],
#             "Yüzüklerin Efendisi": ["fantastik", "macera", "aksiyon"],
#             "Gülse Birsel Dizisi": ["komedi", "aile", "yerli"],
#             "Yıldızlararası": ["bilim kurgu", "uzay", "dram"],
#             "John Wick": ["aksiyon", "suikast", "silah"]
#         }
        
#     def film_oner(self, kullanici_gecmisi):
#         sevilen_turler = []
#         for izlenen_film in kullanici_gecmisi:
#             if izlenen_film in self.film_veritabani:
#                 sevilen_turler.extend(self.film_veritabani[izlenen_film])
                
#         film_skorlari = {}
#         for film, etiketler in self.film_veritabani.items():
#             if film not in kullanici_gecmisi:
#                 ortak_nokta = len([etiket for etiket in etiketler if etiket in sevilen_turler])
#                 film_skorlari[film] = ortak_nokta
                
#         en_iyi_oneri = max(film_skorlari, key=film_skorlari.get)
        
#         return f"Sistem Önerisi: İzleme geçmişinize göre '{en_iyi_oneri}' tam size göre"

# netflix_bot = OneriSistemi()
# kullanici_izledikleri = ["Matrix", "John Wick"]
# print("Geçmiş:", kullanici_izledikleri)
# print(netflix_bot.film_oner(kullanici_izledikleri))

# class AkilliSepet:
#     def __init__(self):
#         self.diger_musteriler = [
#             ["telefon", "kılıf", "kulaklık"],
#             ["laptop", "mouse", "çanta"],
#             ["telefon", "ekran koruyucu", "kılıf"],
#             ["kitap", "kahve", "kupa", "ayraç"]
#         ]
    
#     def eksik_urunu_bul(self,benim_sepetim):
#         oneri_puanlari = {}

#         for musteri_sepeti in self.diger_musteriler:
#             ortak_urunler = [urun for urun in benim_sepetim if urun in musteri_sepeti]

#             if len(ortak_urunler) > 0:
#                 for urun in musteri_sepeti:
#                     if urun not in benim_sepetim:
#                         if urun in oneri_puanlari:
#                             oneri_puanlari[urun] +=1
#                         else:
#                             oneri_puanlari[urun] = 1

#         if oneri_puanlari:
#             tavsiye = max(oneri_puanlari, key=oneri_puanlari.get)
#             return f"Sepetinize eklemek ister misiniz? : {tavsiye}"    

# amazon_bot = AkilliSepet()
# print("Benim Sepetim: ['laptop']")
# print(amazon_bot.eksik_urunu_bul(["laptop"]))


import random
class YapaySairGPT:
    def __init__(self):
        self.kelime_agimiz = {
            "gökyüzü": ["mavi", "karanlık", "bulutlu", "ağlıyor"],
            "mavi": ["deniz", "gözlerin", "gibi", "bir"],
            "deniz": ["dalgalı", "sakin", "ve", "derin"],
            "gibi": ["güzel", "sonsuz", "sessiz", "soğuk"],
            "sonsuz": ["bir", "rüya", "karanlık", "gökyüzü"],
            "bir": ["rüya", "deniz", "akşam", "masal"]
        }
        
    def siir_yaz(self, baslangic_kelimesi, uzunluk):
        if baslangic_kelimesi not in self.kelime_agimiz:
            return "Sistem: Bu kelime ile nasıl başlayacağımı bilmiyorum."
            
        siir = [baslangic_kelimesi]
        suanki_kelime = baslangic_kelimesi
        
        for _ in range(uzunluk - 1):
            if suanki_kelime in self.kelime_agimiz:
                siradaki = random.choice(self.kelime_agimiz[suanki_kelime])
                siir.append(siradaki)
                suanki_kelime = siradaki
            else:
                break
                
        return " ".join(siir).capitalize() + "..."

sair_bot = YapaySairGPT()
print(" Yapay Zeka Şiir Üretiyor (Çıktılar her seferinde değişir):")
print(sair_bot.siir_yaz("gökyüzü", 2))
print(sair_bot.siir_yaz("mavi", 1))