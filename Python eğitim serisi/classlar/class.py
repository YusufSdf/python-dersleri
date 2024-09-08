class product:
    def __init__(self,isim,fiyat):
        self.name = isim
        self.price = fiyat

    def get_product(self):
        return print(f"isim {self.name}  fiyat: {self.price} ")



p1 = product("samsung",1500)
p2 = product("hello",9280)

print(product.get_product(p1))
