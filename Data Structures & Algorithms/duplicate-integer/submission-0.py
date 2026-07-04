class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = []
        for i, num in enumerate(nums):
            if num in uniques:
                return True
            else:
                uniques.append(num)
        return False
            
        