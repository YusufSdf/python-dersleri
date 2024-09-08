# data = {
#     101 : [["yiğit bilgi"],[2010],[50,60,70]],
#     102 : [["ada bilgi"],[2021],[57,60,20]],
#     103 : [["çınar turan"],[2050],[60,10,40]]
# }
# no = int(input("Öğrenci numarasını giriniz: "))
# print(f"{no} numaralı öğrencinin ismi: {data[no][0][0]}, okul not ortalaması {(data[no][2][0] + data[no][2][1] + data[no][2][2]) /3}  ")

data = {
    101: {
        "name": "yiğit bilgi",
        "date": 2010,
        "notes": (50,60,70)
    },
    102: {
        "name": "ada bilgi",
        "date": 2023,
        "notes": (70,64,83)
    }
}
no = int(input("Öğrenci numarasını giriniz: "))
ort = (data[no]["notes"][0] + data[no]["notes"][1] + data[no]["notes"][2]) /3
print(f"{data[no]["name"]} numaralı öğrencinin doğum yılı {data[no]["date"]} ortalaması {ort} ")