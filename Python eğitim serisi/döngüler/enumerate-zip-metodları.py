# enumerate sırayla liste elemanlarını indexler


# marka = ["a","b","c","d"]

# l = list(enumerate(marka,1)) # istediğimiz sıradan itibaren indexler

# for i in l:
#     print(i)



# -* zip birleştirme metodu
isim = ["yusuf", "ali", "ilsu"]
no = [12,45,24]

# a = list(zip(isim,no))
a = list(zip(no,isim))

for x,y in a:
    print(x,y)

print(a)