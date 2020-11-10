a = 7
b = 9
c = 2

if a > b:
    print("{} es mayor que {}".format(a, b))
    if a > c:
        print("{} es mayor que {} y {}".format(a, b, c))

elif b > c:
    print("{} es mayor que {} y {}".format(a, b, c))
else:
        print("{} es mayor que todos".format(c))