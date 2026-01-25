# def kiyafet_secici():
#     print(" Akıllı Kıyafet Asistanına Hoş Geldin! ")
#     sicaklik = int(input("Bugün hava kaç derece? "))

#     if sicaklik > 25:
#         print("Tavsiye: Hava çok sıcak! Şort ve tişört giymelisin. ")
#     elif sicaklik >= 15 and sicaklik <= 25:
#         print("Tavsiye: Hava tam kararında. Bir sweatshirt alabilirsin.")
#     else:
#         print("Tavsiye: Hava oldukça soğuk! Kalın montunu ve atkını unutma.")

# kiyafet_secici()


# def meyve_tani():
#     print("Meyve dedektifine özelliklerini giriniz")
#     renk = input("Meyvenin rengi nedir? (kırmızı/turuncu): ").lower()
#     yuzey = input("Yüzeyi nasıl? (pürüzsüz/tırtıklı:) ").lower()


#     if renk == "kırmızı" and yuzey == "pürüzsüz":
#         print("Tahmin: Bu bir elma olabilir?")
#     elif renk == "turuncu" and yuzey == "tırtıklı":
#         print("Tahmin: Bu bir portakal olabilir.")
#     else:
#         print("Tahmin: Hmm bu meyceyi henüz veri tabanıma eklemediniz.")

# meyve_tani()

# def not_tahmin_et():
#     print("Not tahmin merkezine hoş geldiniz.")
#     saat = float(input("Haftada toplam kaç saat çalışıyorsun?" ))
#     tahmin = (saat *11) +10

#     if tahmin> 100:
#         tahmin = 100
        
#     print(f"Tahminimiz: Bu tempoyla yaklaşık {tahmin} alacaksın!")

# not_tahmin_et()

# def hayvan_tahmin():
#     print("Hayvan tahmin oyununa hoşgeldin")
#     print("Aklından bir hayvan tut: Balina, kedi, kartal veya penguen: ")
#     cevap1 = input("hayvanın kanatları var mı? (e/h) ").lower()

#     if cevap1 == "e":
#         cevap2 = input ("Bu hayvan uçabiliyor mu? (e/h): ").lower()
#         if cevap2 == "e":
#             print("bu kartal")
#         else:
#             print("penguendir")
#     else:
#         cevap2 = input("Bu hayvan suda mı yaşıyor? (e/H): ").lower()
#         if cevap2 == "e":
#             print("bu bir balina")
#         else:
#             print("bu bir kedi")
# hayvan_tahmin()

# kullanici_adi = "admin"; sifre = "yazilim123"; yuz_tanima_puanı = 95

# if kullanici_adi == "admin" and sifre == "yazilim123" and yuz_tanima_puanı > 90:
#     print("Kimlik doğrulandı. Gizli dosyalara erişim izni verildi.")
# else:
#     print("Erişim reddedildi! Güvenlik birimine haber veriliyor.")


def uyku_tahmincisi():

    print("Uyku tahmincisi")
    saat = int(input("Gece kaçta uyyorsun? örn 23 ya da 22 de "))
    kalan_sure = 7 +(24- saat)
    dongu_sayisi = kalan_sure/1.5
    print(f"Sabah 7 ye kadar {dongu_sayisi} kez derin uyku döngüsüne gireceksin")

uyku_tahmincisi()

