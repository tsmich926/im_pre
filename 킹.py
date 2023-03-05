king ,stone, N = input().split()
N1 = int(N)

#R L B T RT LT RB LB
can = {'R':0 ,'L':1, 'B':2, 'T':3 ,'RT':4, 'LT':5, 'RB':6, 'LB':7}
dr=[0,0,1,-1,-1,-1,1,1]
dc=[1,-1,0,0,1,-1,1,-1]

chess = [[-1]*8 for i in range(8)] #체스판 만들기

change = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
king_col = change[king[0]]
king_row = 8-int(king[1])
stone_col= change[stone[0]]
stone_row= 8-int(king[1])


for i in range(N1):
    pc= input()
    newr= king_row+dr[can[pc]]
    newc= king_col+dc[can[pc]]
    if 0<=newr<8 and 0<=newc<8: #범위안이면
        if newr == stone_row and newc == stone_col :
            stone_col=stone_col+dc[can[pc]]
            stone_row=stone_row+dr[can[pc]]
        king_row = newr
        king_col = newc

print(king_row,king_col)
print(stone_row,stone_col)
