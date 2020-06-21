def sorkub(napis):
    a = [i for i in napis]

    for i in range(len(a)):
        for j in range(i,len(a)):
            if ord(a[i]) > ord(a[j]):
                a[i],a[j] = a[j],a[i]
                print(a)

    
sorkub('alamakota')
