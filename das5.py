a = int(input())
b = int(input())
c = int(input())
d = int((a+b+c)/60)
e = (a+b+c) % 60
print(f"{d}:{e:02}")