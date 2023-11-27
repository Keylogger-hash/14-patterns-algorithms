import typing


class Solution:
    def twoSum(self, nums: typing.List[int], target: int) -> typing.List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            print("Current sum:", current_sum)
            print("Left:", left)
            print("Right:", right)
            if current_sum == target:
                return [left, right]
            elif target > current_sum:
                left += 1
            else:
                right -= 1
        return [-1, -1]


# 9
# [1,2,3,4,5]
class Solution1:
    def twoSum(self, nums: typing.List[int], target: int) -> typing.List[int]:
        d = {}
        for i in range(len(nums)):
            num = target - nums[i]
            val = d.get(num)

            if val is not None:
                return [val, i]
            else:
                d[nums[i]] = i
        return [-1, -1]


if __name__ == "__main__":
    s = Solution()
    nums = [4, 2, 3, 4, 5]
    target = 9
    print("Solution with pointers")
    print(s.twoSum(nums, target))
    s1 = Solution1()
    nums = [5, 2, 3, 4, 0]
    target = 9
    print("Solution with dict")
    print(s1.twoSum(nums, target))
