from turtle import *

def skok(a,b):
    x,y = position()
    setposition(x+a,y+b)

def kasuj(slowo, i):
    #if i == 0:
    write(slowo)
    print(slowo)
    if i != 0 :
        for j in range(len(slowo)):
            k = j* (len(slowo)-1)*20
            skok(-k+k*(len(slowo)+1)/2, -20*len(slowo))
            kasuj(slowo[0:j]+slowo[j+1:], i-1)
            skok(k-k*(len(slowo)+1)/2, 20*len(slowo))

kasuj('abcd',3)
