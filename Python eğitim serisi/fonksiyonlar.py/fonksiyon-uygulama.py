import random
#**1
# def app(aralık,word):
#     for i in range(aralık):
#         print(word)
# a = int(input("aralık: "))
# b = input("kelime: ")

# app(a,b)

# **2

# def dikdörtgen():
#     kenar = int(input("kısa kenar: "))
#     uzunkenar = int(input("uzun kenar: "))
#     question = input("alan/çevre a,b : ")
#     if (question == "a"):
#         print(kenar * uzunkenar)
#     else :
#         print((kenar + uzunkenar)*2)

# dikdörtgen()

#**3

# def para(result):
#     if result==1:
#         return "tura"
#     else :
#         return "yazı"
    
# result = int(random.randint(1,2))
# print(para(result))

#**4
liste = []
def numbers(num1):
    for i in range(1,num1 + 1):
        if ((num1 % i) == 0):
            liste.append(i)
            print(i)

        else:
            pass
numbers(39)
print(liste)