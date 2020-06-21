def przenies(a,b,c,n):
    if n==1:
        print('przenies', a,'  ', b)
    else:
        przenies(a,c,b,n-1)
        przenies(a,b,c,1)
        przenies(c,b,a,n-1)
    
def hanoi(n):
    przenies('a','b','c',n)
    
