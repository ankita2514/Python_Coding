def repeatedSubstringPattern(s):
    string = (s + s)[1:-1]
    print(string)
    print(string.find(s))
    return string.find(s) != -1

#print(repeatedSubstringPattern("abcabcabcabc"))
print(repeatedSubstringPattern("abad"))