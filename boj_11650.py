N=int(input())
location=[]
for _ in range(N):
    location.append(list(map(int,input().split())))

location=sorted(location,key=lambda x:(x[0],x[1]))

for i in range(N):
    print(location[i][0],location[i][1],sep=' ')