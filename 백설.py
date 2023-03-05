lst = []
for i in range(9):
    N = int(input())
    lst.append(N)
cha = sum(lst)-100
for i in range(8):
    for j in range(i+1,9):
        if lst[i]+lst[j] == cha:
            a= lst[i]
            b=lst[j]
lst.remove(a)
lst.remove(b)
new_lst = sorted(lst)
for t in new_lst:
    print(t)