nodeNum,edgeNum,start=map(int,input().split())
tree=[]
for _ in range(edgeNum):
    a,b=list(map(int,input().split()))
    tree.append([a,b])
    tree.append([b,a])

#dfs
tree=sorted(tree,key=lambda x:(-x[0],-x[1]))
stack=[start]
visited=[]
while(stack):
    now=stack.pop()
    if now not in visited:
        visited.append(now)
        for each in tree:
            if now == each[0] and each[1] not in visited:
                stack.append(each[1])
for i in visited:
    print(i,end=' ')
print()

#bfs
tree=sorted(tree,key=lambda x:(x[0],x[1]))
queue=[start]
visited=[]
while(queue):
    now = queue.pop(0)
    if now not in visited:
        visited.append(now)
        for each in tree :
            if now == each[0] and each[1] not in visited:
                queue.append(each[1])
for i in visited:
    print(i,end=' ')