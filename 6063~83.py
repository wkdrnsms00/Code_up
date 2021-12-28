#6063
# a, b = map(int, input().split())
# c = (a if (a>=b) else b)
# print(c)
#6064
# a, b, c  = map(int, input().split())
# print(min(a,b,c))
#6065
# def sol(a, b, c):
#     if a%2 ==0:
#         print(a)
#     if b%2 ==0:
#         print(b)
#     if c%2 ==0:
#         print(c)

# a, b, c  = map(int, input().split())
# sol(a, b, c)
#6066
# def sol(a, b, c):
#     if a%2 ==0:
#         print("even")
#     else: print("odd")

#     if b%2 ==0:
#         print("even")
#     else: print("odd")

#     if c%2 ==0:
#         print("even")
#     else: print("odd")
# a, b, c  = map(int, input().split())
# sol(a,b,c)
#6067
# a = int(input())
# if a <0 and (a%2==0):
#     print("A")
# elif a <0 and (a%2!=0):
#     print("B")
# elif a>1 and (a%2==0):
#     print("C")
# else: print("D")
#6068
# a = int(input())
# if a >=90:
#     print("A")
# elif a>=70 and a<90:
#     print("B")
# elif a>=40 and a<70:
#     print("C")
# else: print("D")
# #6069
# a = input()
# if a =="A":
#     print("best!!!")
# elif a == "B":
#     print("good!!")
# elif a == "C":
#     print("run!")
# elif a == "D":
#     print("slowly~")
# else: print("what?")
#6070
# a = int(input())
# if a ==12 or a == 1 or a== 2:
#     print("winter")
# elif a ==3 or a ==4 or a ==5:
#     print("spring")
# elif a == 6 or a==7 or a==8:
#     print("summer")
# elif a ==9 or a ==10 or a==11:
#     print("fall")
#6071
# while(1):
#     a = int(input())
#     if a ==0:
#         break
#     print(a)
#6072
# a = int(input())
# while(a !=0):
#     print(a)
#     a = a-1
#6073
# a = int(input())
# while(a !=0):
#     a=a-1
#     print(a)
#6074
# a = ord(input())
# b = ord('a')
# while(b<=a):
#     print(chr(b), end=' ')
#     b= b+1
#6075
# a = int(input())
# b = 0
# while(b<=a):
#     print(b)
#     b= b+1
#6076
# n = int(input())
# for i in range(n+1) :
#     print(i)
#6077
# n = int(input())
# s = 0
# for i in range(1, n+1) :
#   if i%2==0 :
#     s += i
# print(s)
#6078
# while(1):
#     a = ord(input())
#     print(chr(a))
#     if chr(a) =='q':
#         break
#6079
# a = int(input())
# n = 1
# sum = 0
# while(1):
#     if sum < a:
#         sum = sum +n
#     else: 
#         print(n-1)
#         break
#     n = n+1
#6080
# a, b = map(int, input().split())
# for i in range(1, a+1):
#     for j in range(1, b+1):
#         print(i, j)
#6081
# n  = input()
# n = int(n,16)
# for i in range(1, 16):
#     print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
#6082
# a = int(input())
# for i in range(1,a+1):
#     if i%10 ==3 or i%10 ==6 or i%10 ==9:
#         print('X', end=' ')
#     else: print(i, end=' ')
#6083
r, g, b = map(int, input().split())
m = r*g*b
for i in range(0,r):
    for j in range(0, g):
        for z in range(0, b):
            print(i, j, z)
print(m)