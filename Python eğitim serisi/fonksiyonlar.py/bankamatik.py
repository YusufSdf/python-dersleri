#bankamatik uygulaması

hesapBilgileri = [
    {"name": "yusuf",
    "password": 123,
    "miktar": 1000}
]
ekHesap = {
    "miktar" : 1000000
}
soru1 = input("isim: ")
soru2 = int(input("şifre: "))

while (soru1 == "yusuf" and soru2 == 123):
    menu = input("para çekme/yatırma , bakiye sorgulama /1,2,3 : ")
    if (menu =="1"): # çekme
        miktar = int(input("miktar giriniz: "))
        if (miktar > hesapBilgileri.get("miktar")):
            soru3 = input("ek hesaba geçilsin mi? : 1/0 ")
            if soru3 == "1":
                kalan = ekHesap.get("miktar") - miktar
                ekHesap.update({"miktar":kalan})
                print(kalan)
            else :
                continue 
        else :
            kalan = hesapBilgileri.get("miktar") - miktar
            hesapBilgileri.update({"miktar":kalan})
            print(kalan)
            
    elif (menu == "2") : # yatırma
        yMiktar = int(input("miktar giriniz: "))
        yKalan = hesapBilgileri.get("miktar") + yMiktar
        hesapBilgileri.update({"miktar":yKalan})
        print(yKalan)

    elif (menu == "3" ):
        print(hesapBilgileri.get("miktar"))
        
    else:
        print("hata")
        break

