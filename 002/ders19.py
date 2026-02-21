# karar ağaçları 

#ağdan gelen verileri inceleyerek giriş denemesinin güvenli mi yoksa siber saldırımı

# from sklearn import tree 

#veri: paket boyutu(kb), istek sıklığı(sn), başarısız giriş sayısı, feature

# veriler =  [[500, 1, 0],[2000,50,10],[100,2,0],
#             [5000,100,25],[150,1,1], [4500,80,15]]

#sonuçlar

#güvenli :0 saldırı:1 
# sonuc = [0, 1, 0, 1, 0,1 ]

# siber_ai = tree.DecisionTreeClassifier().fit(veriler,sonuc)

# print("--- Ağ Güvenlik Duvarı  AI")
# boyut = int(input("Gelen veri paket boyutu(KB): "))
# istek = int(input("Saniye başına istek sayısı: "))
# hatali = int(input("Son 1 dakikadaki hatalı giriş denemesi: "))

# tespit = siber_ai.predict([[boyut,istek,hatali]])

# if tespit[0] == 1:
#     print("UYARI: Anomali tespit edildi! Protokol 404 devreye alınıyor: ERİŞİM ENGELLENDİ")
# else:
#     print("DURUM: Trafik temiz. kullanıcı doğrulanmış erişim sağladı.")

#gastronomi ai : yemeğin içeriğine bakarak hangi dünya mutfağına ait olduğunu tahmin eder

#veriler: baharat oranı, zeytinyağı kullanımı, deniz ürünü

# x = [[10,0,0],[2,1,0],[8,0,1],[1,1,0],[9,0,0],[3,1,1]]

#sonuçlar için 0: asya 1: akdeniz 2: okyanuz/egzotik

# y = [0,1,2,1,0,2]

# chef_ai = tree.DecisionTreeClassifier().fit(x,y)

# print("---Moleküler Mutfak Analizörü ---")

# baharat = int(input("Baharat yoğunluğu 1-10: "))
# yag= int(input("Zeytinyağı baskın mı(1 evet 0: hayır): "))
# deniz = int(input("Deniz ürünü içeriyor mu? (1 evet 2 hayır): "))

# tahmin = chef_ai.predict([[baharat,yag,deniz]])
# mutfaklar ={0: "Asya Mutfağı", 1: "Akdeniz Mutfağı", 2: "Egzotik ada mutfağı"}
# print(f"Teşhis: Bu tarif baskın olarak {mutfaklar[tahmin[0]]} karakteristiğine sahiptir.")

#finansal kredi uygunluk skorlaması

# from sklearn.linear_model import LogisticRegression as ai
# import numpy as np

#veri [aylık gelir, kredi skoru] = 2 feature 

# x = np.array([[10, 300], [45,800], [15,450],[60,950],[12,400],[80,990]])
# y = [0,1,0,1,0,1]

# finans_ai = ai().fit(x,y)

# gelir = float(input("Müşterinin aylık net geliri(bin tl): "))
# skor = int(input("Fideks puanı(1-1000): "))

# tahmin = finans_ai.predict([[gelir,skor]])
# olasilik = finans_ai.predict_proba([[gelir,skor]])

# print(f"Kredi Onay Durumu: {'ONAYLANDI' if tahmin[0]==1 else ' REDDEDİLDİ'}")
# print(f"Sistem Güven Endeksi: %{olasilik[0][tahmin[0]]*100:.2f}")

from sklearn.linear_model import LinearRegression
import numpy as np

# Veri: [Gübre Miktarı (kgDönüm), Sulama Saati]
# X = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25]]
# y = [200, 410, 615, 820, 1030] # Ürün kg

# agri_ai = LinearRegression().fit(X, y)

# gubre = float(input("Kullanılacak gübre miktarı (kg): "))
# su = float(input("Haftalık sulama süresi (saat): "))

# mahsul = agri_ai.predict([[gubre, su]])
# print(f"Projesiyon: Mevcut şartlarda sezon sonu tahmini hasat: {mahsul[0]:.1f} kg.")

#veri gövde çapı (cm)  -> tahmini yaş

cap = np.array([[10], [25], [50],[80],[120],[200]])
yas = np.array([5,15,40,75,130,250])
forest_ai = LinearRegression().fit(cap,yas)

print("--- Ağaç Bilimi AI ---")

cap = float(input("Ağacın yerden 1 metre yükseklikteki gövde çapı(cm): "))
yas_tahmini = forest_ai.predict([[cap]])
print(f"Saha raporu: Bu ağacın yaklaşık yaşı {int(yas_tahmini[0])} olarak hesaplandı")