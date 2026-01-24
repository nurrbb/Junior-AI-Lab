#(Nearest Neighbors) : arkadaşını söyle kim olduğunu söyleyeyim

# #Mesafe hesaplama
# def mesafe_1d(x1,x2):
#     return abs(x1 - x2) #mutlak değer = absolute value

# print(f"10 sayısı 15'e {mesafe_1d(10,15)} birim uzaklıktadır")

#iki sayı arasındaki mesafe küçükse
#bu iki veri birbiirne benzer

# sporcular = [[190,90],[200,100],[170,60],[165,55]]
# etiketler= ["Basketbol", "Basketbol", "Jimnastik","Jimnastik"]

# def olcekle(deger,maks):
#     return deger/maks

# print(f"Boy ölçekli: {olcekle(165,200)}")

# yeni_veri = [175,70]


# #çalışma saati, uyku saati
# data= [[10,8],[2,5],[8,6],[1,4]]
# labels = ["Geçti","Kaldı","Geçti","Kaldı"]

# def tahmin_et(saatler):
#     dist =[mesafe_hesapla(saatler,d) for d in data]
#     return labels[dist.index(min(dist))]

# print(f"5 saat çalışma 7 saat uyku sonucu: {tahmin_et([5,7])}")

#gelir-borç oranı 
# musteriler=[[5000,0.2],[2000,0.8],[8000,0.1]]
# durumlar = ["Düşük risk", "Yüksek risk","Düşük risk"]

# def kredi_tahmin(yeni_musteri):
#     dist= [mesafe_hesapla(yeni_musteri,m) for m in musteriler]
#     return durumlar[dist.index(min(dist))]
# print(f"yeni müşteri tahmin:{kredi_tahmin([4000,0.6])}")

#Hesap tutarı, masada kalma süresi dk

# veriler = [[150,30],[200,45],[800,120],[1000,150]]
# etiketler =["Ekonomik","Ekonomik","Cömert","Cömert"]

# def bahsis_tahmin(yeni_musteri):
#     dist =[mesafe_hesapla(yeni_musteri,d)for d in veriler]
#     sonuc  = etiketler[dist.index(min(dist))]
#     return f"Müşteri Segmenti: {sonuc}"

# print(bahsis_tahmin([900,130]))

def mesafe_hesapla(p1,p2):
    fark1 = (p1[0] - p2[0])**2
    fark2 = (p1[1] - p2[1])**2
    return (fark1 + fark2)** 0.5

#günlük paylaşım, takipçi sayısının /1000

# kullanicilar = [[1,0.5],[2,1],[15,500],[20,800]]
# tipler = ["Standart", "Standart", "Fenomen", "Fenomen"]

# def profil_analizi(profil):
#     mesafeler = [mesafe_hesapla(profil,k) for k in kullanicilar]
#     return tipler[mesafeler.index(min(mesafeler))]

# print(f"Bu hesap: {profil_analizi([18,600])}")

#veri tipimiz: beygir gücü/ağırlık ton

# araclar = [[500,15],[450,12],[600,1.5],[400,1.2]]
# tipler = ["Kamyon", "Kamyon", "Spor Araba","Spor araba"]

# def arac_tani(yeni_arac):
#     mesafeler = [mesafe_hesapla(yeni_arac,a) for a in araclar]
#     return tipler[mesafeler.index(min(mesafeler))]

# print(f"Araç Tipi: {arac_tani[550,2]}")

kullanicilar = [[0.05,0.001],[0.1,0.002],[0.9,0.85],[0.8,0.95]]
tipler=["Standart","Standart","Fenomen","Fenomen"]

def profil(profil,k=3):
    mesafeler = []
    for i in range(len(kullanicilar)):
     d = mesafe_hesapla(profil,kullanicilar[i])
     mesafeler.append((d,tipler[i]))
    
    mesafeler.sort()
    en_yakinlar =[mesafeler[0][1],mesafeler[1][1],mesafeler[2][1]]
    return max(set(en_yakinlar),key= en_yakinlar.count)

print(f"Yeni progil tahmini: {profil([0.85,0.9])}")
