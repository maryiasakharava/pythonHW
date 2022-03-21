import operator

text = open("document.txt", "r")
dicti={}
for l in text:
    for w in l.split():
        if w[len(w)-1]=="," or w[len(w)-1]=="?" or w[len(w)-1]==";" or w[len(w)-1]=="!" or w[len(w)-1]=="." or w[len(w)-1]==":":
            w=w[:len(w)-1:]
        if w not in dicti:
            dicti[w]=1
        else:
            dicti[w]+=1

lex_sorted = {val[0] : val[1] for val in sorted(dicti.items(), key = lambda x: (-x[1], x[0]))}

sorted_d=dict(sorted(lex_sorted.items(),key=operator.itemgetter(1),reverse=True))

count=0
for x,y in sorted_d.items():
    if count<5:
        print(x,":",y)
    else:
        break
    count+=1
