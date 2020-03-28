from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search_rec(nums, target, 0, len(nums) - 1)

    def binary_search_rec(self, a, key, low, high):
        if low > high:
            return -1

        mid = low + ((high - low) // 2)
        if a[mid] == key:
            return mid
        elif key < a[mid]:
            return self.binary_search_rec(a, key, low, mid - 1)
        else:
            return self.binary_search_rec(a, key, mid + 1, high)
