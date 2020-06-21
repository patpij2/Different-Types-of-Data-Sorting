def babsor(napis):
    a = [int(i) for i in napis]
    good = True
    i = 0
    licznik = 0
    c=0
    
    for x in range(len(a)):
        if a[i+1] > a[i]:
            a[i],a[i+1] = a[i+1],a[i]

        i+=1
        if i == len(a)-1:
            i=0

    return a

        
            
        

    

print(babsor('12535639')  )
