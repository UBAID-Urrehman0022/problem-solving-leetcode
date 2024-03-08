class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            while nums[i] !=nums[nums[i]-1]:
                nums[nums[i]-1], nums[i]  = nums[i], nums[nums[i]-1]
        
        return [i for i in range(1,len(nums)+1) if i!=nums[i-1] ]