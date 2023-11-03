def isUnique(s):
    # create a dictionary 
    # attempt to ad each letter
    # if letter already exists ion dict, return false i.e. duplicate found

    letters = {}
    for c in s:
        if ( c in letters.keys() ):
            return False
        letters[c] = c

    return True

print(isUnique("abcd"))
print(isUnique("1234"))
print(isUnique("efgt"))
print(isUnique("aacd"))
print(isUnique("aaaaa"))

