
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for n in nums:
            if n in frequencies:
                frequencies[n] = frequencies[n] + 1
            else:
                frequencies[n] = 0
        return heapq.nlargest(k, frequencies, key=frequencies.get)
        