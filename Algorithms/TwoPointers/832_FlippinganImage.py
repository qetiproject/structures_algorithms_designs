# https://leetcode.com/problems/flipping-an-image/

from typing import List

# Time: O(N ^ 2)
# Space: O(1)
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        # for row in image:
        #     row.reverse()
        #     for i in range(n):
        #         row[i] = 1 - row[i]
        # return image
    
        for row in range(n): # O(N)
            image[row] = image[row][::-1] # O(N/2)
            for col in range(n): # O(N)
                image[row][col] = 1 - image[row][col]
        return image             
