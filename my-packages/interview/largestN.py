class LargestN:
    def __init__(self) -> None:
        pass

    def findMinIndex(self, l):
        
        # assume i is  not null
        minIndex = 0
        myRange = range(1, len(l)) 
        
        for i in myRange:
            if l[i] < l[minIndex]:
                minIndex = i
        
        return minIndex


    def largestN(self, l, n):
        nLarge, lastN = l[:n], l[n:]
        minIndex = self.findMinIndex(nLarge)
        indexes = range(0, len(lastN))
        
        for i in indexes:
            if nLarge[minIndex] < lastN[i]:
                nLarge[minIndex] = lastN[i]
            minIndex = self.findMinIndex(nLarge)
      
        return nLarge



lObj = LargestN()
#print(lObj.findMinIndex([89, 90, 5]))
print (lObj.largestN(l=[89, 90, 5, 78, 9, 67,88,7], n=3) )
