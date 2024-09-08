def notGir():
    name = input("isim: ")
    note1 = input("not 1: ")
    note2 = input("not 2: ")

    with open("notUygulama.txt",encoding="utf-8",mode="w") as file:
        file.write(name + " notları " + note1 + " " + note2 + "\n")

def ortalama():
    with open("notUygulama.txt",encoding="utf-8",mode="a") as file:
        file.read()

def kayıt():
    pass


while True:
    menu = input("1- not gir  2-ortalamaları göster 3-kayıt et: ")
    if (menu == "1"):
        notGir()
        
        
            
    elif (menu == "2"):
        ortalama()

    else :
        break
