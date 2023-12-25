class Solution(object):
    def sortColors(self, nums):
        zero = -1
        one = -1
        two = -1
        for num in nums:
            if num==0:
                zero += 1
                one += 1
                two += 1
                nums[two]=2
                nums[one]=1
                nums[zero]=0
            elif num==1:
                one += 1
                two += 1
                nums[two]=2
                nums[one]=1
            else:
                two += 1
                nums[two]=2
        return nums