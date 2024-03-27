class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        # ans = []
        unique_set = set()
        for i in range(n):
            for j in range( i +1, n):
                k = j+1
                l = n - 1
                while k < l:
                    total_sum = nums[i] + nums[j] +nums[k] + nums[l]
                    if total_sum == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        unique_set.add(tuple(temp))
                        k,l = k+1, l-1
                    elif total_sum < target:
                        k +=1
                    else:
                        l -=1
        return (list(unique_set))