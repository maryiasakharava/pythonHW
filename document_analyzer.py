import operator

lines = open("document.txt", "r")
d={}
for line in lines:
    for word in line.split():
        if word[len(word)-1]=="." or word[len(word)-1]=="," or word[len(word)-1]==":" or word[len(word)-1]==";" or word[len(word)-1]=="?" or word[len(word)-1]=="!":        
            word=word[:len(word)-1:]
        if word not in d:
            d[word]=1
        else:
            d[word]+=1

lex_sorted = {val[0] : val[1] for val in sorted(d.items(), key = lambda x: (-x[1], x[0]))}

sorted_d=dict(sorted(lex_sorted.items(),key=operator.itemgetter(1),reverse=True))

c=0
for i,j in sorted_d.items():
    if c<5:
        print(i,":",j)
    else:
        break
    c+=1
