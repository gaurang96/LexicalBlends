import stringdist
import numpy as np
import re
from pyjarowinkler import distance
blends = open("blends.txt", "r")
wordforms = open("wordforms.txt", "r")
candidates = open("candidates.txt", "r")
dict = open("dict.txt", "r")

wordforms = wordforms.readlines()
blends = blends.readlines()
candidates = candidates.readlines()
dict = dict.readlines()

i = 0
j = 0
c = 0
new = []
for i in range(len(dict)):
   for j in range(len(wordforms)):
        if (wordforms[j] != dict[i]):
         new = wordforms[j]


def diff(a, b):
    b = set(b)
    return [item for item in a if item not in b]

c = diff(wordforms, dict)
print(len(dict))
print(len(wordforms))
print(len(c))
print(len(candidates))


i = 0
target = []
s1 = []
s2 = []
for i in range(len(blends)):
    h = blends[i].split()[0]
    target.append(h)

#print(lb)       # target happens to be just the true lexical blends, separated with the to source words

for i in range(len(blends)):
    u = blends[i].split()[1]
    s1.append(u)

for i in range(len(blends)):
    k = blends[i].split()[2]
    s2.append(k)

stringdist
print(target[0])
print(s1[0])
ld = []

for i, j, k in zip(range(len(target)), range(len(s1)), range(len(s2))):
    a = round(distance.get_jaro_distance(target[i], s1[j]),1)
    b = round(distance.get_jaro_distance(target[i], s2[k]),1)
    ld.append(a)
    ld.append(b)

#print(ld)
#print(len(ld))
arr1 = np.reshape(ld, (183,2))
print(arr1)


ld1 =[]
for i, j, k in zip(range(len(target)), range(len(s1)), range(len(s2))):
    a = stringdist.levenshtein(target[i], s1[j])
    b = stringdist.levenshtein(target[i], s2[k])
    ld1.append(a)
    ld1.append(b)

#print(ld)
#print(len(ld))
arr2 = np.reshape(ld1, (183,2))
print(arr2)

o = []
for i in range(len(candidates)):
    str = candidates[i]
    if (str[0] == str[1] == str[2]) | (str[-1] == str[-2] == str[-3]):
        o.append(str);


f1cand = diff(candidates, o)
#print(o)
#print(f1cand)
print(len(candidates))
print(len(o))
print(len(f1cand))
#print(f1cand)

pre = ("ahh", "aha", "aa", "bwah", "bwh", "aja", "bahah", "ayy", "oo", "jaja", "lm", "xox", "xx", "xk", "yaa")



f1cand = [x for x in f1cand if not x.startswith(pre)]
print(len(f1cand))

#print(f1cand)

# WAY TO REMOVE WORDS FOR OVER-EMPHASIZED WORDS
regex = re.compile(r'(.)\1{2,}')
test = filter(regex.search, f1cand)
#print(test)
print(len(test))

f1cand = [x for x in f1cand if x not in test]
print(len(f1cand))



f2cand = []
for i in range(len(f1cand)):
    if len(f1cand[i]) >= 5:
        f2cand.append(f1cand[i])

print(len(f2cand))

reg = re.compile(r'([a|e|i|o|u]){4,}')
t = filter(reg.search, f2cand)
#print(t)
print(len(t))

f2cand = [x for x in f2cand if x not in t]
print(len(f2cand))

reg2 = re.compile((r'^[^aeyiuo]+$'))
t2 = filter(reg2.search, f2cand)
print(len(t2))

f2cand = [x for x in f2cand if x not in t2]
print(len(f2cand))


with open('fil_candidates.txt', 'w') as filehandle:
    for listitem in f2cand:
        filehandle.write(listitem)
#s= "\n"
#target = [x + s for x in target]
#print(target)


