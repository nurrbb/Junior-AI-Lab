import numpy as np
from sklearn.linear_model import LinearRegression as ln
from sklearn import tree

#karbon ayakizi

#veri aylık ulaşım(km), elektrik(kWh), et tüketimi(kg)
#hedef  yıllık karbon ayak izi (ton co2)

x_carbon =np.array([
    [500,150,5],
    [2000, 400, 20],
    [100,100,2],
    [3000,600,30],
    [900,15,2]
])

y_carbon = np.array([1.2,  4.5, 2.4, 0.6, 7.8])

carbon_model = ln().fit(x_carbon,y_carbon)

#öneri sistemi
#veri : co2 miktarı, en büyük kalem(0:ulaşım, 1: elektrik , 2 :et)
#sonu.: 0: bisiklet kullan 1: güneş paneli 2: vegan ürünleri dene

x_advice = [[1.0,0],[5.0,1],[3.0,2],[0.5,0],[6.0,0]]
y_advice =[0,1,2,0,0]

advice_ai = tree.DecisionTreeClassifier().fit(x_advice,y_advice)

#endüstriyel üretim
#veri üretim miktarı (adet), dış sıcaklık(c), vardiya sayısı
#aylık elektrik faturası(TL)

x_factory = np.array([
    [100,30,3],  [800,25,2], [1200,35,3],
    [500,20,1], [1500,32,3],[900,15,2]
])
y_bill = np.array([50000,35000,65000,15000,85000,38000])

factory_model = ln().fit(x_factory,y_bill)

def smart_energy_manager():
    print("*" * 50)
    print("ECO FACTORY AI: ENERJİ VE KARBON YÖNETİMİ")
    print("*"*50)
    print("Modül 1: Karbon Ayak İzi Hesaplayıcı")
    km= float(input("Aylık kaç km araç kullanıyorsunuz?: "))
    kwh = float(input("Aylık elektrik tüketiminiz(kWh)?: "))
    et = float(input("Aylık et tüketim miktarınız(kg)?: "))

    footprint = carbon_model.predict([[km, kwh,et]])[0]
    print(f"Yıllık karbon ayak iziniz: {footprint:.2f} ton CO2")

    #en büyük kirletmeyi bul
    kalemler =[km,kwh,et]
    buyuk_index = kalemler.index(max(kalemler))
    tavsiye_id= advice_ai.predict([[footprint,buyuk_index]])[0]

    tavsiyeler = {0:"Ulaşımda bisiklet veya toplu taşımayı arttırın",
                  1:"Evde enerji tasarruflu cihazlara geçiş yapın.",
                  2: "Beslenmenizde bitkisel proteinlere daha çok yer açın"}
    
    print(f"AI Önerisi: {tavsiyeler[tavsiye_id]}")

    print("MODÜL 2: POWER-SAVE FABRİKA ALARM SİSTEMİ")
    uretim= float(input("Bu ayki üretim adedi: "))
    sicaklik = float(input("Dış ortam sıcaklığı: "))
    vardiya = int(input("Çalışılan toplam vardiya: "))
    fatura= float(input("Gelen fatura tutarı(TL): "))

    tahmin = factory_model.predict([[uretim,sicaklik,vardiya]])[0]
    sapma = (abs(fatura-tahmin) /tahmin)*100
    print(f"AI tahmin fatura{tahmin:.2f} TL")
    
    if fatura > tahmin and sapma > 15:
        print("ENERJİ KAÇAĞI TESPİT EDİLDİ")
    elif fatura < tahmin and sapma > 15:
        print("Verimlilik beklenenden az enerji harcandı")
    else:
        print("Durum normal, enerji tüketimi üretimle paralel seyrediyor")
smart_energy_manager()
    
