# get the size of the matrix from the user
n = int(input("Enter the size of the matrix: "))

# initialize an empty matrix to store the input
matrix = []

# get the matrix elements from the user
for i in range(n):
    row = input(f"Enter the space-separated elements of row {i+1}: ")
    row_list = list(map(int, row.split()))
    if len(row_list) != n:  # check if the row has the correct number of elements
        print("Error: Each row should have exactly n elements")
        exit()
    matrix.append(row_list)

# rotate the matrix by 90 degrees in clockwise direction
rotated_matrix = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        rotated_matrix[j][n-1-i] = matrix[i][j]

# print the rotated matrix
print("Rotated Matrix:")
for row in rotated_matrix:
    print(" ".join(str(element) for element in row))
