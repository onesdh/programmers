import sys
input = sys.stdin.readline

num = int(input())
# hw = [list(map(int, input().split())) for _ in range(6)]

"""
           2
  |------------------|
3 |                  |   4
  |                  |
  |------------------
          1
"""
h = []
w = []
d = []
for _ in range(6) :
  k, m = map(int, input().split())
  if k == 1 or k == 2 :
    w.append(m)
    d.append(m)
  elif k == 3 or k == 4 :
    h.append(m)
    d.append(m)
max_w = max(w)
max_h = max(h)
min_h = 0
min_w = 0
d = d*2
"""
------------------|
|                 |
|                 |
|------|          |
       |          |
       |---------
"""
for i in range(6) :
  if d[i] == max_h and d[i+1] == max_w:
    min_h = d[i+3]
    min_w = d[i+4]
    break
  elif d[i] == max_w and d[i+1] == max_h:
    min_w = d[i+3]
    min_h = d[i+4]
    break

print(num*((max_h*max_w) - (min_h*min_w)))