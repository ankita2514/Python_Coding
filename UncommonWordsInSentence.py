def uncommonFromSentences(s1, s2):
    word1 = s1.split()
    word2 = s2.split()
    counts = {}
    uncommon = {}
    for word in word1+word2:
        counts[word] = counts.get(word,0)+1
    uncommon = [word for word in counts if counts[word]==1]
    return uncommon

s1 = "this apple is sweet"
s2 = "this apple is sour"
print(uncommonFromSentences(s1, s2))