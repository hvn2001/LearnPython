# https://leetcode.com/problems/merge-sorted-array/
from typing import List


class Solution:
    #  40 ms, faster than 17.69%
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


sol = Solution()


# l1 = [1, 2, 3, 0, 0, 0]
# sol.merge(l1, 3, [2, 5, 6], 3)
# print(l1)

# l1 = [0]
# print(sol.merge(l1, 0, [1], 1))
# print(l1)


# print(sol.merge([1, 0], 1, [2], 1))
# print(sol.merge([1], 1, [], 0))  # [1]

# HVN: 32 ms, faster than 84.04%
def merge_lists2(lst1, m, lst2, n):
    i = 0
    j = 0
    ans = []
    copy_lst1 = lst1[0:m]  # 2 separate obj
    lst2 = lst2[0:n]
    while i <= len(copy_lst1) - 1 and j <= len(lst2) - 1:
        if copy_lst1[i] < lst2[j]:
            ans.append(copy_lst1[i])
            i += 1
        else:
            ans.append(lst2[j])
            j += 1
    ans.extend(copy_lst1[i:])
    ans.extend(lst2[j:])
    lst1[:] = ans[:]


l1 = [1, 2, 3, 0, 0, 0]
merge_lists2(l1, 3, [2, 5, 6], 3)
print(l1)
