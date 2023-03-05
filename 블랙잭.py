N,M = map(int,input().split())
s = list(map(int,input().split()))
mmax = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            ssum = s[i]+s[j]+s[k]
            if ssum <= M and ssum > mmax:
                mmax = ssum
print(mmax)