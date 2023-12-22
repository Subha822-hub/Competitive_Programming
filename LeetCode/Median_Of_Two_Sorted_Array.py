class Solution(object):
    def findMedianSortedArrays(self, list1, list2):
        merged_array = list1 + list2
        merged_array.sort()
        length = len(merged_array)
        medians = length%2
        median = length/2
        if medians!=0:
            median = int(median)
            calculation = merged_array[median] 
            return calculation
        else:
            median = int(median)
            first = merged_array[median]
            second = merged_array[median-1]
            calculation = (second+first)
            calculation = calculation/2.0
            return calculation