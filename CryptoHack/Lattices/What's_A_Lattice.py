import numpy as np
def abs(x):
    if x<0:
        return (-1)*x
    return x
v1 = [6, 2, -3]
v2 = [5, 1, 4]
v3 = [2, 7, 1]
matrix = np.array([v1,v2,v3])
print(round(abs(np.linalg.det(matrix))))

# 255

# This script calculates the absolute value of the determinant of a matrix formed by the vectors v1, v2, and v3. It first defines a custom absolute value function. The matrix is created using NumPy from the three vectors. The determinant of this matrix is then computed using `np.linalg.det`, and its absolute value is rounded to the nearest integer. The result is 255.