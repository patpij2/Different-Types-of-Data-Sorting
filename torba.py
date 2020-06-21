def ilerazy(n,tab):
    torba = []
    tmp_torba = 0
    
    for i in range(len(tab)):
        if i%2 == 0:
            for j in range(tab[i]):
                tmp_torba += 1
                torba.append(tmp_torba)
        else:
            for j in range(tab[i]):
                tmp_torba -= 1
                torba.append(tmp_torba)
                
    print(torba)
