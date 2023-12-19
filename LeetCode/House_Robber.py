class Solution:
    def rob(self, nums: List[int]) -> int:
        incl = 0
        excl = 0
        mx = 0
        for i in range (len(nums)):
            mx = max(incl,excl)
            incl = excl + nums[i]
            excl = mx
        return max(incl,excl)