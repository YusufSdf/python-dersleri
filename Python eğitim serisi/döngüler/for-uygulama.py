# numbers = [1,2,3,4,5]


# kap =  0
# for i in numbers:
#     # bölme = i % 3
#     # if bölme == 0:
#     #     print(i)
#     kap += i
# print(kap)


products = ["samsung s24", "samsung s23", "samsung a55", "iphone 15", "iphone 14"]

# for i in products:
#     t = i.find("iphone")
#     if t == 0:
#         print(i)
#     else  :
#         pass

adet = 0
for i in products:
    t = i.find("samsung")
    if t == 0:
        adet += 1
    else  :
        pass
print(adet)