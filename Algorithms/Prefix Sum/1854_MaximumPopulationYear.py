# https://leetcode.com/problems/maximum-population-year/

from typing import List

# Time: O(N * M)
# Space: O(N)
# def maximumPopulation(logs: List[List[int]]) -> int:
#     population = {}  
#     for birth, death in logs:
#         for year in range(birth, death):
#             population[year] = population.get(year, 0) + 1

#     max_population = max(population.values())
#     max_years = [year for year, count in population.items() if count == max_population]
#     return min(max_years)

# Time: O(N)
# Space: O(1)
def maximumPopulation(logs: List[List[int]]) -> int:
    time = [0] * 101
    for birth, death in logs:
        time[birth - 1950] += 1
        time[death - 1959] -= 1
    max_number = 0
    max_year = 0
    current = 0
    for i in range(len(time)):
        current += time[i]
        if current > max_number:
            max_year = i + 1950
            max_number = current

    return max_year