import numpy as np
from util import *

# First
list = [1, 2, 3]
my_matrix = np.array(list)
create_first_matrix(my_matrix)

# Second
b = my_new_array()
print(b.shape)

# Third
a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [1, 2, 3, 4]])
a3 = np.array([[1, 2], [5, 6], [1, 2], [1, 2], [1, 2]])
check_random_matrix(a1, a2, a3)

# Fourth
a4 = np.matmul(a3, a1)
check_mul(a4)