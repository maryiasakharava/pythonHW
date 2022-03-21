def sort_list(x):
    n=len(x)
    if (n==0):
        print ('Invalid input')
        exit()
    l=0
    while l<n:
        if type(x[l])== str:
            print ('Invalid input, string detected')
            exit()
        l+=1
    i = 0
    while i<n:
        y = 0
        while y<n-i-1:
            if x[y]>x[y+1]:
                z=x[y]
                x[y]=x[y+1]
                x[y+1]=z
            y+=1
        i+=1
    return x

print(sort_list(x=['a',14,6,3,'b']))
