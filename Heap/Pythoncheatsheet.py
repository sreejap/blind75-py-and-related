import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappop(heap)        # 1
heapq.heappush(heap, -2)   # max-heap trick
