class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        
        left = [0] * len(nums)
        left[0] = 1
        right = [0] * len(nums)
        right[len(nums) - 1] = 1

        for i in range(len(nums)):
            if i > 0:
                left[i] = nums[i - 1] * left[i - 1]
                right[(len(nums)- 1) - i] = right[(len(nums) - 1) - (i - 1)] * nums[len(nums) - 1 - (i - 1)]

        for i in range(len(nums)):
            output[i] = left[i] * right[i]

        return output