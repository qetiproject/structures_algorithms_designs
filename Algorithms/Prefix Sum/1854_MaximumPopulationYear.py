# https://leetcode.com/problems/maximum-population-year/

from typing import List

# Time: O(N)
# Space: O(N)
def maximumPopulation(logs: List[List[int]]) -> int:
    population = {}  
    for birth, death in logs:
        for year in range(birth, death):
            population[year] = population.get(year, 0) + 1

    max_population = max(population.values())
    max_years = [year for year, count in population.items() if count == max_population]

    return min(max_years)