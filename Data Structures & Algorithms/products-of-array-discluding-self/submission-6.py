class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        output[0] = 1
        
        right = 1

        for i in range(len(nums)):
            if i > 0:
                output[i] = nums[i - 1] * output[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:
                right = right * nums[i + 1]

            output[i] = output[i] * right

        return output