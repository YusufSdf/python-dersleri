my_tuple = 1,2,3,4 # köşeli parantez yoksa tuple = değiştirilemez, ekleme çıkarma yapılmaz
my_liste = ["a",1,2,"b"]


my_list = list(my_tuple) # tuple veri liste dönüştü
my_tuple2 = tuple(my_liste) # liste listeye döndü
print(type(my_tuple2))
print(my_list)
