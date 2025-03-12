a = float(input())
if a <= 100:
    b = 5
elif (a < 1000):
    b = a/5
else:
    b = a/10
if (a % 10 == 5):
    c = b+2
elif (a % 2 == 0):
    c = b+1
else:
    c = b
print(c)
print(a+c)