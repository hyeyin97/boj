num=int(input())

lst=[0,1,2]

if num==1:
    print(lst[1])
elif num==2:
    print(lst[2])
else:
    for i in range(3,num+1):
        lst.append(lst[i-1]+lst[i-2])

    print(lst[-1]%10007)