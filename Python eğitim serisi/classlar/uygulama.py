

class bankaHesabı:
    def __init__(self, hesapAdi):
        self.hesapAdi = hesapAdi
        self.bakiye = 0

    def paraYatır(self, miktar):
        self.bakiye += miktar
        return self.bakiye 

hesap = bankaHesabı("yusuf")
print(hesap.paraYatır(100))
print(hesap.paraYatır(1900))
