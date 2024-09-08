
# fuel = input("yakıt tipi nedir?: ")
# km = int(input("mesafe bilgisini giriniz: "))

# gasolina = 39.35
# diesel = 41.71
# lpg = 20.25 

# if (fuel == "benzin"):
#     print(gasolina*km)
# elif (fuel=="dizel"):
#     print(diesel*km)
# elif (fuel=="lpg"):
#     print(lpg*km)
# else:
#     print("tekrar deneyiniz")

yazili = int(input("yazılı notu: "))
yazili2 = int(input("2. yazılı notu: "))
sözlü = int(input("sözlü notu: "))
ort = (yazili + yazili2 + sözlü) / 3
print(ort)

if (0<= ort <= 24):
    print("0")
elif (25<= ort <= 44):
    print("1")
elif (45<= ort <= 54):
    print("0")
elif (55<= ort <= 69):
    print("3")
elif (70<= ort <= 100):
    print("4")
else :
    print("try again")
