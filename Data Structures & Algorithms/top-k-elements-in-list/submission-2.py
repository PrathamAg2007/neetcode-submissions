class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if num not in seen:
                seen[num] = 1
            else:
                seen[num]+=1
        result = []
        while(k>0):
            maxCount = 0
            maxNum = -1
            for num in seen:
                if (seen[num] > maxCount) and (num not in result):
                    maxCount = seen[num]
                    maxNum = num
            result.append(maxNum)
            k-=1
        return result