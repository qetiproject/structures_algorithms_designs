# https://leetcode.com/problems/merge-sorted-array/

from typing import List

# Time: O(N + M)
# Space: O(N + M)
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    if m == 0:
        nums1[:] = nums2
        return
    if n == 0:
        return
    
    result = []
    l, r = 0, 0
    
    while l < m and r < n:
        if nums1[l] < nums2[r]:
            result.append(nums1[l])
            l += 1
        elif nums1[l] == nums2[r]:
            result.append(nums1[l])
            result.append(nums2[r])
            l += 1
            r += 1
        else:
            result.append(nums2[r])
            r += 1
    result.extend(nums1[l:m])
    result.extend(nums2[r:n])

    nums1[:] = result

    print(result)


print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
# print(merge([1], 1, [], 0))