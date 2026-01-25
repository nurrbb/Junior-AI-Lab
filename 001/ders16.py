# def otonom_fren():
#     hiz = int(input("Hız(km/s): "))
#     mesafe = int(input("Engel Mesafesi(m): "))
#     emniyet_siniri = hiz * 0.5 #dinamik eşikleme değeri
#     if mesafe < emniyet_siniri:
#         print(f"Acil Durum: Mesafe {mesafe}m, emniyet sınırının {emniyet_siniri}m altında! ")
#     else:
#         print("Sürüş parametreleri güvenli aralıktadır.")

# otonom_fren()

# def kredi_Analizi():
#     gelir = int(input("Aylık gelir: "))
#     skor = int(input("Kredi Notu(1-1000): "))
#     endeks = (gelir * 0.7) + (skor * 0.3) # özellik ağırlıklandırma
#     if endeks > 5000:
#         print(f"Risk Analizi Olumlu: Endeks puanı {endeks}")
#     else:
#         print("Ne yazık ki risk analizi olumsuzdur")

# kredi_Analizi()

#decision tree 

# def teshis_botu():
#     ates  = float(input("Vücut ateşi: "))
#     if ates > 37.5:
#         oksuruk = input("Öksürük var mı? (e/h): ")
#         if oksuruk == "e" : print("Klinik tahmin: Enfeksiyon riski.")
#         else: print("Klinik tahmin: Hipotermi/Güneş Çarpması")
#     else:
#         print("Klinik Tahmin: Fizyolojik değerler normal")

# teshis_botu()

#Regresyon analizi
# veriler arasındaki sebep-sonuç ilişkisini matematikselleştirmek
# def bilet_fiyatlandirma():
#     baz_fiyat = 1000
#     talep_orani = int(input("Anlık doluluk oranı (%): "))
#     guncel_fiyat = baz_fiyat + (talep_orani * 15)
#     print(f"Dinamik Fiyatlandırma Uygulandı: {guncel_fiyat} TL")

# bilet_fiyatlandirma()

# def siber_guvenlik_analizi():
#     hatali = int(input("Son 10 dakikda hatalı giriş sayısı: "))
#     konum = input("Cihazın konumu alışılmışın dışında mı? (e/h): ")
#     vpn = input("VPN ya da proxy tespit edildi mi? (e/h): ")

#     risk = hatali *15
#     if konum == "e" : 
#          risk += 30

#     if vpn == "e" :
#         risk += 20
#     if risk > 60:
#         print(f"YÜKSEK RİSKE SAHİP: {risk}. Hesap geçici olarak donduruldu")
#     else:
#         print(f"Güvenli: Risk {risk}, eşik değerinin altındadır. İyi günler dilerim")
# siber_guvenlik_analizi()

def rota_maliyeti():
    mesafe = int(input("Teslimat mesafesi (km): "))
    trafik = int(input("Trafik yoğunluğu 1-10 arası kaç? "))
    yakit_fiyati = 40.5
    tuketim = 1+ (trafik * 0.1)
    toplam = mesafe * tuketim * (yakit_fiyati /10)
    print(f"Tahmini ulaşım maliyeti:{toplam: .2f} TL ")
rota_maliyeti()