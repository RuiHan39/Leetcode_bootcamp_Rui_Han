import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for num, cnt in freq.items():
            heapq.heappush(heap,(cnt,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _,num in heap]
