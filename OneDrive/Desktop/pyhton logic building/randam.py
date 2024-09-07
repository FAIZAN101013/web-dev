n = '4'

# Print '4444' on the first line
for _ in range(4):
    print(n, end="")
print()

# Print '4334' on the second and third lines
for _ in range(4):
    if _ == 1 or _ == 2: #tis the row number 
        print(n, '3', '3', n, sep="", end="")
        print()
    else:
      pass

# Print '4444' on the last line
for _ in range(4):
    print(n, end="")
print()

