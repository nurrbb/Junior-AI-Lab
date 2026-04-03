# print("--- SİBER-ROBOT BAKICISI ---")
# print("Amacın robotunu 7 gün boyunca hayatta tutmak!")
# print("Dikkat et: Bir özelliği artırırken diğeri düşebilir.\n")

# gun = 1
# enerji = 50
# mutluluk = 50
# saglamlik = 50

# while gun <= 7:
#     print(f"\n=== GÜN: {gun} ===")
#     print(f"Enerji: {enerji} | Mutluluk: {mutluluk} | Sağlamlık: {saglamlik}")
#     print("--------------------------------------------------")
    
#     if enerji <= 0 or mutluluk <= 0 or saglamlik <= 0:
#         print("SİSTEM ÇÖKTÜ! Robotun bozuldu. Oyunu kaybettin.")
#         break
        
#     print("1. Hızlı Şarj Et (+30 Enerji, ama -10 Mutluluk)")
#     print("2. Dijital Oyun Oyna (+30 Mutluluk, ama -20 Enerji)")
#     print("3. Parçaları Yağla ve Tamir Et (+30 Sağlamlık, ama -15 Enerji)")
#     print("4. Uyku Moduna Al (Her şeye +5 ekler ama günü atlar)")
    
#     secim = input("Bugün ne yapmak istersin? (1/2/3/4): ")
    
#     if secim == "1":
#         print("Robot şarj edildi. Biraz sıkıldı...")
#         enerji = enerji + 30
#         mutluluk = mutluluk - 10
#     elif secim == "2":
#         print("Robot çok eğlendi! Ama şarjı azaldı.")
#         mutluluk = mutluluk + 30
#         enerji = enerji - 20
#     elif secim == "3":
#         print("Vidalar sıkıldı, motor yağlandı.")
#         saglamlik = saglamlik + 30
#         enerji = enerji - 15
#     elif secim == "4":
#         print("Robot dinleniyor...")
#         enerji = enerji + 5
#         mutluluk = mutluluk + 5
#         saglamlik = saglamlik + 5
#     else:
#         print("Hatalı tuşlama! Kararsız kaldığın için robot strese girdi (-5 Mutluluk).")
#         mutluluk = mutluluk - 5
#         continue 
        
#     print("\n* Gün bitiyor... Robot yoruluyor ve eskiyor. *")
#     enerji = enerji - 10
#     mutluluk = mutluluk - 5
#     saglamlik = saglamlik - 10
    
#     if enerji > 100:
#         enerji = 100
#     if mutluluk > 100:
#         mutluluk = 100
#     if saglamlik > 100: saglamlik = 100
    
#     gun = gun + 1

# if gun > 7:
#     print("\n*** TEBRİKLER! ***")
#     print("Robotunu 7 gün boyunca başarıyla hayatta tuttun. Harika bir bakıcısın!")

isim = input("Ajan adın: ")

can,altin,guc,bolum = 100,0,10,1

while can > 0 and bolum <4:
    print(f" === {isim} - can: {can} - altın: {altin} - güç: {guc} ===")

    print("HÜCRE: 1- samanı ara, 2- kapıyı tekmele, 3- fare deliği")
    s = input("seçim:")

    if bolum ==1: 
        if s== "1" : 
            guc+= 15; 
            print("Hançer buldun!(güç+)")
        elif s=="2":
            can -= 10
            print("Kapı açıldı ama ayağın sakatlandı can---")
        elif s== "3":
            altin+=10
            print("Kapı açıldı ama ayağın sakatlandı altın+++")
        bolum = 2

    elif bolum ==2:
        print( "koridor 1-sessiz geç, 2-saldır, 3-anahtar çal")
        s= input("Seçim")
        if s =="1": can -= 20; print("Fark edildin! Darbe aldın")
        elif s=="2":
            if guc> 15: print("Hançerle kolayca yendin")
            else: can -= 10; print("Güçsüzsün dayak yedin")
        elif s == "3": can-=10 ; print("Anahtarı aldın ama yaralandın")
        elif s == "4":
            if altin >= 10: altin -= 10; print("Nöbetçi parayı aldı")
            else: can-= 25; print("Paran yok nööbetçi vurdu")
        bolum = 3
    elif bolum == 3:
        mcan = 50
        print("---FİNAL ZİNDAN BÖLÜMÜ---")
        while mcan >0 and can > 0:
            print(f"Müdür: {mcan} - Sen: {can}")
            h = input("1- saldır, 2- savun, 3- kum at: ")
            if h == "1": mcan -= guc; can -= 15; print("Karşılıklı darbe")
            elif h== "2": can -= 5; print("Az hasar aldın.")
            elif h =="3": mcan -= 20; print("Müdür kör oldu")
        if can >0: print("TEBRİKLER ÖZGÜRSÜN");
        bölüm =4

if can <=0: print("Öldünnn zindan mezar olduu")
            

