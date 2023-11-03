
import pandas as pd
import numpy as np

def mutateItem(item) -> str:
    return item.upper()

# create dictionary
num_dictionary = {"a":20, "b":30, "c":40, "d":50}

map(num_dictionary, lambda item: item.keys().upper())
map(lambda item: item[0] + str(item[1]), num_dictionary.items())


# create data frame
df = pd.DataFrame(num_dictionary.items(), columns=['letter', 'number'])
print(list(df.index))

# set index to the letter column
df.set_index("letter")

# add new column derived from existing column
df["rating"] = df["number"].apply(lambda x: x * 2)
df

# create empty python dictionary
my_dict = {}
my_dict["a"] = "1"
my_dict["b"] = "2"
my_dict["c"] = "3"
my_dict["d"] = "4"
print (my_dict)

# example of a list comprehension
my_list = [item for item in range(1, 10)]

items = [item[0] + item[1] for item in dict2.items()]
print ("".join(items))


# generator expressions
# - generator expressions are similar to list comprehensions
# - they are enclosed in parentheses instead of brackets
# - they are lazy evaluated

# example of a generator expression
# square of numbers from 1 to 10
nums = [1,2,3,4,5,6,7,8,9,10]
my_generator = ( i*i for i in nums)
print (list(my_generator))
