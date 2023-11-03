# python classes
# class className:
#     1. class variable, shared by all instances
#        but instance can modify their own copy
#        category = "unit_test"

#     2. constructor and instance variable
#        def __init__(self, fName):
#        self.firstName = fName    # instance variable 'firstName'

#    3. inheritance
#      class className(parentClass):

#    4. instance methods
#    - all methods are implicitly supplied the self (current instance) as the first argument   
#    - therefore the methods defnition must have the self argument
#      def methodName(self):

#    5. static methods
#    - static methods are methods that do not require the self argument
#    - they are defined using the @staticmethod decorator
#      @staticmethod
#      def methodName():

#   6. private methods/data
#   - private methods are methods that cannot be accessed outside the class
#   - they are defined using the __methodName() convention
#   - private methods can only be accessed within the class


def hasItem(items: [], item):
    return items.__contains__(item)

def containsApple(items: []):
    return hasItem(items, "apple")

class SC():    
    __items = []
    def add(self, item):
        self.__items.append(item)
        
    def remove(self, item):
        self.__items.remove(item)
        
    def display(self):
        print(self.__items)
        
    def hasApple(self):
        return containsApple(self.__items)
    
sc = SC()
sc.add("apple")
sc.display()

print(sc.hasApple())


num = 987
print( reversed(list(str(num))))
 
for x in range(len(word)-1, -1, -1 ):
    print(word[x])


# reverse a string
word = "hello"
print(word[::-1])



def oddNumbers(nums):
    for n in nums:
        if n % 2 > 0:
            yield n 

oddNumbers = oddNumbers([1,2,3,4,5,6,7,8,9,10])
print(list(oddNumbers))
