def sor(a,b,c):
    if a >= b:
        
        if a >= c:
            if b >= c:
                return c,b,a
            else:
                return b,c,a
            
        else:
            return c,a,b

    else:
        
        if a >= c:
            if b >= c:
                return a,c,b
            else:
                return a,b,c
            
        else:
            return c,a,b

print(
sor(1,2,3),
sor(3,2,1),
sor(2,3,1),
sor(1,3,2),
sor(3,1,2),
sor(2,1,3)
)
