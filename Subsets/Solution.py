import typing 


class Solution:
	def subsets(self,nums:typing.List[int]):
		subsets = [[]]
		for num in nums:
			for i in range(len(subsets)):
				subsets.append(subsets[i]+[num])
		return subsets


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.subsets(nums))