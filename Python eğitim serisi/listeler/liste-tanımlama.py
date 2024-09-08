programlama_dilleri = ["python","C#","java"]


#güncelleme
programlama_dilleri[0] = "php"
result = programlama_dilleri + ["go"]
print(result)

# del programlama_dilleri[1] #  elemanı siler
# result = "go" in programlama_dilleri  listenin içinde var mı true false
result2 = "go" in result

print(result2)