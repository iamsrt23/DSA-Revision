from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        low, mid, high = 0, 0, n - 1
        # low keeps tracks the 0's
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

        # mid traverse the list
            elif nums[mid] == 1:
                mid += 1
        # hight keep tracks the 2's
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
