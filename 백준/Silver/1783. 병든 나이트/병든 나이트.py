import sys
input = sys.stdin.readline

N, M = map(int,input().split())

"""
1. 위 : 2칸 오른쪽 : 1칸
2. 위 : 1칸 오른쪽 : 2칸
3. 아래: 1칸 오른쪽 : 2칸
4. 아래: 2칸 오른쪽 : 1칸
"""
# 무조건 오른쪽으로 움직임 
# 못움직임
if N == 1 : 
  print(1)
  # 최대가 4
elif N == 2 :
  print(min(4, (M+1)//2))
else : 
  if M <= 6:
    print(min(4, M))
  else :
    print(M-2)
