import sys
from collections import deque
input = sys.stdin.readline

N= int(input())
# 그래프 생성
graph = [list(map(int, input().split())) for _ in range(N)] 
#graph = [[map(int, input().split())] for _ in range(N)] 이런식일경우 [[<map object at 0x000001E8C670FF10>], [<map object at 0x000001E8C670F970>], [<map object at 0x000001E8C670F8B0>]] 로 출력
visit = [[0]*N for _ in range(N)] 
u = False
# dfs - > 재귀 or stack
# bfs - > queue
#print(graph)
move = [[0,1], [1, 0]] # 우 하 로만 움직임
# print(visit)
# bfs
def bfs(x, y) :
    global u
    queue = deque()
    visit[x][y] = 1
    queue.append([x, y])
    # print("queue: ", queue)
    while queue: # queue가 비어있기 전까지 작동 None이되면 작동 정지
        qx, qy = queue.popleft()
        num = graph[qx][qy]
        if num == -1 :
            u = True
            return u
        for i in range(2) :
            
            dx = qx + move[i][0] * num
            dy = qy + move[i][1] * num

            if (0>dx or dx > N-1 or 0> dy or dy > N-1) :                          
                continue # continue는 아래코드 무시하고 wile문 다시 시작 
            if visit[dx][dy] == 0 :
                visit[dx][dy] = 1
                queue.append([dx, dy])
        
bfs(0, 0)    
if u == True :
    print('HaruHaru')
else :
    print('Hing')
"""
출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸이다. 다른 출발점에서는 출발하지 않는다.
이동 가능한 방향은 오른쪽과 아래 뿐이다. 위쪽과 왼쪽으로는 이동할 수 없다.
-1 에 도착시 종료
한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼이다. 칸에 쓰여 있는 수 초과나 그 미만으로 이동할 수 없다.
"""