from turtle import *

def skok(a,b):
    x,y = position()
    setposition(x+a,y+b)

def graf(slowo):
    i = len(slowo)

    if i >1:
        write(slowo)
        skok(-10*i,-10*i)
        
        graf(slowo[0:i//2])
        skok(10*i,10*i)
        skok(10*i,-10*i)

        graf(slowo[i//2:])

        skok(-10*i,10*i)
        
    elif i == 1:
        write(slowo)

graf('Włodek')
    
