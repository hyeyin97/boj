#점화식...분명 쉬웠는데,,
N=int(input())
times=[0]
pays=[0]
for _ in range(N):
    a,b=map(int,input().split())
    times.append(a)
    pays.append(b)

dp=[0]*(N+2)
day=1

for i in range(N,0,-1):
    if times[i]+i>N+1:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(pays[i]+dp[i+times[i]],dp[i+1])

print(dp[1])