import typing 


class Solution:
    def findMaxAverage(self, nums: typing.List[int], k:int):
        average = []
        _sum = 0
        start = 0
        for end in range(len(nums)):
            _sum+=nums[end]

            if end >= k - 1:
                average.append(_sum/k)
                _sum -= nums[start]
                start+=1
        return max(average)