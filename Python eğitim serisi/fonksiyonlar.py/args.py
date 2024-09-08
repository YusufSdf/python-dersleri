
def toplam(*args):
    print(args)
    result = 0
    for i in args:
        result += i
    return result

print(toplam(1,2,34,5,65))

