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
                break  

    return result

# O(N)-შიც იწერება


print(nextGreaterElement([4,1,2], [1,3,4,2]))