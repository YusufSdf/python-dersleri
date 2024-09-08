# hataları filtreliyebiliriz
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x / y)
except ZeroDivisionError:
    print("y sıfır olamaz")
except:
    print("bilinmeyen hata")
else:
    print("her şey yolunda")