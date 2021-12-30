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
d= []
for i in range(20):
    d.append([])
    for j in range(0,20):
        d[i].append(map(int,input().split()))
        print(len(d))
# n = int(input())
# for i in range(n):
#     x, y = map(int, input().split())
# for i in range(n):
#     x, y = map(int,input().split())
#     for j in range(1,20):
#         if d[j][y] == 0:
#             d[j][y] = 1
#         else:
#             d[j][y] = 0
#         if d[x][j] ==0:
#             d[x][j] = 1
#         else:
#             d[x][j] = 0
        
# print(d)
