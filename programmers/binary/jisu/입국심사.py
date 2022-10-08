from heapq import heappush, heappop


def solution(n, times):
    heap = []
    for time in times:
        heappush(heap, (time, time))
    while n > 0:
        total, time = heappop(heap)
        heappush(heap, (total+time, time))
        n -= 1
    return total

# 힙 이용 : 테케 6~9 시간초과


def solution(n, times):
    min_t = times[0]
    max_t = times[0]*n
    while True:
        count = 0
        mid = (min_t + max_t) // 2
        for time in times:
            count += mid // time
        if count >= n:
            max_t = mid
        elif count < n:
            min_t = mid
        if min_t == max_t - 1:
            break
    return max_t

# 이분탐색하라고 만든 문제인듯...
