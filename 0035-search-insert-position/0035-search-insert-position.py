class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            mid  = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else: # nums[mid ] > target:
                r = mid-1
        if nums[mid]< target:
            mid += 1
        return mid
        


