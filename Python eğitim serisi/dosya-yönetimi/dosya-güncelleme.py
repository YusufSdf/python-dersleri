with open("markalar.txt",encoding="utf-8",mode="r+") as file:
    markalar = file.readlines()
    markalar.insert(2,"3. rent")
    print(markalar)