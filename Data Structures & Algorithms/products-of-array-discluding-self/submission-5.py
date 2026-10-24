class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        
        left = [0] * len(nums)
        left[0] = 1
        
        right = 1

        for i in range(len(nums)):
            if i > 0:
                left[i] = nums[i - 1] * left[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:
                right = right * nums[i + 1]
                
            output[i] = left[i] * right

        return output