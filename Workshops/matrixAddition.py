"""
@author: emretosun

"""
firstMatrix = [[1, 3, 5],
               [2, 4, 1],
               [1, 5, 7]];
secondMatrix = [[3, 3, 4],
                [2, 4, 1],
                [3, 5, 4]];
resultMatrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]];
for x in range(len(firstMatrix)):
    for y in range(len(firstMatrix[0])):
        resultMatrix[x][y] = firstMatrix[x][y] + secondMatrix[x][y];
for value in resultMatrix:
    print(value);
        