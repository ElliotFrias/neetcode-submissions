class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rep = {}
        for i, num in enumerate(nums):
            if num in rep:
                return True
            else :
                rep[num] = i
        return False