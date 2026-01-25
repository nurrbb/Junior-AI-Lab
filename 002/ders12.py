# class Film:
#     def __init__(self,isim,puan,kategori):
#         self.isim = isim
#         self.puan = puan
#         self.kategori = kategori

# print("-- Film yönetim merkezine hoş geldiniz --")

# adet = int(input ("Kaç tane yeni film girişi yapmak istiyorsunuz?"))

# for i in range(adet):
#     print(f"\n{i+1}. Filmin detaylarını hazırlayın:")
#     isim = input("Filmin adı: ")
#     puan = input ("IMDB puanı: ")
#     kategori = input("Filmin kategorisi: ")

#     yeni_film = Film(isim,puan,kategori)

#     with open("arsiv.txt","a", encoding = "utf_8") as  dosya:
#         satir = yeni_film.isim + " ; " + yeni_film.puan + " ; " + yeni_film.kategori
#         dosya.write(satir)
#         print(f">>>'{yeni_film.isim}' başarıyla arşive eklendi.")

# print("FİLM ARŞİV ANALİZİ")

# toplam_puan = 0
# film_sayacı = 0

# with open("arsiv.txt","r",encoding="utf-8") as dosya:
#     for satir in dosya:
#         parca = satir.strip().split(";")
        
#         if len(parca) == 3:
#             f = Film(parca[0], parca[1], parca[2])
#             print(f"İnceleniyor:{f.isim}...")

#             toplam_puan = toplam_puan + float(f.puan)
#             film_sayacı = film_sayacı +1

# if film_sayacı >0:
#     print(f"SONUÇ: ARŞİVİNİZDEKİ {film_sayacı} filmin genel ortalaması: {toplam_puan / film_sayacı}") 
# 
# 

# class Ogrenci:
#     def __init__(self,ad,soyad,notu):
#         self.ad = ad
#         self.soyad = soyad
#         self.notu = notu

# print("\n -- ÖĞRENCİ KAYIT PANELİ --")
# ad = input("Öğrenci adı: ")
# soyad = input("Soyad: ")
# notu = input ("Sınav Notu: ")

# yeni_ogrenci = Ogrenci(ad,soyad,notu)

# with open("sinif.txt","a",encoding= "utf-8") as dosya:
#     dosya.write(yeni_ogrenci.ad + " ; " + yeni_ogrenci.soyad  + " ; " + yeni_ogrenci.notu)


# print("SINIF NOT ANALİZİ")

# with open("sinif.txt","r",encoding="utf-8") as dosya:
#     for satir in dosya:
#         ogrenci = satir.strip().split(";")
#         if len(ogrenci) == 3:
#             if int(ogrenci[2]) >= 60:
#                 print(f"{ogrenci[0]} {ogrenci[1]} dersi geçti.")
#             else:
#                 print(f"{ogrenci[0]}{ogrenci[1]} dersten kaldı.")

# class Kitap:
#     def __init__(self,isim,yazar,sayfa):
#         self.isim = isim
#         self.yazar = yazar
#         self.sayfa = sayfa

# print("--- Kütüphane Yönetim Sistemi ---")

# kitap_sayisi = int(input("Kütüphaneye kaç yeni kitap eklemek istersiniz? : "))

# for i in range (kitap_sayisi):
#     print(f"{i+1}. kitabın bilgileri: ")
#     ad = input("Kitap adı: ")
#     yazar = input("Yazar adı: ")
#     sayfa = input("Sayfa sayısı: ")

#     yeni_kitap = Kitap(ad,yazar,sayfa)

#     with open("kutup.txt","a",encoding="utf-8") as dosya:
#         satir = yeni_kitap.isim +";"+yeni_kitap.yazar+";"+yeni_kitap.sayfa
#         dosya.write(satir)
#         print(f"{yeni_kitap.isim} rafa yerleştirildi.")

# print("Kütüphane analizi başlatılıyor")

# toplam_sayfa = 0
# kitap_sayaci =0 

# with open("kutup.txt", "r", encoding = "utf-8") as file:
#     for satir in file:
#         parcalar = satir.strip().split(";")
#         if len(parcalar) == 3:
#             yeni_kitap = Kitap(parcalar[0],parcalar[1],parcalar[2])
#             toplam_sayfa = toplam_sayfa + int(yeni_kitap.sayfa)
#             kitap_sayaci = kitap_sayaci +1
