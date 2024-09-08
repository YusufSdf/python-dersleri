name = "yusuf"
surname = "sedef"
age = 19

msj = "my name is {} {}. I'm {} old.".format(name,surname,age)
msj = "my name is {2} {1}. I'm {0} old.".format(name,surname,age)
msj = "my name is {a} {s}. I'm {n} old.".format(n=name,s=surname,a=age)

msj = f"my name is {name} {surname}. I'm {age} years old."


print(msj)