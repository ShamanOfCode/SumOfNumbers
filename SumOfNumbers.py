
num = int(input("Enter a number: "))
num = int(num)

var = 0

if num < 0:
    print("This is a negative number")
else:
    for i in range(0, num + 1):
        var = var + i
        print("i: %d | var: %d" % (i, var))
    print("sum: %d" % (var))
