# %%
#Array slicing
'''
* Array slicing allows you to take elements of one array from a given index and store them in another array
Array slicing options:
 *  We pass slice instead of index like this: [start:end].
 * Define start, end  and step e.g: [start:end:step].
 * If we don't pass start its considered 0
 * If we don't pass end its considered length of array in that dimension
 * If we don't pass step its considered 1

'''

#Example

import numpy as np
a = np.array([10, 11, 12, 13, 14, 15, 16])
print(a)  #original array
print(a[1:5]) #slice the elements from index 1to index 4 (exclude index 5)


# %%

#Example

import numpy as np
a = np.array([10, 11, 12, 13, 14, 15, 16])
print(a)  #original array
print(a[1:5]) #slice the elements from index 1to index 4 (exclude index 5)


# %%
#slice elements from start to a given index (not included)
import numpy as np
a = np.array([10, 11, 12, 13, 14, 15, 16])
print(a[:4]) #slice from index 0 to index 3 (index 4 not included

# %%
#slice from specified index to end of array
import numpy as np
a = np.array([10, 11, 12, 13, 14, 15, 16])
print(a[4:])  #slice from index 4 to the end

# %%
#slice from specified start to end indices
import numpy as np
a = np.array([10, 11, 12, 13, 14, 15, 16])
print(a[4:6])  #slice from index 4 to index 5

# %%
#change array element 
import numpy as np
a = np.array([[10, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22]])
b = a[:2, 1:3]
b[0, 0] = 77
print(a[0, 1]) #print 77


# %%
#Negaticve slicing
import numpy as np
a = np.array([10, 11, 12, 13, 14, 15, 16])
print(a[-3:-1]) #Slice from the index 3 from the end to index 1 from the end:



# %%
# Step - slicnginterval 
import numpy as np
a = np.array([10, 11, 12, 13, 14, 15, 16])
print(a[1:5:2]) #return  elements from index 1 to index 4 with a step of 2


# %%
##print the first  index of the first column i.e 12
import numpy as np
a = np.array([[10, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22]])
# [[10 12 13 14]
#  [15 16 17 18]
#  [19 20 21 22]]
print(a[0, 1])


# %%
import numpy as np
a = np.array([[10, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22]])
print(a)

# [[10 12 13 14]
#  [15 16 17 18]
#  [19 20 21 22]]
#slice sub-array from column 1 and 2 (2D array) and return index 1 to 2 i.e 3 not included
b = a[0:2, 1:3]
print(b)
# [[12 13]
#  [16 17]]

# %%
#access array rows and slice it 
import numpy as np
b = np.array([[11, 12, 13, 14, 17, 21, 22], [14, 15, 16, 17, 16, 30, 34], [19, 20, 21, 22, 23, 15, 26], [40, 34, 33, 31, 30, 25, 20]])
print(b)
print('\n')
print(b[0, 2:4]) #access row 1 and slice index 2 to 3 (4 excluded)
print('\n')
print(b[2, 1:6]) #access row 2 and slice index 1 to 5 (6 excluded)

# %%
#access middle row arrays
import numpy as np
a = np.array([[10, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22]])
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

# %%
#access middle row arrays
import numpy as np
a = np.array([[10, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22]])
print(a)
print('\n')
row_r1 = a[1, : ]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints [15 16 17 18] (4,)
print(row_r2, row_r2.shape)  # Prints [15 16 17 18] (4,)

# %%
# Accessing elements of row row 3 and slice throu index 1 to 5(5 not included)
import numpy as np
b = np.array([[11, 12, 13, 14, 17, 21, 22], [14, 15, 16, 17, 16, 30, 34], [19, 20, 21, 22, 23, 15, 26], [40, 34, 33, 31, 30, 25, 20]])
print(b[2, 1:5])

# %%
# Accessing elements from row 1(row index 0) to last (row 4) and slice elements through index 1 to 5(5 not included)
import numpy as np
b = np.array([[11, 12, 13, 14, 17, 21, 22], [14, 15, 16, 17, 16, 30, 34], [19, 20, 21, 22, 23, 15, 26], [40, 34, 33, 31, 30, 25, 20]])
print(b[0: , 1:5]) #1st ratio before the comma indicates the row indices, second ration indicates the the slicing ratio for the array elements

# %%
# Accessing elements from row 1(row index 0) to row index 2(row 3) and slice elements through index 1 to 5(5 not included)
import numpy as np
b = np.array([[11, 12, 13, 14, 17, 21, 22], [14, 15, 16, 17, 16, 30, 34], [19, 20, 21, 22, 23, 15, 26], [40, 34, 33, 31, 30, 25, 20]])
print(b[0:2 , 1:5]) #1st ratio before the comma indicates the row indices, second ration indicates the the slicing ratio for the array elements

# %%
#lookup for matching inces
import numpy as np
a = np.array([12, 13, 15, 16, 17, 18, 20])
b = np.array([12, 15, 15, 16, 19, 18, 21])
print(np.where(a == b))

# %%
#array stacking - arrays must have same dimensions
import numpy as np
a = np.array([[12, 13, 15], [16, 17, 18]])
b = np.array([[12, 15, 15], [16, 19, 18]])

h_stack = (np.hstack((a, b))) #Horizontal stacking 
v_stack = (np.vstack((a, b))) #vertical stacking
print('Array after Horizontal stacking is: \n', h_stack)
print('Array after vertical stacking is: \n', v_stack)


# %%
#array stacking - arrays must have same dimensions
import numpy as np
a = np.array([[2, 3, 1],
              [4, 2, 6],
              [5, 6, 0]])
              
b = np.array([[5, 8, 1],
              [4, 5, 3],
              [0, 3, 5]])
              

              
h_stack = np.hstack((a, b)) #Horizontal stacking 
v_stack = np.vstack((a, b)) #vertical stacking
print('Array after Horizontal stacking is: \n', h_stack)
print('Array after vertical stacking is: \n', v_stack)

#array multiplication = sum of rows*columns
# product=    ([[22, 34 , 16]
#              [28, 60,  40]
#              [49, 70, 23 ]])
arr_prod = np.matmul(a, b) 
print('The product of array a & b is: \n', arr_prod)
arr_prod1 = a@b
print("Another array product of a & b is: \n", arr_prod1)

#array transpose
'''
arr_prod_transpose = ([[22, 28, 49],
                     [34, 60, 70],
                     [16, 40, 23]])
'''
arr_prod_transpose = np.transpose(arr_prod)
print('The transposed array product is: \n', arr_prod_transpose)
arr_prod_transpose1 = arr_prod.T
print('Another transposed array product is: \n', arr_prod_transpose1)


