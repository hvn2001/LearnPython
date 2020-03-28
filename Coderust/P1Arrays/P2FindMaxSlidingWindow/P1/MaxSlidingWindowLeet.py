from collections import deque
from typing import List


# https://leetcode.com/problems/sliding-window-maximum/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        if len(nums) == 0:
            return result

        window = deque()
        # find out max for first window
        for i in range(0, k):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)

        result.append(nums[window[0]])
        for i in range(k, len(nums)):
            # remove all numbers that are smaller than current number
            # from the tail of list
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            # remove first number if it doesn't fall in the window anymore
            if window and (window[0] <= i - k):
                window.popleft()
            window.append(i)
            result.append(nums[window[0]])
        return result


sol = Solution()
print("Max = " + str(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)))
