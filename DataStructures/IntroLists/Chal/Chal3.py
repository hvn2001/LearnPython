from typing import List


# HVN
def find_sum(lst, k):
    lst.sort()
    start = 0
    end = len(lst) - 1
    while start < end:
        if lst[start] + lst[end] == k:
            return lst[start], lst[end]
        elif lst[start] + lst[end] > k:
            end -= 1
        else:
            start += 1


print('HVN', find_sum([1, 2, 3, 4], 5))


def find_sum2(lst, k):
    set_num = set()
    for num in lst:
        if k - num in set_num:
            return num, k - num
        else:
            set_num.add(num)


print('HVN', find_sum2([1, 2, 3, 4], 5))


# 1: Brute Force
def findSumSol(lst, value):
    # iterate lst with i
    for i in range(len(lst)):
        # iterate lst with j
        for j in range(len(lst)):
            # if sum of two iterators is value
            # and i is not equal to j
            # then we have our answer
            if lst[i] + lst[j] is value and i is not j:
                return [lst[i], lst[j]]


def binarySearch(a, item, curr):
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if a[mid] == item:
            index = mid
            found = True
        else:
            if item < a[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return index
    else:
        return -1


# 2: Sorting the List
def findSumSol2(lst, value):
    lst.sort()
    for j in range(len(lst)):
        # find the difference in list through binary search
        # return the only if we find an index
        index = binarySearch(lst, value - lst[j], j)
        if index is not -1 and index is not j:
            return [lst[j], value - lst[j]]


print('Sol2', findSumSol2([1, 5, 3], 2))
print('Sol2', findSumSol2([1, 2, 3, 4], 5))


# 3: Moving indices
def findSumSol3(lst, value):
    # sort the list
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to value
    # returns false when the two indices meet
    while (index1 != index2):
        sum = lst[index1] + lst[index2]
        if sum < value:
            index1 += 1
        elif sum > value:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result


print('Sol3', findSumSol3([1, 2, 3, 4], 5))
print('Sol3', findSumSol3([1, 2, 3, 4], 2))


# 4: Using a Dictionary
def findSumSol4(lst, value):
    foundValues = {}
    for ele in lst:
        # Check for value in dictionary
        # If found return
        try:
            foundValues[value - ele]
            return [value - ele, ele]
        except KeyError:
            foundValues[ele] = 0
    return "No numbers add upto that value"


print('Sol4', findSumSol4([1, 3, 2, 4], 6))


# 5 Using the Python set()
def findSumSol5(lst, value):
    foundValues = set()
    for ele in lst:
        if value - ele in foundValues:
            return [value - ele, ele]
        foundValues.add(ele)
    return False


print('Sol5', findSumSol5([1, 2, 3, 4], 6))


# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

    def twoSum2(self, lst: List[int], value: int) -> List[int]:
        dic = {}
        for index in range(len(lst)):
            if value - lst[index] in dic:
                return dic[value - lst[index]] + 1, index + 1
            else:
                dic[lst[index]] = index
