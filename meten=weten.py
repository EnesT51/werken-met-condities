a =int(input('Vul een gehele getal in: '))
b =int(input('Vul een gehele getal in: '))

print(type(a)) 

if a > b:
    max = a
    min = b
    print("is een groter getal",max)

elif a < b:
    max = b
    min = a
    print("is kleiner getal",min)

else:
    min =b
    max =a
    print("getallen zijn even groot")

print("het miniumum is",min)
print("het maximum is", max)