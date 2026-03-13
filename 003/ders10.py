# break  = dur
#continue = atla

# for kurabiye in range (1,11):
#     if kurabiye == 5:
#         print("Eyvah! Fırın bozuldu!")
#         break
#     print(kurabiye, ". kurabiye pişti")

# for sayi in range (1,7): # 1 2 3 4 5 6
#     if sayi == 5:
#          break
#     print(sayi)

# for sayi in range(1,6): # 1 2 3 4 5
#     if sayi == 3:
#         continue
#     print("Sayı:", sayi)

# for kat in range(1,21):
#     if kat == 13:
#         continue
#     print("Şu anki kat: ", kat)

# sifre = "ai123"
# hak = 3

# while hak > 0:
#     deneme = input("Kapı şifresini giriniz: ")
#     if deneme == sifre:
#         print("Şifre doğru kapı açılıyor")
#         break # şifre doğruysa döngüyü kırdı
#     else:
#         hak = hak -1
#         print("Hatalı şifre! Kalan: ",hak,)
# if hak == 0:
#     print("Çok fazla hatalı deneme! Sistem kitlendi") 


# print("Geri sayım başlıyor...")
# for saniye in range(10,0,-1):
#     print("Fırlatmaya son ",saniye," saniye")
#     durum = input("Durdurmak için 'iptal yazın(Devam için enter): ")
#     if durum == "iptal":
#         print("Fırlatma durduruldu! Görev iptal.")
#         break
#     else:
#         print("Roket fırlatıldı!")

# for i in range(1,11):
#     if i == 5:
#         print("5. şınav: Mola ver su iç")
#         continue
#     print(i,". şınav çekildi")

# print("Pizza Hazırlama Makinesi")

# for i in range(1,6):
#     malzeme = input("Eklemek istediğin malzemeyi yaz: ")
#     if malzeme == "soğan":
#         print("Müşteri soğan sevmiyor! Bu malzemeyi atlıyoruz")
#         continue
#     elif malzeme == "kaşar":
#         print("Muhteşem! Olmazsa olmaz!")
#     elif malzeme == "balık":
#         print("Balıklı pizza mı olur? Bu pizza yenmez üzgünüm")
#         break
#     print(malzeme, "hamurun üzerine eklendi")


# for i in range(3): # 0 1 2 
#     print(i, "Hi!")

print("Hazine Avı")

for adim in range(1,11):
    secim = input(f"{adim}. adımdasın. (ilerle / dur): ")

    if secim == "dur":
        print("Korktun! Oyun bitti")
        break
    if adim == 4:
        print("Dikkat et çukur! Üstünden atlıyorsun")
        continue
    if adim == 7:
        print("Ejderha! Kaçarsan kaybedersin.")
        hamle = input("Savaş mı?(e/h): ")
        if hamle != "e":
            print("Ejderha seni yakaladı!")
            break
        print("Güvenle ilerledin!")
    
    if adim == 10:
        print("Tebrikler! Hazineye ulaştın!")