# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75

from typing import List

# Time: O(N)
# Space: O(1)
def compress(chars: List[str]):
    if len(chars) == 1:
            return 1

    result = []
    prev = chars[0]
    group_length_count = 1
    for i in range(len(chars)):
        if chars[i] != prev:
            result.append(prev)
            if group_length_count > 1:
                result.extend(list(str(group_length_count)))
                # result.append(str(group_length_count)) - O(N) space-ის დროს
            prev = chars[i]
            group_length_count = 1
        else:
            group_length_count += 1

    result.append(prev)
    if group_length_count > 1:
         result.extend(list(str(group_length_count)))
         # result.append(str(group_length_count)) - O(N) space-ის დროს

    # ესენი საჭირო არ არის, return len(result)
    chars.clear()
    chars.extend(result)
    return len(chars)

print(compress( ["a","a","b","b", "c", "c", "c"]))

 