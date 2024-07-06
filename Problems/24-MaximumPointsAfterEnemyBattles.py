'''
From contest:

You are given an integer array enemyEnergies denoting the energy values of various enemies.

You are also given an integer currentEnergy denoting the amount of energy you have initially.

You start with 0 points, and all the enemies are unmarked initially.

You can perform either of the following operations zero or multiple times to gain points:

Choose an unmarked enemy, i, such that currentEnergy >= enemyEnergies[i]. By choosing this option:
- You gain 1 point.
- Your energy is reduced by the enemy's energy, i.e. currentEnergy = currentEnergy - enemyEnergies[i].
If you have at least 1 point, you can choose an unmarked enemy, i. By choosing this option:
- Your energy increases by the enemy's energy, i.e. currentEnergy = currentEnergy + enemyEnergies[i].
- The enemy i is marked.
Return an integer denoting the maximum points you can get in the end by optimally performing operations.

'''

'''
This solution is based on the greedy approach. We sort the enemyEnergies array and then iterate over the array from the start and end.
'''

from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        points = 0
        i, j = 0, len(enemyEnergies) - 1

        while i <= j:
            if currentEnergy >= enemyEnergies[i]:
                points += (currentEnergy // enemyEnergies[i])
                currentEnergy = (currentEnergy % enemyEnergies[i])
            
            elif points > 0:
                currentEnergy += enemyEnergies[j]
                j -= 1

            else:
                break
        
        return points