# https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List

# Time: O(min(len(nums1), len(nums2)))
# Space: O(min(len(nums1), len(nums2)))
# def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#     return set(nums1) &  set(nums2)

# Time: O(len(nums1) + len(nums2))
# Space: O(len(nums1) + min(len(nums1), len(nums2)))
# def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#     result = [] # O(min(len(nums1), len(nums2)))
#     nums1_dict= {} # O(len(nums1))

#     for i in nums1:
#         if i not in nums1_dict:
#             nums1_dict[i] = 1
#     for j in nums2:
#         if j in nums1_dict:
#             result.append(j)
#             del nums1_dict[j]

#     return result

# Time complexity: O(n+m), where n and m are the lengths of nums1 and nums2 respectively.
# Space complexity: O(min(n,m)), where n and m are the lengths of nums1 and nums2 respectively.
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_set = set(nums1)
    result = set()
    for num in nums2:
        if num in nums1_set:
            result.add(num)
    return list(result)