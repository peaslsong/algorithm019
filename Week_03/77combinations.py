class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        for i in range(n):
            nums.append(i+1)
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        new_res = []
        for i in range(len(res)):
            if len(res[i]) == k:
                new_res.append(res[i])
        return new_res