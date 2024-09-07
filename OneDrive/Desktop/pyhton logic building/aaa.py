'''A  = [ 1, 2 ,2 , 3 , 4 ,5, 6, 6 ,7 ,10 ]
a1 = A[0:4]
a2 =A[5:10]
a1 = list(set(a1))
a2 = list(set(a))



        
print(  a1 , a2 )
'''
'''
A = [1, 2, 2, 3, 4, 5, 6, 6, 7, 10]
a1 = []
a2 = []

# Append first 5 elements of A to a1
a1 = A[0:5]
# Remove duplicates from a1 (if that's what you intend)
a1 = list(set(a1))  # set() removes duplicates, and we convert it back to a list

# Append the last 5 elements of A to a2
a2 = A[5:10]

# (Optional) Process a2 in a similar manner if needed
# for example, remove duplicates from a2:
a2 = list(set(a2))

# Print final results
print("a1:", a1)
print("a2:", a2)
'''

A = [1,2,3,4,5,6,6,7,7,8,8,9,9,0,3,6,5,4,6,6,7,6,7,8,7,9]
m = len(A)// 2
a1 = A[:m]
new_a1 = []
for elem in a1:
    if elem not in new_a1:
        new_a1.append(elem)
a2 =A[m:]
new_a2 = []
for elem in a2:
    if elem not in new_a2:
        new_a2.append(elem)
        
print( new_a1 , new_a2 )

import random

# Generate a list 'A' of random integers between 1 and 10, with a length of 20 elements
A = [random.randint(1, 10) for _ in range(20)]

# Calculate the midpoint
m = len(A) // 2

# Initialize two lists for the first and second halves without duplicates
new_a1 = []
new_a2 = []

# Process first half and add unique elements to new_a1
for elem in A[:m]:
    if elem not in new_a1:
        new_a1.append(elem)

# Process second half and add unique elements to new_a2
for elem in A[m:]:
    if elem not in new_a2:
        new_a2.append(elem)

# Output the generated list and the two halves without duplicates
print("Original list A:", A)
print("First half (unique):",sorted(new_a1))
print("Second half (unique):", sorted(new_a2))
