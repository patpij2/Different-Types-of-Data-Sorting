def sorwyb(napis):
    a = [int(i) for i in napis]
    maks = -10000

    for i in range(len(napis)):

        for j in range(i, len(napis)):
            if a[j] > a[i]:
                a[j], a[i] = a[i], a[j]

                print(a)
        

sorwyb('241635')
