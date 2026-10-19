class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictNums = {}
        mostFreq = []
        temp = [[] for _ in range(len(nums) + 1)]   # listas independientes

        for num in nums:
            if num in dictNums:
                dictNums[num] = dictNums.get(num) + 1
            else:
                dictNums[num] = 1

        for num, rep in dictNums.items():
            temp[rep].append(num)

        i = len(nums)
        while len(mostFreq) < k:
            for num in temp[i]:          # agrega número por número
                mostFreq.append(num)
                if len(mostFreq) == k:   # corta justo en k
                    break
            i -= 1

        return mostFreq

