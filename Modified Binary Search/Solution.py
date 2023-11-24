import typing

# Simple binary search
class Solution:
    def search(self, nums:typing.List[int], target:int):
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2            
            elem = nums[mid]
            if elem == target:
                return mid
            elif elem>target:
                r = mid-1
            elif elem<=target:
                l = mid+1
        return -1
    

if __name__ == "__main__":
    s = Solution()
    nums = [4,5,6,7,0,1,2]
    target =2

    print(s.search(nums,target))