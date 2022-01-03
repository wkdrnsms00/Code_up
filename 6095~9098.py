#6095
# box = [[0 for j in range(20)] for i in range(20)] # 19X19 바둑판 생성

# n = int(input())
# for i in range(n):
#     x, y = map(int, input().split())
#     box[x][y] = 1 # 입력, 원하는 위치의 값 1로 변경

# for i in range(1, 20):
#     for j in range(1, 20):
#         print(box[i][j], end=' ')
#     print()  

#6096
# d = [[0 for j in range(19)] for i in range(19)]
# for i in range(19):
#     d[i] = list(map(int, input().split()))

# n = int(input())
# for i in range(n):
#     x, y = map(int,input().split())
#     for j in range(19):
#         if d[j][y-1] == 0:
#             d[j][y-1] = 1
#         else:
#             d[j][y-1] = 0
#         if d[x-1][j] == 0:
#             d[x-1][j] = 1
#         else:
#             d[x-1][j] = 0

# for i in range(0, 19):
#     for j in range(0, 19):
#         print(d[i][j], end=' ')
#     print()

#6097
# h, w = map(int, input().split())
# n = int(input())
# grid = [list(0 for _ in range(w)) for _ in range(h)]

# for i in range(n):
#     l, d, x, y = map(int, input().split()) # d : 가로는 0, 세로는 1
#     x = x-1
#     y = y-1
#     for j in range(l):
#         if d == 0:
#             grid[x][y+j] = 1
#         else:
#             grid[x+j][y] = 1
# for i in range(h):
#     for j in range(w):
#         print(grid[i][j], end=' ')
#     print()
#6098

grid = []
x, y = 1, 1
for i in range(10):
    grid.append(list(map(int, input().split())))

while(1):
    if grid[x][y] == 0: # 현재 위치 점검
        grid[x][y] = 9
    elif grid[x][y] == 2:
        grid[x][y] = 9
        break
    if grid[x][y+1] == 1 and grid[x+1][y] == 1:
        break
    if grid[x][y+1] !=1:
        y = y+1
    elif grid[x+1][y] !=1:
        x = x+1
for i in range(10):
    for j in range(10):
        print(grid[i][j], end=' ')
    print()

