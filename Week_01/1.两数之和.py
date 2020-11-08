class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            a = target - nums[i]
            try:
                b = nums.index(a, i+1,len(nums))
                if (a in nums) & (i != b):
                    return [i, b]
            except:
                pass