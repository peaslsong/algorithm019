class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            else:
                nums[k] = nums[i+1]
                k = k+1
        for j in range(k,len(nums)):
            nums.pop()
