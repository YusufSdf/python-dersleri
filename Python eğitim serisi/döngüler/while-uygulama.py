# num1 = int(input("1. sayı: "))
# num2 = int(input("2. sayı: "))

# while (num1 <= num2):
#     control = num1 % 2
#     if (control == 0):
#         print(num1)
#     num1 += 1  

# num = 100
# while num >= 0:
#     print(num)
#     num-=1

# liste = []
# i = 1
# while i<6:
#     num1 = liste.append(int(input("1. sayı: ")))
#     i += 1
# liste.sort()
# print(liste)

# username = input("username: ")
# while (bool(username) == False):
#     username = input("username: ")

# print("başarılı")

# uygulama 2 *****

students = []

soru = input("giriş için 'giriş' yazınız ").lower()
print(soru)
while  (soru == "giriş"):
    yes = input("ekleme yapmak için evet yazınız: ").lower()
    if (yes == "evet"):
        print("giriş yapıldı")
        name = input("öğrenci ismi giriniz: ")
        no = input("öğrenci no giriniz: ")
        students.append({
            "name": name,
            "no": no
        })
    else :
        soru = input().lower
print(students)    





    