def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    col_length = len(a[0])

    res = [[0] * row_length for _ in range(col_length)]
    for r in range(row_length):
        for c in range(col_length):
            res[c][row_length-1-r] = a[r][c]

    return res

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(item) for item in list_of_tuples]
    # return map(list, list_of_tuples)

a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(rotate_a_matrix_by_90_degree(a))