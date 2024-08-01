class FIFO:
    def __init__(self):
        self.list = []
    def ele(self):
        nele = int(input("enter number of elements you wish to enter: "))
        for _ in range(nele):
            ele = int(input("enter your integers: "))
            self.list.append(ele)
    def elelist(self):
        return self.list
    def flist(self):
        newlist = []
        newlist.extend(self.list)
        if len(newlist) > 2 :
            newlist.pop(0)
        newlist.reverse()
        return newlist

fifo = FIFO()
fifo.ele()
finallist = fifo.flist()
print(finallist)
