class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict:
                k = i
                j = dict[diff]
                return [j,k]
            else:
                dict[nums[i]] = i

        return [0,0]