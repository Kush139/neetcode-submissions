from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -heappop(maxHeap)
            y = -heappop(maxHeap)

            if x != y:
                heappush(maxHeap, -(x-y))


        return 0 if not maxHeap else -maxHeap[0] 