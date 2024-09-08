# uygulama 1 :  daire alanı hesaplama

radius = int(input("Yarıçap giriniz: "))

area = str(3.14 * radius)
cevre = str(2 * 3.14 * radius)
print("alan "  + area + " çevre "+ cevre)

###
# uygulama 2 : km mil dönüşüm

kl = int(input("kilometre: "))
mil = kl/609344
mil = round(mil, 2) # kaç basamak yazılacak
print(mil)