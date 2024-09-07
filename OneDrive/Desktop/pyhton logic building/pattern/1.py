print("1")
num = 5
for n in range(num+1):
    for i in range(n):
        print("*" , end="")
    print()
print() 
  
print("2")
rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ") # print number
    # line after each row to display pattern correctly
    print(" ")
print()
    
print("3")
n = 5
for i in range(1 , n +1):
    for j in range (1,i+1 ):
        print(j , end=" ")
    print()
print()

print("5")
n = 5
for i in range(1 ,n + 1):
    print(' ' * (n - i),end='')
    print('*' * (2 * i - 1))
print()

print("5")
n = 5
for i in range(1, n + 1):
    # Printing leading spaces
    print(' ' * (n - i), end='')
    # Printing the first part of the asterisks
    print('*' * (2 * i - 1))
print()

print("6")
n = 5
for  i in range(1 , n + 1):
    print(" " * (n -i) , end='')
    for j in range(1 , i+1):
        print(j , end='')
    for j in range( i -1 , 0 , -1):
        print( j , end="")
    print()
print()

print("7")
n = 5
num = 1
for i in range(1 , n+1):
    for j in range( 1 , i+1):
        print(num , end="")
        num += 1
    print()
print()

print("8")
n = 5
for i in range(1, n + 1):
    # Print leading spaces for alignment
    print(' ' * (n - i ), end='')
    
    # Print the number i, i times in the row
    for j in range(i):
        print(i, end=' ')
    
    # Move to the next line after completing the row
    print()
