products = [
    {'name':'iphone 8', 'price': 4000 },
    {'name':'iphone 8 Plus', 'price': 5000 },
    {'name':'iphone X', 'price': 6000 },
    {'name':'iphone XR', 'price': 7000 },
    {'name':'iphone 11', 'price': 8000 },
    {'name':'samsung s10', 'price': 6000 },
]

# for a in products:
#     print(f"{a.get("name")} marka ürünün fiyatı {a.get("price")} TL dir")

# top =0
# for i in products:
#     top += i.get("price")
# print(top)

# for i in products:
#     price = i.get("price")
#     if (5500 < price < 6500):
#         print(i.get("name"))
#     else :
#         pass

name = input("aranacak ürün: ")
for i in products:
    if (i.get("name").find(name) == 0):
        print(i.get("name"))
    else :
        print("tekrar deneyiniz")

