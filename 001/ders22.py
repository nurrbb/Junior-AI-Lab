# from sklearn import tree
#Bugün dışarı çıkmalı mıyım?
#0: yağmurlu 1: güneşli, sıcaklık(derece)
# hava_durumlari = [[0,15],[0,20],[1,25],[1,30],[0,10],[1,18]]
#0: çıkma 1: çık
# sonuc = [0, 0, 1, 1, 0, 1 ]

# ai_modelimiz = tree.DecisionTreeClassifier().fit(hava_durumlari,sonuc)

#kullanıcıdan bilgi alıyorz

# print("-----Dışarı Çıkma Karar Mekanizması")
# hava = int(input("Hava nasıl? (0: yağmurlu, 1: güneşli)"))
# derece = int(input("Sıcaklık kaç derece? "))

# tahmin = ai_modelimiz.predict([[hava,derece]])
# if tahmin[0]==1:
#     print("Sonuç: Kesinlikle dışarı çıkmalısın!")
# else:
#     print("Sonuç: Evde kalıp kod yazmak daha iyi bir fikir.")

#oyun karakteri sınıflandırıcı 

# veri: güç,büyü,hız

# veri = [[10,2,5],[9,1,4],[2,10,3],[3,9,2],[5,4,10],[4,3,9]]

#türler 0: savaşçı, 1: büyücü, 2: okçu

# turler = [0, 0, 1, 1, 2,2 ]

# rpg_ai = tree().fit(veri,turler)

# print("----RPG Karakter Testi----")
# guc = int(input("Güç(1-10): "))
# buyu = int(input("Büyü(1-10): "))
# hiz = int(input("Hız(1-10): "))

# tahmin = rpg_ai.predict([[guc,buyu,hiz]])
# siniflar =["Savaşçı", "Büyücü", "Okçu"]
# print(f"Senin sınıfın: {siniflar[tahmin[0]]}")

from sklearn.tree import DecisionTreeClassifier as tree

#evcil hayvan tahmin modeli
#ev büyüklüğü, boş vakit, bütçe, gürültü toleransı (1 sessiz 5 sesli)

veriler =[ [1,1,1,5], [1,2,1,4], [2,1,2,5],
           [2,2,2,3], [1,3,2,4], [2,3,1,2],
           [3,3,3,3], [4,2,4,4], [2,4,3,3],
           [4,5,5,2], [5,4,4,1], [5,5,5,1],
           [1,4,3,1], [2,5,4,2], [3,4,3,1],
           [3,2,2,4], [4,3,3,5], [3,4,2,4]]

# 0: balık 1: hamster 2: kedi 3: köpek 4: papağan 5: tavşan

hayvanlar = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
oneri_ai = tree().fit(veriler,hayvanlar) 
print("---Evcil Hayvan öneri sistemine hoşgeldin ---")
print("Lütfen sorulara 1 ile 5 arası puan ver. ")

ev= int(input("Evin ne kadar büyük(1 küçük 5 büyük): "))
vakit = int(input("Günde ne kadar vakit ayırabilirsin? "))
butce = int(input("Aylık bütçen ne kadar?: "))
ses = int(input("Sese ne kadar dayanabilirsin? (1 - rahatsız etmez 5- çok eder): "))
tahmin = [[ev,vakit,butce,ses]]
tahmin_no = oneri_ai.predict(tahmin)[0] 

sonuclar = [["Balık: sessiz ve bakımı kolay"],
            ["Hamster: Az yer kaplayan sevimli dost"],
            ["Kedi:Bağımsız ve sevgi dolu"],
            ["Köpek:Sadık ve ilgi ister "],
            ["Papağan: konuşkan ve sosyal"],
            ["tavşan sessiz neşe"]]
onerilen = sonuclar[tahmin_no]
print(f"Önerimiz: {onerilen}")
