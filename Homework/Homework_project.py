# @mapekdemir
print("------Öğrenci-Bilgi-Sistemi--------")
login_data = ["Muhammet Ali", "Pekdemir"]
a = 0
while a < 3:
    a+=1
    isim = input("İsminiz: ")
    soyad = input("Soyadınız: ")
    if a < 3:
        if isim == login_data[0] and soyad == login_data[1]:
            print(f"Hoşgeldin {isim} {soyad}")
            break
        else:
            print("Tekar Deneyin.")
    elif a > 2:
        print("Daha Sonra Tekrar Deneyin.")
        exit()
secim = ""
istek = int(input("Seçmek istediğiniz ders sayısı: "))
if istek < 3:
    print("Sınıfta başarısız oldunuz.")
    exit()
elif istek == 3:
    ders1 = input("Birinci Ders: ")
    ders2 = input("İkinci Ders: ")
    ders3 = input("Üçüncü Ders: ")
    dersler = [ders1, ders2, ders3]
    sec = input(f"1- {ders1}\n2- {ders2}\n3- {ders3}\nBir dersi seçiniz: ")
    if sec == "1":
        secim = ders1
    elif sec == "2":
        secim = ders2
    elif sec == "3":
        secim = ders3
    else:
        print("Geçersiz giriş.")
        exit()
elif istek == 4:
    ders1 = input("Birinci Ders: ")
    ders2 = input("İkinci Ders: ")
    ders3 = input("Üçüncü Ders: ")
    ders4 = input("Dörtünü Ders: ")
    dersler = [ders1, ders2, ders3, ders4]
    sec = input(f"1- {ders1}\n2- {ders2}\n3- {ders3}\n4- {ders4}\nBir dersi seçiniz: ")
    if sec == "1":
        secim = ders1
    elif sec == "2":
        secim = ders2
    elif sec == "3":
        secim = ders3
    elif sec == "4":
        secim = ders4
    else:
        print("Geçersiz giriş.")
        exit()
elif istek == 5:
    ders1 = input("Birinci Ders: ")
    ders2 = input("İkinci Ders: ")
    ders3 = input("Üçüncü Ders: ")
    ders4 = input("Dörtüncü Ders: ")
    ders5 = input("Beşinci Ders: ")
    dersler = [ders1, ders2, ders3, ders4, ders5]
    sec = input(f"1- {ders1}\n2- {ders2}\n3- {ders3}\n4- {ders4}\n5- {ders5}\nBir dersi seçiniz: ")
    if sec == "1":
        secim = ders1
    elif sec == "2":
        secim = ders2
    elif sec == "3":
        secim = ders3
    elif sec == "4":
        secim = ders4
    elif sec == "5":
        secim = ders5
    else:
        print("Geçersiz giriş.")
        exit()
else:
    print("Geçersiz değer.")
    exit()

midterm = int(input(f"{secim} Vize: "))
final = int(input(f"{secim} Final: "))
project = int(input(f"{secim} Project: "))
nates = {"Vize":midterm, "Final":final, "Project":project}

gecme_notu = (midterm/100*30)+(final/100*50)+(project/100*20)
print("---------------Sonuç-------------")
if gecme_notu > 90:
    print(" - AA")
elif gecme_notu > 70 and gecme_notu < 90:
    print(" - BB")
elif gecme_notu > 50 and gecme_notu < 70:
    print(" - CC")
elif gecme_notu > 30 and gecme_notu < 50:
    print(" - DD")
elif gecme_notu < 30:
    print(" - FF")

