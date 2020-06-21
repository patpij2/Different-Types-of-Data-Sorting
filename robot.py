def robot(batP,dlD):
    bateria = sum([i for i in range(batP+1)])+1
    droga = dlD
    x = 0
    
    i = -1 #kierunek
    while bateria > 0:
        if x == droga or x == 0:
            i+=1
            bateria-=1
            
        bateria-=1
        
        if bateria < 0 :
            print('STOP')

        if i % 2 == 0:
            x+=1
        else:
            x-=1


        print(x,bateria)


robot(5,10)
