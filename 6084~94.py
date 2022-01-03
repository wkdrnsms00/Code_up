#6084
# h, b, c, s = map(int, input().split())
# result = h*b*c*s/8/1024/1024
# print(format(result,".1f" ),"MB")
#6085
# w, h, b = map(int, input().split())
# result = w*h*b/8/1024/1024
# print(format(result, ".2f"),"MB")
#6086
# a = int(input())
# sum = 0
# i = 0
# while(1):
#     sum = sum+i
#     i = i+1
#     if sum>=a:
#         print(sum)
#         break
#6087
# a = int(input())
# i = 0
# for i in range(1, a+1):
#     if i%3 != 0:
#         print(i)
#6088
# a,d,n = map(int, input().split())
# cnt = 1
# next = a
# while(1):
#     if cnt == n:
#         print(next)
#         break
#     next = next+d
#     cnt = cnt+1
#6089
# a,r,n = map(int, input().split())
# cnt = 1
# next = a
# while(1):
#     if cnt == n:
#         print(next)
#         break
#     next = next*r
#     cnt = cnt+1
#6090
# a,m,d,n = map(int, input().split())
# cnt = 1
# next = a
# while(1):
#     if cnt ==n:
#         print(next)
#         break
#     next = next*m+d
#     cnt = cnt+1
#6091
# a,b,c = map(int, input().split())
# day = 1
# while(1):
#     if day%a==0 and day%b==0 and day%c==0:
#         print(day)
#         break
#     day = day+1
#6092
# n = int(input())
# a = input().split()
# d = []
# for i in range(n):
#     a[i] = int(a[i])
# for j in range(0, 24):
#     d.append(0 )
# for i in range(n):
#     d[a[i]] = d[a[i]]+1
# for i in range(1,24):
#     print(d[i],end=' ')
#6093
# n = int(input())
# a = input().split()
# for i in range(n):
#     a[i] = int(a[i])
# for i in range(n-1, -1, -1):
#     print(a[i],end=' ') #내림차순
#6094
# n = int(input())
# a = input().split()
# for i in range(n):
#     a[i] = int(a[i])
# print(min(a)) # 94번까지 완료


