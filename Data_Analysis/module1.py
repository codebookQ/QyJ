
import numpy as np

player1 = np.array([7, 9, 10, 9, 11, 13, 10, 10, 11, 10])
player2 = np.array([7, 9, 8, 9, 11, 10, 11, 12, 10, 13])
player3 = np.array([3, 7, 10, 3, 6, 30, 10, 7, 11, 13])

print('球员1的平均得分为', player1.mean())
print('球员2的平均得分为', player2.mean())
print('球员3的平均得分为', player3.mean())