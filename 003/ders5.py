# puan = 40

# if puan > 50: #eğer puan elliden yüksek ise 
#     print("Geççtiniz") #geçtiniz yazısını bastır
# else:  # diğer durumlarda
#     print("Kaldınız.")


# renk = "Kırmızı"
# if renk == "Kırmızı":
#     print("Dur!")
# else:
#     print("Geçebilirsin")

# sayi = int(input("Bir sayı gir: "))

# if sayi % 2 == 0: # % = bölümden kalanı alır.  
#     print("Bu sayı çifttir")
# else: # kalan 1 dir. 
#     print("Bu sayı tektir.")

# sayi = int(input("Bir sayı girin:"))
# if sayi > 0:
#     print("Bu sayı pozitiftir")
# else:
#     print("bu sayı negatiftir")

# sayi1 = int(input("1. Sayı: "))
# sayi2 = int(input("2. Sayı: "))

# if sayi1 > sayi2:
#     print("Birinci sayı daha büyük.")
# else:
#     print("Ya İkinci sayı daha büyük ya da birbirlerine eşittirler")

# yas = int(input("Yaşın kaç?"))
# if yas >= 18:
#     print("Ehliyet için başvuru yapabilirsin")
# else: 
#     print("Maalesef, ehliyet için henüz küçüksün")

# sicaklik = float(input("Oda sıcaklığı: "))
# if sicaklik > 30:
#     print("Klima çalıştırılıyor")
# else:
#     print("Sıcaklık normal.")

# saat = int(input("Kaç saat uyudun?: "))

# if saat < 8:
#     print("Bugün belki biraz yorgun hissedebilirsin")
# else:
#     print("Harika! Uykunu almışsın!")

# hiz= int(input("Hızın nedir?"))

# if hiz > 120 : # 120 üzeri
#     print("Hız sınırını aştın! Ceza kesildi.")
# else:
#     print("İyi yolculuklar.")


# kullanici = input("Kullanıcı adı: ")

# if kullanici == "admin":
#     print("Sisteme hoş geldiniz yetkili.")
# else:
#     print("Standart kullanıcı girişi yapıldı.")


# veri = input("Bir şeyler yaz: ")

# if veri == "":
#     print("Neden hiçbir şey yazmadın ki?!")
# else:
#     print("Mesajın alındı!")

# 500 liranın üzerindeyse yapılan alışveriş indirim kazanılan bir senaryomuz mevcuttu.

# toplam = float(input("Yaptığınız toplam alışveriş tutarını giriniz: "))
# if toplam >= 500:
#     print("Tebrikler!500 tl sınırını geçtiğiniz için indirim kazandınız.")
# else: 
#     print("Maalesef inidirim için harcamanız gereken minimum tutuarın altındasınız.")


# cevap = input("Ders çalışmak istiyor musun? (evet/hayır)") #metin türü ile (string) iş yapıyoruz

# if cevap == "evet":
#     print("Başarılar dilerim!")
# else: 
#     print("Biraz mola vermek de iyidir.")

# tutar = int(input("Sepet tutarı: "))
# if tutar >= 250 : 
#     print("Kargo bedava.!")
# else: 
#     print("Kargo bedava kampanyasının altındasınız")

derece = int(input("Suyun sıcaklığı: "))

if derece <= 0:
    print("Su buz yani katı haldedir.")
else:
    print("Su sıvı haldedir.") 