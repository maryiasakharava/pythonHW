def sort_list(x):
    n=len(x)
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
