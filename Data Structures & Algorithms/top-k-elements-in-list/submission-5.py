class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictNums = {}
        mostFreq = []
        cuenta = 0
        for num in nums:
            if num in dictNums:
                dictNums[num] = dictNums.get(num) + 1
            else:
                dictNums[num] = 1

        while cuenta < k:
            maxAct = max(dictNums, key=dictNums.get)
            mostFreq.append(maxAct)
            del dictNums[maxAct]
            cuenta = cuenta + 1

        return mostFreq