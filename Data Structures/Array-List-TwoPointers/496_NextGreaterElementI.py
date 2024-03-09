# https://leetcode.com/problems/next-greater-element-i/

from typing import List

# Time: O(N * M)
# Space: O(N)
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    result = [-1] * len(nums1)
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                for k in range(j + 1, len(nums2)): 
                    if nums2[k] > nums1[i]:
                        result[i] = nums2[k] 
                        break  
    return result

# Time: O(len(nums1) + len(nums2))
# Space: O(2N)
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    nextGreaterElement = []
    result = []
    ans_dict = {}
    for i in range(len(nums2)):
        while nextGreaterElement and nums2[nextGreaterElement[-1]] < nums2[i]:
            ans_dict[nums2[nextGreaterElement[-1]]] = nums2[i]
            nextGreaterElement.pop()
        nextGreaterElement.append(i)

    
    for item in nums1:
        if item in ans_dict:
            result.append(ans_dict[item])
        else:
            result.append(-1)
    return result