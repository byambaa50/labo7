geo = input()
if geo == "square":
    a = int(input())
    s = (a*a)
    print("%.3f" % s)
elif geo == "rectangle":
    a = int(input())
    b = int(input())
    s = (a*b)
    print("%.3f" % s)
elif geo == "circle":
    r = int(input())
    s = (3.14*r*r)
    print("%.3f" % s)
elif geo == "triangle":
    f = int(input())
    h = int(input())
    s = (0.5*f*h)
    print("%.3f" % s)