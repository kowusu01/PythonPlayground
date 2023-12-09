
def findMinIndex(l):
    minIndex = 0
    for i in range(1, len(l)):
        if(l[i] < l[minIndex]):
            minIndex = i
            
    return minIndex        
        

def selectionSort(l):
        
    for i in range(0, len(l)):
        
        print ("i: ", i)
        startIndex = i+1
        newList = l[startIndex:]
        print ("new list: ", newList)
        minIndex = findMinIndex(newList)        
        print (minIndex)
        print(l[i], l[minIndex])
        if l[i] < l[minIndex]:
            temp  = l[i]
            l[i] = l[minIndex]
            l[minIndex] = temp
            print("after swap: ", l)
                
    return l            
        

#print(findMinIndex([10,3,5,6,1]))

print ( selectionSort([50,56,40,6,88]) )


    