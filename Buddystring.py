'''In the Buddy Strings problem, you need to check if it is possible to get two strings, different from exactly a swap of two letters. If such a swap exists, the program 
should return True; otherwise, it should return False. The program should also return False if the two strings have different lengths.'''
def buddyStrings(x,y):   #if size of x is not same as size of y, then
    if len(x) != len(y): 
        return False
    if sorted(x) != sorted(y):  #otherwise when x and y has any element that are not common, then
        return False
#If x and y are the same string, the function checks if there are repeated characters in x. If there are repeated characters, we can swap them so that x and y are the same.'''
    if x==y:
        return len(set(x)) < len(x)
    diffs = [(a,b) for a,b in zip(x,y) if a!=b]
    return len(diffs)==2 and diffs[0]==diffs[1][::-1]

a = "ab"
b = "ba"

print(buddyStrings(a, b))