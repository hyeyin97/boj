x=int(input())
minSet= [-1] * (x + 1)
if x==1:
    minSet[0]=0
    minSet[1]=0
elif x==2:
    minSet[0] = 0
    minSet[1] = 0
    minSet[2]=1
else:
    minSet[0] = 0
    minSet[1] = 0
    minSet[2] = 1
    minSet[3]=1
for i in range(4,x+1):
    if i%3==0 and i%2==0:
        minSet[i]= min(minSet[i // 3], minSet[i // 2], minSet[i - 1]) + 1
    elif i%3==0:
        minSet[i]= min(minSet[i // 3], minSet[i - 1]) + 1
    elif i%2==0:
        minSet[i]= min(minSet[i // 2], minSet[i - 1]) + 1
    else:
        minSet[i]= minSet[i - 1] + 1
print(minSet[x])