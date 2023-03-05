N = int(input())
lst = []
ans =  -99
if N%5 != 0:
    a= N//5
    for i in range(1,a+1):
        if (N-(i*5))%3 ==0:
            ans = i + (N-(i*5))//3
            lst.append(ans)

    if N%3 != 0:
        b = N // 3
        for i in range(1, b + 1):
            if (N - (i * 3)) % 5 == 0:
                ans = i + (N - (i * 3)) // 5
                lst.append(ans)
    else:
        ans = N//3
        lst.append(ans)
else: #5로 나눈 나머지가 0 일때
    ans = N//5
    lst.append(ans)

if ans == -99:
    ans = -1
    lst.append(ans)
print(min(lst))
