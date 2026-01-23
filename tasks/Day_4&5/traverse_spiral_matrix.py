"""
Write a function about Traverse a matrix in a spiral format. (3 methods)

input:
matrix = [[1,   2,   3,   4,  5,   6], [7,   8,   9,  10,  11,  12],  [13,  14,  15, 16,  17,  18]]

output:
[1,2,3,4,5,6,12,18,17,16,15,14,13,7,8,9,10,11]
"""


#Method_1 index based 
# def spirallyTraverse(mat):
#     m = len(mat)
#     n = len(mat[0])
#     res = []
#     visited = [[False] * n for _ in range(m)]
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     r, c = 0, 0
#     idx = 0
#     for _ in range(m * n):
#         res.append(mat[r][c])
#         print(res)
#         visited[r][c] = True
#         newR, newC = r + dr[idx], c + dc[idx]
#         if 0 <= newR < m and 0 <= newC < n and not visited[newR][newC]:
#             r, c = newR, newC
#         else:
#             idx = (idx + 1) % 4
#             r += dr[idx]
#             c += dc[idx]
#     return res

# mat = [ 
#         [1,   2,   3,   4,  5,   6], 
#         [7,   8,   9,  10,  11,  12],  
#         [13,  14,  15, 16,  17,  18]
#       ]
# print(spirallyTraverse(mat))

"""
        print("n value :",n)
        print("visited:",visited)
        print("row value dr:",dr)
        print("column value dc:",dc)
        print("m and n values:",m,n)
        print("res value:",res)
        print("visited or not ",visited[r][c])
        print("newr, newc",newR,newC)
        print("r,c value :",r,c )
        print("if not what value:",newC,newR)
        print("idx value:",idx)
        print("r row value:",r)
        print("c column value :", c)
        print("final res value:", res)
"""

#Method_2 top left right bottom
# def spirallyTraverse(mat):
#     m, n = len(mat), len(mat[0])
#     res = []
#     top, bottom, left, right = 0, m - 1, 0, n - 1
#     while top <= bottom and left <= right:
#         for i in range(left, right + 1):
#             res.append(mat[top][i])
#         top += 1
#         for i in range(top, bottom + 1):
#             res.append(mat[i][right])
#         right -= 1
#         if top <= bottom:
#             for i in range(right, left - 1, -1):
#                 res.append(mat[bottom][i])
#             bottom -= 1
#         if left <= right:
#             for i in range(bottom, top - 1, -1):
#                 res.append(mat[i][left])
#             left += 1
#     return res
# mat = [ 
#         [1,   2,   3,   4,  5,   6], 
#         [7,   8,   9,  10,  11,  12],  
#         [13,  14,  15, 16,  17,  18]
#       ]
# print(spirallyTraverse(mat))

#Method_3 using dictionaries to iterate the values 
def spiralOrder(matrix):
    nextDirection = {
        'top': 'right',
        'right': 'bottom',
        'bottom': 'left',
        'left': 'top'
    }
    m, n = len(matrix), len(matrix[0])

    res = []
    rtop, rbottom = 0, m-1
    cleft, cright = 0, n-1
    direction = 'top'
    while len(res) != (m*n):
        if direction == 'top':
            for j in range(cleft, cright+1):
                res.append(matrix[rtop][j])
            rtop += 1
        elif direction == 'right':
            for i in range(rtop, rbottom+1):
                res.append(matrix[i][cright])
            cright -= 1
        elif direction == 'bottom':
            for j in reversed(range(cleft, cright+1)):
                res.append(matrix[rbottom][j])
            rbottom -= 1
        elif direction == 'left':
            for i in reversed(range(rtop, rbottom+1)):
                res.append(matrix[i][cleft])
            cleft += 1
        direction = nextDirection[direction]
        # print("first to last iteration",direction)
    return res
matrix = [ 
            [1,   2,   3,   4,  5,   6], 
            [7,   8,   9,  10,  11,  12],  
            [13,  14,  15, 16,  17,  18]
         ]

result = spiralOrder(matrix)
print(result)
