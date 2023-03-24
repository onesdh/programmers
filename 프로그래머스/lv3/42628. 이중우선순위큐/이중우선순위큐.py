import heapq

def solution(operations):
    q = []
    for i in operations:
        j, h = i.split()
        h= int(h)
        # max delete
        if j == "D" and h == 1:
            if q:
                q.remove(max(q))
        # min delete
        elif j == "D" and h == -1:
            if q:
                heapq.heappop(q)
        else:
            heapq.heappush(q, h)
    
    # heap이 비어있는 경우
    if not q:
        return [0, 0]
    return max(q), q[0]