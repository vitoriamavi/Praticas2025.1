p = 120
for a in range (1, p+1):
    for b in range (a, p +1 - a):
        c = p - (a + b)
        if c > 0:
            a2 = a*a
            b2= b*b
            c2= c*c
            if (a2 +b2) == c2:
                print(a, b, c)