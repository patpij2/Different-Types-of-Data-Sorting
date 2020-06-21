class drzewko(object):
    def __init__(self,n):
        self.wartosc = n
        self.rodzic = None
        self.dziecko1 = None
        self.dziecko2 = None


brzoza = drzewko(4)
print(brzoza.wartosc)
brzoza.dziecko1 = drzewko(2)
