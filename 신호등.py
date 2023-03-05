n , l = map(int,input().split())
now = 0 #이동한 위치
time = 0
for _ in range(n):
    d, r, g = map(int,input().split())#위치,빨간불,초록불
    time += d-now #현재위치에서 신호등위치를 뺀 만큼의 시간을 더해줌
    now = d #신호등위치만큼 이동
    if time % (r+g) <= r :
        time += r - time % (r+g)
time += l-now
print(time)