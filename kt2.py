from pyjarowinkler import distance
import stringdist

blends = open("blends.txt", "r")
blends = blends.readlines()

f2cand = open("fil_candidates.txt", "r")

dict = open("dict.txt", "r")
dict = dict.readlines()

f2cand = f2cand.readlines()
print(len(f2cand))


i = 0
target = []
s1 = []
s2 = []
for i in range(len(blends)):
    h = blends[i].split()[0]
    target.append(h)

print(target)

s = "\n"
dict = [x.rstrip("\n") for x in dict]
print(len(dict))


import random

#train_set = random.sample(target, 20)
# fixing the train set obtained randomly from the command above
train_set = ["gravator", "metroplex", "homeboy", "cheeseburger", "smush", "tweeple", "governator", "snazzy", "muppet", "payola",
             "sexpert", "telethon", "fantabulous", "flunk", "shim", "twitterati", "webisode", "frappuccino", "infomercial", "newbiew"]
print(len(train_set))

train_set = sorted(train_set)
print(train_set)
pre = []
for i in train_set:
    i = i[:3]
    pre.append(i)
print(pre)
suf = []
for i in train_set:
    i = i[-(len(i)-3):]
    suf.append(i)
print(suf)

#cheeseburger
l1 = [x for x in dict if x.startswith(pre[0]) or x.endswith(suf[0])]
print(len(l1))
print(l1)

l1_rev = []
for i in range(len(l1)):
    if (round(distance.get_jaro_distance(train_set[0], l1[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[0], l1[i]) <= 5:
        l1_rev.append(l1[i])
print(len(l1_rev))
print(l1_rev)



#fantabulous
l2 = [x for x in dict if x.startswith(pre[1]) or x.endswith(suf[1])]
print(len(l2))
print(l2)

l2_rev = []
for i in range(len(l2)):
    if (round(distance.get_jaro_distance(train_set[1], l2[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[1], l2[i]) >= 5:
        l2_rev.append(l2[i])
print(len(l2_rev))
print(l2_rev)

#flunk

l3 = [x for x in dict if x.startswith(pre[2]) or x.endswith(suf[2])]
print(len(l3))
print(l3)

l3_rev = []
for i in range(len(l3)):
    if (round(distance.get_jaro_distance(train_set[2], l3[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[2], l3[i]) <= 5:
        l3_rev.append(l3[i])
print(len(l3_rev))
print(l3_rev)


#frappuccino
l4 = [x for x in dict if x.startswith(pre[3]) or x.endswith(suf[3])]
print(len(l4))
print(l4)

l4_rev = []
for i in range(len(l4)):
    if (round(distance.get_jaro_distance(train_set[3], l4[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[3], l4[i]) <= 5:
        l4_rev.append(l4[i])
print(len(l4_rev))
print(l4_rev)

#governator

l5 = [x for x in dict if x.startswith(pre[4]) or x.endswith(suf[4])]
print(len(l5))
print(l5)

l5_rev = []
for i in range(len(l5)):
    if (round(distance.get_jaro_distance(train_set[4], l5[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[4], l5[i]) <= 5:
        l5_rev.append(l5[i])
print(len(l5_rev))
print(l5_rev)

#gravator

l6 = [x for x in dict if x.startswith(pre[5]) or x.endswith(suf[5])]
print(len(l6))
print(l6)

l6_rev = []
for i in range(len(l6)):
    if (round(distance.get_jaro_distance(train_set[5], l6[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[5], l6[i]) <= 5:
        l6_rev.append(l6[i])
print(len(l6_rev))
print(l6_rev)

#homeboy

l7 = [x for x in dict if x.startswith(pre[6]) or x.endswith(suf[6])]
print(len(l7))
print(l7)

l7_rev = []
for i in range(len(l7)):
    if (round(distance.get_jaro_distance(train_set[6], l7[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[6], l7[i]) <= 5:
        l7_rev.append(l7[i])
print(len(l7_rev))
print(l7_rev)

#infomercial

l8 = [x for x in dict if x.startswith(pre[7]) or x.endswith(suf[7])]
print(len(l8))
print(l8)

l8_rev = []
for i in range(len(l8)):
    if (round(distance.get_jaro_distance(train_set[7], l8[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[7], l8[i]) <= 5:
        l8_rev.append(l8[i])
print(len(l8_rev))
print(l8_rev)

#metroplex
l9 = [x for x in dict if x.startswith(pre[8]) or x.endswith(suf[8])]
print(len(l9))
print(l9)

l9_rev = []
for i in range(len(l9)):
    if (round(distance.get_jaro_distance(train_set[8], l9[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[8], l9[i]) <= 5:
        l9_rev.append(l9[i])
print(len(l9_rev))
print(l9_rev)

#muppet

l10 = [x for x in dict if x.startswith(pre[9]) or x.endswith(suf[9])]
print(len(l10))
print(l10)

l10_rev = []
for i in range(len(l10)):
    if (round(distance.get_jaro_distance(train_set[9], l10[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[9], l10[i]) <= 5:
        l10_rev.append(l10[i])
print(len(l10_rev))
print(l10_rev)

#newbie

l11 = [x for x in dict if x.startswith(pre[10]) or x.endswith(suf[10])]
print(len(l11))
print(l11)

l11_rev = []
for i in range(len(l11)):
    if (round(distance.get_jaro_distance(train_set[10], l11[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[10], l11[i]) <= 5:
        l11_rev.append(l11[i])
print(len(l11_rev))
print(l11_rev)

#payola

l12 = [x for x in dict if x.startswith(pre[11]) or x.endswith(suf[11])]
print(len(l12))
print(l12)

l12_rev = []
for i in range(len(l12)):
    if (round(distance.get_jaro_distance(train_set[11], l12[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[11], l12[i]) <= 5:
        l12_rev.append(l12[i])
print(len(l12_rev))
print(l12_rev)


#sexpert

l13 = [x for x in dict if x.startswith(pre[12]) or x.endswith(suf[12])]
print(len(l13))
print(l13)

l13_rev = []
for i in range(len(l13)):
    if (round(distance.get_jaro_distance(train_set[12], l13[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[12], l13[i]) <= 5:
        l13_rev.append(l13[i])
print(len(l13_rev))
print(l13_rev)

#shim

l14 = [x for x in dict if x.startswith(pre[13]) or x.endswith(suf[13])]
print(len(l14))
print(l14)

l14_rev = []
for i in range(len(l14)):
    if (round(distance.get_jaro_distance(train_set[13], l14[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[13], l14[i]) <= 5:
        l14_rev.append(l14[i])
print(len(l14_rev))
print(l14_rev)

#smush

l15 = [x for x in dict if x.startswith(pre[14]) or x.endswith(suf[14])]
print(len(l15))
print(l15)

l15_rev = []
for i in range(len(l15)):
    if (round(distance.get_jaro_distance(train_set[14], l15[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[14], l15[i]) <= 5:
        l15_rev.append(l15[i])
print(len(l15_rev))
print(l15_rev)

#snazzy

l16 = [x for x in dict if x.startswith(pre[15]) or x.endswith(suf[15])]
print(len(l16))
print(l16)

l16_rev = []
for i in range(len(l16)):
    if (round(distance.get_jaro_distance(train_set[15], l16[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[15], l16[i]) <= 5:
        l16_rev.append(l16[i])
print(len(l16_rev))
print(l16_rev)

#telethon

l17 = [x for x in dict if x.startswith(pre[16]) or x.endswith(suf[16])]
print(len(l17))
print(l17)

l17_rev = []
for i in range(len(l17)):
    if (round(distance.get_jaro_distance(train_set[16], l17[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[16], l17[i]) <= 5:
        l17_rev.append(l17[i])
print(len(l17_rev))
print(l17_rev)

#tweeple

l18 = [x for x in dict if x.startswith(pre[17]) or x.endswith(suf[17])]
print(len(l18))
print(l18)

l18_rev = []
for i in range(len(l18)):
    if (round(distance.get_jaro_distance(train_set[17], l18[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[17], l18[i]) <= 5:
        l18_rev.append(l18[i])
print(len(l18_rev))
print(l18_rev)

#twitterati

l19 = [x for x in dict if x.startswith(pre[18]) or x.endswith(suf[18])]
print(len(l19))
print(l19)

l19_rev = []
for i in range(len(l19)):
    if (round(distance.get_jaro_distance(train_set[18], l19[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[18], l19[i]) <= 5:
        l19_rev.append(l19[i])
print(len(l19_rev))
print(l19_rev)

#webisode

l20 = [x for x in dict if x.startswith(pre[19]) or x.endswith(suf[19])]
print(len(l20))
print(l20)

l20_rev = []
for i in range(len(l20)):
    if (round(distance.get_jaro_distance(train_set[19], l20[i]), 1)) >= 0.6 and stringdist.levenshtein(train_set[19], l20[i]) <= 5:
        l20_rev.append(l20[i])
print(len(l20_rev))
print(l20_rev)


pred = 5
true = 20

accuracy = 5*100/20

print("The accuracy is = " + str(accuracy) + "%")