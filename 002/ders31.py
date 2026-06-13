# # #(NLP): Doğal dil işleme 

# # #tokenization: token 
# # #stop-words: 


# # class AkilliDuyguAnalizi:

# #     def __init__(self):
# #         self.pozitif_sozluk =["başarılı", "muazzam", "harika", "tavsiye","efsane"]
# #         self.negatif_sozluk = ["rezalet", "kötü", "berbat", "sıkıcı", "hayal"]
# #         self.tersine_cevirenler =["değil", "yok","etmedim", "değildi"]

# #     def metin_skoru_hesapla(self,yorum):
# #         tokenler = yorum.lower().split()
# #         duygu_skoru = 0

# #         for index in range(len(tokenler)):
# #             kelime = tokenler[index]

# #             if kelime in self.pozitif_sozluk:

# #                 if index +1 < len(tokenler) and tokenler[index+1] in self.tersine_cevirenler:
# #                     duygu_skoru -= 2
# #                 else:
# #                     duygu_skoru +=2
            
# #             elif  kelime in self.negatif_sozluk:
# #                 if index+1 < len(tokenler) and tokenler [index+1] in self.tersine_cevirenler:
# #                     duygu_skoru += 2
# #                 else:
# #                     duygu_skoru -= 2

# #         return self.sonuc_bildir(duygu_skoru)
            
# #     def sonuc_bildir(self,skor):
# #      if skor > 0:
# #       return f"Skor: {skor} -> Olumlu yorum"
# #      elif skor < 0 :
# #        return f"Skor: {skor} -> Olumsuz Yorum"
# #      return f"Skor: {skor} -> Nötr/tarafsız Yorum"
        
# # analizor = AkilliDuyguAnalizi()
# # print(analizor.metin_skoru_hesapla("Film kesinlikle berbat değil oldukça başarılı"))
# # print(analizor.metin_skoru_hesapla("Senaryo harika değildi beklentilerimi karşılamadı"))

# class AsistanBot:
#     def __init__(self):
#         self.niyet_sozlukleri = {
#             "selamlama" : ["merhaba", "selam", "hey", "günaydın"],
#             "hava_durumu" : ["hava", "yağmur", "sıcak", "derece", "soğuk"],
#             "yardim": ["yardım", "destek", "sorun", "çalışmıyor"]
#             }
        
#     def niyet_tespit_et(self, kullanici_metni):
#         kelimeler = kullanici_metni.lower().replace("?", "").split()
#         niyet_skorlari = {"selamlama": 0, "hava_durumu":0 , "yardim": 0}

#         for kelime in kelimeler:
#             for niyet, anahtar_kelimeler in self.niyet_sozlukleri.items():
#                 if kelime in anahtar_kelimeler:
#                     niyet_skorlari[niyet] += 1
            
#             en_yuksek_niyet = max(niyet_skorlari, key= niyet_skorlari.get)
#             en_yuksek_skor = niyet_skorlari[en_yuksek_niyet]

#             if en_yuksek_skor == 0:
#                 return "Bot: Üzgünüm, ne demek istediğinizi tam olarak anlayamadım."
#             return self.cevap_uret(en_yuksek_niyet)
        
#     def cevap_uret(self, niyet):
#         if niyet == "selamlama":
#             return "Bot: Merhaba! Size nasıl yardımcı olabilirim?"
#         elif niyet == "hava_durumu":
#             return "Bot: Bugün hava parçalı bulutlu ve 22 derece olacak"
#         elif niyet == "yardim":
#             return "Bot: Endişelenmeyin, destek ekibimize hemen bir kayıt açıyorum."

# bot = AsistanBot()
# print(bot.niyet_tespit_et("Selam bugün hava nasıl olacak dışarısı sıcak mı?"))
# print(bot.niyet_tespit_et("Sistem çalışmıyor acil yardım gerekli."))

class DestekYonlendirici:
    def yonlendir(self, musteri_mesaji):
        mesaj = musteri_mesaji.lower()
        
        if "kargo" in mesaj or "teslimat" in mesaj:
            return "Sistem: Lojistik Departmanına Aktarılıyor..."
            
        elif "iade" in mesaj or "para" in mesaj:
            return "Sistem: Muhasebe Departmanına Aktarılıyor..."
            
        elif "şifre" in mesaj or "giriş" in mesaj:
            return "Sistem: Teknik Destek Departmanına Aktarılıyor..."
        else:
            return "Sistem: Genel Müşteri Temsilcisine Bağlanıyorsunuz..."

bot = DestekYonlendirici()
print(bot.yonlendir("Merhaba, kargom hala gelmedi yardımcı olur musunuz?"))
print(bot.yonlendir("Şifremi unuttum hesabıma giremiyorum!"))
print(bot.yonlendir("Ürünü beğenmedim, iade etmek istiyorum."))