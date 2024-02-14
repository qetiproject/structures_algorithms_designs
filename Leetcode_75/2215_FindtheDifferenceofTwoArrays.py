# https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75

from typing import List
# Time: O(n1 + n2) = O(N)
# Space: O(len(nums1) + len(nums2))
# def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:

#     set1 = set(nums1)
#     set2 = set(nums2)

#     difference1 = list(set1.difference(set2))
#     difference2 = list(set2.difference(set1))

#     result = [difference1, difference2]
#     return result

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:

    set1, set2 = set(nums1), set(nums2)
    res1, res2 = set(), set()

    for n in nums1:
        if n not in set2:
            res1.add(n)
    for n in nums2:
        if n not in set1:
            res2.add(n)

    return [len(res1), len(res2)]
print(findDifference([1,2,3],[2,4,6]))