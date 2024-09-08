numbers = [1,55,3,94,5,6,7,4,4,4,6,8,4]
names = ["ali","yusuf","asel"]

result = min(numbers)
result = max(names)

print(result)
#ekleme
# numbers.append("77") # sona ekler
# numbers.insert(1,"ilsu")
# print(numbers)

# silme 
numbers.remove(55) # girilen değeri kaldırır !
numbers.pop(2) # girilen indexi kaldırır !

numbers.sort() # küc büy sıralama
numbers.reverse() # büy küc sıralama
result = numbers.count(4) # yazılan değer kaç kere tekrar ediyor


print(result)