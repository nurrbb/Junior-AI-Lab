from sklearn.linear_model import LogisticRegression  
import numpy as np

#  x -> çalışma saatleri y-> sonuçlar (1- geçti 2- kaldı )
# x = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
# y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) #5 tane 0 5 tane 1

# model = LogisticRegression()

# model.fit(x, y)

# tahmin = model.predict([[5.5]]) # tahmin süreci 5.5 saat çalışan biri dersten geçer mi
# olasilik = model.predict_proba([[5.5]]) # sonucun 1 olma yüzdesini verecek 

# print(f"Tahmin: {tahmin[0]} (Olasılık: {olasilik[0][1]})")

#Girdilerimiz: Kabuk parlaklığı (0-100), çıktı 1-> taze 2->bayat/bozulmuş

# urun_parlaklik = [[20], [45],[75],[90]]
# durum = [0, 0, 1, 1]

# buzdolabi_ai = LogisticRegression().fit(urun_parlaklik,durum)
# sonuc= buzdolabi_ai.predict([[80]])

# print(f"Ürün Durum Tahmini: {'Taze' if sonuc[0] == 1 else 'Çürük'} (Sınıf: {sonuc[0]}) ")

#Deniz biyolojisi. çıkardıkları ses frenkasnlarını -> türlerde

# #Verileri ->  ses frekansı, yüzme hızı (knot)
# deniz_kayitlari = [[15000, 25], [14000,22], [2000,10], [1500,8]]
# # 1-> yunus, 0->balina
# canli_turu = [1, 1, 0, 0]

# biyolog_asistan = LogisticRegression().fit(deniz_kayitlari, canli_turu)
# tespit = biyolog_asistan.predict([[14500,24]])

# print(f"Canlı Türü Tahmini: {'Yunus(Yüksek Frekans)' if tespit[0] == 1 else 'Balina (Düşük Frekans)'}")

#Ejderha evcilleştirme (dost/vahşi)
#veri : ateşin sıcaklığı, kanat hızı. 

# ejderha_verileri = [[1000,120], [800,100],[2000,300],[2500,400]]

# #dost mu 1 -> dost, 2-> vahşi

# dost_mu = [1 ,1, 0, 0]
# ejderha_tanımlama = LogisticRegression().fit(ejderha_verileri,dost_mu)

# tahmin = ejderha_tanımlama.predict([[900,110]])
# print(f"Ejderha Durumu: {'Dost Canlısı' if tahmin[0] == 1 else 'Vahşi Tür'}")


# # Girdi: [Derinlik (Y seviyesi), Lav Bloğu Sayısı]
# maden_verisi = [[-58, 10], [-60, 15], [50, 0], [10, 2]]
# elmas_var_mi = [1, 1, 0, 0] 

# maden_modeli = LogisticRegression().fit(maden_verisi, elmas_var_mi)

# sonuc = maden_modeli.predict([[-59, 12]])
# print(f"Maden Tahmini: {'ELMAS BULUNDU!' if sonuc[0] == 1 else 'Sıradan Taş'}")

#ANKA TÜY SAYISI, KARIŞTIRMA HIZI(TUR/DK)
iksir_testleri = [[2, 10], [3, 15], [10, 80], [12, 100]]
patlama_riski = [0, 0, 1, 1] # 1: patlar 

iksir_modeli = LogisticRegression().fit(iksir_testleri, patlama_riski)

tahmin = iksir_modeli.predict([[1, 5]])
print(f"İksir Durumu: {'Güvenli Karışım' if tahmin[0] == 0 else 'TEHLİKE: PATLAMA RİSKİ'}")