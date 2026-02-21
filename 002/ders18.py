# from sklearn import tree

#Verilerimiz (sıcaklık,yağmur var mı?(yağmur var mı yok mu 1: var , 0 yok))

# x =[[25,0], [30,1],[15,0],[10,1],[20,0],[5,0]]

# #etiketler sonuçlar = 0: evde kal 1: parka git
# y=[1,0,1,0,1,0]

# #karar ağacı modelini oluşturuyoruz

# model = tree.DecisionTreeClassifier()
# model = model.fit(x,y)

# #yeni bir durum tahmine etmesini isteleyim

# tahmin = model.predict([[22,0]])

# if tahmin[0] == 1:
#     print("Sonuç: AI parka gitmeni öneriyor!")
# else:
#     print("Sonuç: AI Robot evde kalıp kitap okumanı tavsiye ediyor!")

#verilerimiz yaprak rengi, yaprak kuruluğu
#rengi temsil eden sayılar: 0: kahve 1: sarı 2: yeşil
#kuruluk: 0:kuru 1:canlı

# x = [[2,1],[2,0],[1,0],[0,0],[1,1],[0,1]]

# #results: 0:su verme 1: su ver

# y =[0, 1, 1, 1, 0, 0]

# doktor = tree.DecisionTreeClassifier()
# doktor = doktor.fit(x,y)

# yeni_bitki= [[0,1]]
# tahmin = doktor.predict(yeni_bitki)

# print("--- Bitki doktoru teşhis sonucu ---")

# if tahmin[0] == 1:
#     print("Teşhis: bu bitkiye su verilmesi gereklidir.")
# else:
# print("Teşhis: Toprağı tekrar kontrol et, şu an su istemiyor.")

#özellikler (merhamet, kaos,zeka,cesaret) -> 0-10 arasında

# x =[
#     [10, 1, 8, 5], #bilge aziz
#     [2, 10, 3, 9], #babar istilacı
#     [5, 5, 10, 2], #stratejist
#     [0, 8, 9, 7], # kurnaz tiran
#     [8, 7, 5, 10], # halk kahramanı 
#     [1, 2, 4, 1], #korkak hain
#     [5, 2, 8, 6], #düzen muhafızı
#     [9, 9, 2, 10] #kaotik koruyucu
# ]

# #sonuçları: 0: kutsal son 1: karanlık son 2: huzurlu son 3: özgürlük sonu 4: yalnız son 

# y= [0, 1, 2, 1, 3, 4, 0, 3]

# rpg_ai = tree.DecisionTreeClassifier().fit(x,y)

# #test seçimler ortalaması
# yeni_oyuncu = [[4, 2, 9, 4]]

# tahmin = rpg_ai.predict(yeni_oyuncu)

# hikaye_sonlari = {
#     0: "Krallığın yeni koruyucusu oldun, adalet seninle yükseldi",
#     1: "Eski krallığı yıktın, korku içinde bir çağ başlattın",
#     2: "Savaşlardan uzak, tüm kozmik sırları bilen bir bilge olarak emekli oldun.",
#     3: "Halkı özgürleştirdin ama ardında koca bir enkaz bıraktın",
#     4: "Kimse seni hatırlamadı, tarihin tozlu sayfaları içerisinde kayboldun"
# }
# print(f"----DESTAN SONU----\n{hikaye_sonlari[tahmin[0]]}")


#######################################################################

# from sklearn.linear_model import LogisticRegression
# import numpy as np

# #akıllı spam filtresi
# #veri setimiz = mesajdaki acil, bedava, son şans, nakit gibi kelimelerin toplam sayısı

# x = np.array([0,1,2,5,7,10,12,15]).reshape(-1,1)

# #etiket: 0: güvenli mesaj 1: spam(istenmeyen )

# y= [0,0,0,1,1,1,1,1]

# spam_dedektoru = LogisticRegression().fit(x,y)

# yeni_mesaj = [[4]]
# tahmin= spam_dedektoru.predict(yeni_mesaj)
# olasilik = spam_dedektoru.predict_proba(yeni_mesaj)

# print(f"Mesaj Durumu: {'Spam!' if tahmin[0] == 1 else 'Güvenli'}")
# print(f"Spam olma ihtimali: %{olasilik[0][1] * 100:.2f}")

from sklearn.linear_model import LogisticRegression

# # Veriler (X): [Yakıt Miktarı (Ton), Roket Ağırlığı (Ton)]
# x = [
#     [100, 50],  # Bol yakıt, hafif roket  Başarılı
#     [80, 70],   # Az yakıt, ağır roket Başarısız
#     [120, 80],  # Dengeli  Başarılı
#     [50, 40],   # Çok az yakıt  Başarısız
#     [90, 60],   # Sınırda  Başarılı
#     [60, 90]    # Çok ağır, az yakıt  Başarısız
# ]

# # Sonuçlar (y): 1: Yörüngeye ulaştı, 0: Başarısız oldu
# y = [1, 0, 1, 0, 1, 0]
# model = LogisticRegression().fit(x, y)
# yeni_gorev = [[85, 55]]
# tahmin = model.predict(yeni_gorev)
# sans = model.predict_proba(yeni_gorev)

# print("--- Görev Kontrol Raporu ---")
# if tahmin[0] == 1:
#     print(f"SONUÇ: Fırlatma Onaylandı! Başarı Şansı: %{sans[0][1] * 100:.1f}")
# else:
#     print(f"SONUÇ: Fırlatma İptal! Risk Çok Yüksek. Başarı Şansı sadece: %{sans[0][1] * 100:.1f}")

#verilerimiz ses frekansı, ve knot cinsinden yüzme hızı

x = [[15000,25],[14000,22],[2000,10],[1500,8]]

# 1 yunus 0 balinadır

y = [1,1,0,0]

biyolog_asistan = LogisticRegression().fit(x,y)
tespit = biyolog_asistan.predict([[5000,8]])

print(f"Canlı Türü tahmini: {'Yunus' if tespit[0]==1 else 'Balina'}")