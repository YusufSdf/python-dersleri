# # eğer parametre yerine bir şey göndermezsek default olarak girer
# def greeting(name="yusuf ",word="selam"):
#     print(name,word)

# greeting("ali","hello")

def topla(a,b):
    return a+b

def cıkar(a,b):
    return a-b

def islem(a,b,fn = topla):
    return fn(a,b)

result = islem(10,20,cıkar)
print(result)


