recipe = {
    "a" : {"ismi": "mantı",
    "tarif": "tarifler",
    "resim": "1.jpeg"}
}

recipe2 = {
    "ismi": "mantı",
    "tarif": "tarifler",
    "resim": "1.jpeg"
}

# # access items
# # result = recipe.get("a").get("ismi")
# result = recipe2.keys() # anahtarı döndürür
# result = recipe2.values() # değerleri döndürür
# result = recipe2.items() # tuple yapar

# update items
# result = recipe2.update({"şef":"yusuf"}) # veriyi değiştirir ya da sona ekler

# delete items
result = recipe2.pop("resim")

result = recipe2
print(result)

