class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        for i, num in enumerate(nums):
            if num in uniques:
                return True
            else:
                uniques.add(num)
        return False
            
        