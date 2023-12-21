class Solution(object):
    def longestConsecutive(self, nums):
       nums = set(nums)
       output = 0
       for i in nums:
           if i-1 not in nums:
               start = i
               while start in nums:
                   start += 1
               output = max(output,start-i)
       return output
