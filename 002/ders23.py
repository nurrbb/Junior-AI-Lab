# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn import tree

# #veri seti(uyku,su,antreman yoğunluğu,nabız)
# x_athlete = np.array([
#     [8.0, 2.5, 7.0, 65.0],
#     [6.0, 1.5, 9.0, 75.0],
#     [7.5, 3.0, 5.0, 60.0],
#     [5.0, 1.0, 8.0, 80.0],
#     [9.0, 2.0, 4.0, 55.0]
# ])
# #performas puanı (0-100)
# y_athlete = np.array([85.0, 60.0, 92.0, 50.0, 95.0])
# athlete_model = LinearRegression().fit(x_athlete, y_athlete)

# #uyku, yoğunluk,kas ağrısı seviyesi
# x_training = np.array([
#     [8.0, 7.0, 4.0],  # İyi uyku, orta yoğunluk, orta ağrı
#     [6.0, 9.0, 8.0],  # Az uyku, yüksek yoğunluk, yüksek ağrı
#     [7.5, 5.0, 2.0],  # Normal uyku, düşük yoğunluk, az ağrı
#     [5.0, 8.0, 9.0],  # Kötü uyku, yüksek yoğunluk, çok ağrı
#     [9.0, 4.0, 1.0],  # Çok uyku, düşük yoğunluk, ağrı yok
#     [7.0, 6.0, 5.0]   # Ortalama her şey
# ])
# # veri setimiz X_ ; result y ile isimlendirme yapılır

# # 0: aktif dinlenme, 1: hafif kardiyo, 2: güç antremanı

# y_training = np.array([2, 0, 1, 0, 2, 1])

# training_ai = tree.DecisionTreeClassifier().fit(x_training,y_training)

# def smart_athlete_app():
#     print("*" * 75)
#     print("Smart Athlete - Günlük Performans Asistanı")
#     print("*" * 75)

#     uyku = float(input("Dün gece kaç saat uyudunuz?: "))
#     su = float(input("Bugün kaç litre su içtiniz?: "))
#     yogunluk = float(input("Dünkü antreman yoğunluğunuzu 1 ile 10 arasında puanlayınız: "))
#     nabiz = float(input("Şu anki durgun anda nabzınız(BPM): "))
#     agri = float(input("Şu anki kas ağrısı seviyenizi 1 ile 10 arasında puanlandırınız: "))

#     tahmin = athlete_model.predict([[uyku,su,yogunluk,nabiz]])[0]

#     antreman_tipi_id = training_ai.predict([[uyku,yogunluk,agri]])[0]

#     #Antreman sözlüğü
#     antreman_tipleri ={
#         0: "Aktif Dinlenme/ yoga / esneme (vücudun toparlanmaya ihtiyacı var)",
#         1: "Hafif Kardiyo / Teknik Çalışma (Orta tempo yağ yakımı )",
#         2: "Yüksek yoğunluklu güç antremanı"
#     }

#     print("*" * 75)
#     print(f"AI Analizi: Bugünkü tahmini antreman performansınız: {tahmin:.1f} / 100")

#     if tahmin >= 80:
#         print("Durum: Harika! Vücudun tam kapasite çalışmaya hazır.")
#     elif tahmin >= 60:
#         print("Durum: Normal Standart antreman programına sabit kalmalısın")
#     else:
#         print("Durum: Riskli! Aşırı yorgunluk belirtisi, dinlenmeye odaklan.")

#     print(f" AI Antreman Reçetesi: \nÖnerilen Program: {antreman_tipleri[antreman_tipi_id]}")
#     print("-" * 75)

# smart_athlete_app()


# # formatlama = formatted string literals

# yas = "başka bir"

# print(f"yaşı: {yas}")

# print(f"|{yas:<10}|")# |Başka bir          |
# print(f"|{yas:>10}|")
# print(f"|{yas:^10}|")

# print(f"{yas:=^30}")

# sonuc = 32924.3274
# print(f"Sonuç: {sonuc:,.2f}")

import numpy as np
import time
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn import tree

#eta  = estimated time of arrival = tahmini varış zamanı/saati
#mesafe, trafik(1-10), hava(1 açık ,2 yağmurlu ,3 karlı)

#Lineer Regresion modeli
x_eta = np.array([
    [5.0, 2, 1], [15.0, 8, 2], [2.0, 1, 1], 
    [25.0, 9, 3], [10.0, 5, 1], [20.0, 7, 2]
])
y_sure = np.array([15, 65, 8, 120, 35, 85])

eta_model = LinearRegression().fit(x_eta,y_sure)

#Optimal araç seçimi (karar ağacı)
#ağırlık(kg), mesafe(km), hava durumu(1-3)
x_arac = np.array([
    [1.5, 5.0, 1], [50.0, 15.0, 2], [0.5, 2.0, 1], 
    [150.0, 50.0, 3], [15.0, 10.0, 1], [80.0, 20.0, 2],
    [3.0, 25.0, 3] 
])

#0: moto-kurye, 1: hafif ticari, 2 kamyon
y_arac = np.array([0, 1, 0, 2, 0, 1, 1])
arac_model = tree.DecisionTreeClassifier().fit(x_arac,y_arac)

#Gecikme
#trafik(1-10), hava(1-3), kurte geçmiş yükü(paket sayısı)
x_risk = np.array([
    [2, 1, 5], [8, 2, 15], [1, 1, 2], [9, 3, 20], 
    [5, 1, 10], [7, 2, 18], [10, 3, 5], [3, 1, 25]
])
#0: zamanında teslimat, 1: gecikme riski(müşteri uyarılmalı)
y_risk = np.array([0, 1, 0, 1, 0, 1, 1, 1])
risk_model = LogisticRegression().fit(x_risk,y_risk)

def logistic_app():
    print("="* 75)
    print("Fio Yönetim Merkezi")
    print("="* 75)

    agirlik = float(input("Paketin ağırlığı(kg): "))
    mesafe = float(input("Hedef mesafe (km): "))
    trafik = int(input("Rotadaki trafik yoğunluğu (1-10):"))
    hava = int(input("Hava durumu (1: açık, 2: yağmurlu, 3: karlı): "))
    kurye_yuku = int(input("Atanacak kuryenin günceldeki mevcut paket sayısı"))

    print("\n[Sistem] Veriler işleniyor, rota optimize ediliyor")
    time.sleep(1)
    print("[Sistem] AI modelleri çalıştırılıyor... \n")
    time.sleep(1.5)

    eta_tahmini = eta_model.predict([[mesafe,trafik,hava]])[0]
    eta_tahmini = max(5,eta_tahmini)
    arac_id = arac_model.predict([[agirlik,mesafe,hava]])[0]
    arac_tipleri ={
        0: "Moto-Kurye ",
        1: "Panelvan",
        2: "Ağır Vasıta"
    }

    gecikme_riski = risk_model.predict_proba([[trafik,hava,kurye_yuku]])[0][1]
    risk_durumu = risk_model.predict([[trafik,hava,kurye_yuku]])[0]

    print(">>> AI OPERASYON RAPORU <<<")
    print("-" * 60)

    print(f"Tahmini varış süresi: {eta_tahmini:.0f} dakika")
    print(f"Sistem tarafından atanan araç: {arac_tipleri[arac_id]}")
    print(f"Gecikme/Operasyonel Risk Oranı: % {gecikme_riski:.1f}")

    print("-"* 60)

    if risk_durumu == 1 or eta_tahmini >60:
        print("Sistem uyarısı: Hizmet seviyesi ihlali")
        print("-> Aksiyon: Müşteriye 'Gecikme bekleniyor' SMS'i otomatik göndeirldi ")
        if arac_id == 0 and hava ==3:
            print(" -> Aksiyon:Karlı havada moto kurye güvenliği için araç tipi panelvana çevrildi")
    elif hava == 2 and trafik > 7:
        print("Sistem uyarısı: Yağışlı hava ve yoğun trafik")
        print("Aksiyon: Kurye terminaline 'Dikkatli Sürüş!' uyarısı iletildi")
    else:
        print("Durum normal: Paket standart prosedürler çerçevesinde yola çıktı")
        print("-> Aksiyon: Fiş kesildi, rota kurye cihazına iletildi")

    print("-"*60)

logistic_app()    