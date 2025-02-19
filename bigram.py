

reader=open('masal.txt',encoding='utf-8')#türkçe karakter
punctuation = ".,?!'*<>|;¨#$%&/{[]}=)(/`"
conjunctions = ["and", "or", "but", "because", "although", "while", "if", "unless", "so", "as", "either", "neither", "whether", "since", "until","ve", "ile", "hem", "ama", "fakat", "çünkü", "lakin", "o yüzden", "eğer", "şayet", "gibi", "dolayısıyla",  "hâlbuki", "oysa"]
from collections import Counter
sayac=Counter()
ikilisayac=Counter()
uclusayac=Counter()
for line in reader:
    words=line.split()
    cleaned=[]
    bigram=[]
    trigram=[]
    temp=()
    for word in words:

        if word.lower().strip(punctuation) not in  conjunctions:
            cleaned.append(word.lower().strip(punctuation))

    for i in cleaned:
        sayac[i]+=1
        bigram.append(i)
        trigram.append(i)
        if len(bigram)>=2:
            temp=tuple(bigram) #ikili liste counter a eklenmiyor tupple eklenebiliyor
            ikilisayac[temp]+=1
            bigram.pop(0)
        if len(trigram)>=3:
            temp = tuple(trigram)
            uclusayac[temp]+=1
            trigram.pop(0)

"""print("Teklisayac\t",sayac)
print("**********************************************")
print("İkili sayaç\t",ikilisayac)
print("**********************************************")
print("Üçlü sayaç\t",uclusayac)"""
reader.close()
