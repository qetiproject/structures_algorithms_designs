# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List

# Time: O(N * M)
# Space: O(N)
def canPartition(nums: List[int]) -> bool:
     # Calculate the total sum of the input array
    total_sum = sum(nums)
    # If the total sum is odd, we cannot partition the array into two equal sum subsets
    if total_sum % 2 == 1:
        return False
    
    # Calculate the target sum for each subset
    target_sum = total_sum // 2
    
    # Initialize a boolean list of size target_sum+1 to keep track of whether a sum can be formed using the input array
    result = [False] * (total_sum + 1)
    # We can always form a sum of 0 using the input array
    result[0] = True
    
    # Loop through each element in the input array
    for num in nums:
        for j in range(target_sum, num - 1, -1):
            result[j] = result[j] or result[j - num]
    # Return whether or not we can form a sum of target_sum using the input array
    return result[target_sum]

print(canPartition([1,5,11,5]))