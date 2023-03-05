# H,W = map(int,input().split())
# arr = [list(input()) for _ in range(H)]
# ans = 0
# print(arr)
# for row in range(H):
#     for col in range(W):
#         if arr[row][col] == 'c':
#             arr[row][col] = 0
#         if arr[row][col] == '.':
#             for i in range(col-1,0,-1):
#                 if arr[row][i] != '0': #구름이 있는 칼럼은 0으로 바뀌어 있음
#                     if i == 0: #내 앞,앞앞,앞앞앞 이런식으로 검사,맨 앞까지 왔는데 구름이 없으면
#                         arr[row][col]= -1
#                 else:
#                     ans = col - i
#                     arr[row][col] = ans
#
# print(arr)


H,W = map(int,input().split())
arr = [list(input()) for _ in range(H)]
for row in range(H):
    ans = -99
    for col in range(W):
        if arr[row][col] == 'c':
            arr[row][col] = 0
            ans =col
        if arr[row][col] == '.':
            if ans != -99:
                arr[row][col] = col-ans
            else:
                arr[row][col] = -1

    print(*arr[row])