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

    for i in range(len(cleaned)-1):
        current=cleaned[i]
        next1=cleaned[i+1]
        if current not in dic:
            dic[current]=[next1]
        else:
            dic[current].append(next1)
    return dic

map1=successor_map()
w_1="ali"
for i in range(104):
    try:
        print(w_1,end=' ')
        w_2=random.choice(map1[w_1])
        print(w_2,end=' ')
        w_1=random.choice(map1[w_2])
    except :
        print("sonuncuya geldik")
        w_1='ali'
        w_2=('zeynep')
