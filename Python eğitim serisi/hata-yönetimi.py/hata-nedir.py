
# hata oluşabilecek kodlar try içinde. oluşursa except bloğuna yönlendiriliyor

try:
    x = int(input("X: "))
    y = int(input("y: "))
    print(x + y)
except:
    print("hata oluştu")