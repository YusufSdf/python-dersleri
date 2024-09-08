import database
db = database
def urunGuncelle(sıra,name,price):
    db.products[sıra].update({"ismi":name,"fiyat":price})
    for i in db.products.values():
        print(i)

def urunEkle(sıra,name,price):
    db.products.update({sıra:{"ismi":name,"fiyat":price}})
    for i in db.products.values():
        print(i)


def urunGetir(sıra):
    print(db.products[sıra])
