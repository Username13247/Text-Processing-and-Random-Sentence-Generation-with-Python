from collections import Counter
import random

def successor_map():
    counter=Counter()
    dic={}
    reader=open("masal.txt",encoding='utf-8')
    punc=".,?!'*<>|;¨#$%&/{[]}=)(/"
    cleaned=[]
    for line in reader:
        words = line.split()

        for word in words:
            cleaned.append(word.lower().strip(punc))

    for i in range(len(cleaned)-2):
        current=cleaned[i]
        next1=cleaned[i+1]
        next2=cleaned[i+2]
        if (current,next1) not in dic:
            dic[(current,next1)]=[next2]
        else:
            dic[(current,next1)].append(next2)
    return dic

map1=successor_map()
#print(map1)
temp1=[]
temp1=list(map1)


temp2=random.choice(temp1)


"""
w_1=temp2[0]
w_2=temp2[1] """

w_1='bir'
w_2='gün'

for i in range(107):
    try:
        print(w_1,end=' ')
        print(w_2,end=' ')
        w_3=random.choice(map1[(w_1,w_2)])
        w_1=random.choice(map1[(w_2,w_3)])
        w_2=random.choice(map1[(w_3,w_1)])
    except :
        temp2 = random.choice(temp1)
        w_1 = temp2[0]
        w_2 = temp2[1]
