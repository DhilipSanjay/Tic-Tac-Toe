from server import check_rows

# Test case 1: All rows are empty
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
assert check_rows() == 0

# Test case 2: First row has a winning combination
matrix = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
assert check_rows() == 1

# Test case 3: Second row has a winning combination
matrix = [[0, 0, 0], [2, 2, 2], [0, 0, 0]]
assert check_rows() == 2

# Test case 4: Third row has a winning combination
matrix = [[0, 0, 0], [0, 0, 0], [3, 3, 3]]
assert check_rows() == 3

# Test case 5: No winning combination in any row
matrix = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]
assert check_rows() == 0
