# def power(x, y):
#     if (y == 0):
#         return 1
#     elif (int(y % 2) == 0):
#         return (power(x, int(y / 2)) * power(x, int(y / 2)))
#     else:
#         return (x * power(x, int(y / 2)) * power(x, int(y / 2)))
# x = int(input("enter the value of x:"))
# y = 2
# print(power(x, 2))

# def power(x, y):
#     if (y == 0):
#         return 1
#     elif (int(y % 2) == 0):
#         return (power(x, int(y / 2)) * power(x, int(y / 2)))
#     else:
#         return (x * power(x, int(y / 2)) * power(x, int(y / 2)))
# x = int(input("enter the value of x:"))
# y = 3
# print(power(x, 3))

# def power(x, y):
#     if (y == 0):
#         return 1
#     elif (int(y % 2) == 0):
#         return (power(x, int(y / 2)) * power(x, int(y / 2)))
#     else:
#         return (x * power(x, int(y / 2)) * power(x, int(y / 2)))
# x = int(input("enter the value of x:"))
# y = int(input("enter the value of y:"))
# print(power(x, y))

# p=int(input("enter the value of p:"))
# r=int(input("enter the value of r:"))
# t=int(input("enter the value of t:"))
# def Simple_interest(P,R,T):
#     print("The principal is", P)
#     print("The rate of interest is", R)
#     print("The time period is",T)
#     S = (P * R * T)/100
#     print('The Simple Interest is', S)
#     return S
# Simple_interest(p, r, t)
#
# p=int(input("enter the value of p:"))
# r=int(input("enter the value of r:"))
# n=int(input("enter the value of n:"))
# t=int(input("enter the value of t:"))
# def compound_interest(P,R,N,T):
#     print("The principal is", P)
#     print("The rate of interest is", R)
#     print("The number of times interest applied per time period is", N)
#     print("The time period is",T)
#     c = p*((1+(r/(100.0*n)))**(n*t))
#     print('The compound Interest is', c)
#     return c
# compound_interest(p,r,n,t)

# def Profit(costPrice, sellingPrice):
#     profit = (sellingPrice - costPrice)
#     return profit
# def Loss(costPrice, sellingPrice):
#     Loss = (costPrice - sellingPrice)
#     return Loss
# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
# if __name__ == "__main__":
#     costPrice, sellingPrice = a,b
#     if sellingPrice == costPrice:
#         print("No profit nor Loss")
#     elif sellingPrice > costPrice:
#         print(Profit(costPrice,sellingPrice), "Profit")
#     else:
#         print(Loss(costPrice,sellingPrice), "Loss")

# def angles(a, b, c):
#     if ((a + b + c == 180) and a != 0 and b != 0 and c != 0):
#         return True
#     else:
#         return False
# a = int(input("enter the value of a:"))
# b = int(input("enter the value of b:"))
# c = int(input("enter the value of c:"))
# if (angles(a, b, c)):
#     print("Valid")
# else:
#     print("Invalid")

# def perimeter_of_Rectangle(length, width):
#     return 2*(length + width)
# def area_of_Rectangle(length, width):
#     return length*width
# length = float(input('Please Enter the Length of a Triangle: '))
# width = float(input('Please Enter the Width of a Triangle: '))
# perimeter = perimeter_of_Rectangle(length, width)
# print("The Perimeter of a Rectangle is", "=" , perimeter)
# area = area_of_Rectangle(length, width)
# print("The Area of a Rectangle is", "=" , area)
# if (area>perimeter):
#     print("area is greater than perimeter:")
# else:
#     print("perimeter is greater than area:")

# num = int(input("enter the numbers:"))
# total_sum = 0
# for n in range(num):
#     n = float(input("Enter the value of n:"))
#     total_sum += n   #total_sum = total_sum + n
# avg = total_sum / num
# print("Average of ", num, " numbers is :", avg)
#
# def lucas(n):
#     a = 2
#     b = 1
#     if (n == 0):
#         return b
#     for i in range(2, n + 1):
#         c = a + b
#         a = b
#         b = c
#     return b
# n = int(input("enter the value of n:"))
# print(lucas(n))

# def fibonacci(n):
#     a = 0
#     b = 1
#     if (n == 0):
#         return b
#     for i in range(2, n + 1):
#         c = a + b
#         a = b
#         b = c
#     return b
# n = int(input("enter the value of n:"))
# print(fibonacci(n))

# n=int(input("Enter The value of n"))
# if (n % (n/2)+1 == 0)or(n % 2 == 0):
#     print(n, "is not a Prime Number")
# else:
#     print(n,"is a Prime number")

# a = int(input("Enter an input number:"))
# def P(a):
#     if a > 1:
#         for i in range(2, int(a/2) + 1):
#             if (a % (a/2)+1 == 0)or(a % 2 == 0):
#                 print(a, "is not a prime number")
#             else:
#                 print(a, "is a prime number")
# print(P(a))

# ta=5%
# da=ta+basic salary=4%
# hra=ta+da+Basic salary=3%
# cca=ta+da+hra+basic salary=8%
# pf=ta+da+hra+basic salary=10%
# incometax=ta+da+hra+basic salary+cca-pf=7%
# netsalary=basicsalary+ta+da+hra+pf-cca-incometax

# B=int(input("enter the value of B:"))
# ta=0.05*(B)
# print("The value of ta = 0.05*(b):",ta)
# da=0.04*(ta+B)
# print("the value of da = 0.04*(ta+B):",da)
# hra=0.03*(ta+da+B)
# print("the value of hra = 0.03*(ta+da+B):",hra)
# cca=0.08*(ta+da+hra+B)
# print("the value of cca = 0.08*(ta+da+hra+B):",cca)
# pf=0.1*(ta+da+hra+B)
# print("the value of pf = 0.1*(ta+da+hra+B):",pf)
# IT=0.07*(ta+da+hra+B+cca-pf)
# print("the value of IT = 0.07*(ta+da+hra+B+cca-pf):",IT)
# NTS=(B+ta+da+hra+pf-cca-IT)
# print("the value of NTS = (B+ta+da+hra+pf-cca-IT):",NTS)

# B=int(input("enter the value of B:"))
# def fun(B):
#     ta=0.05*(B)
#     print("The value of ta = 0.05*(b):", ta)
#     da = 0.04 * (ta + B)
#     print("the value of da = 0.04*(ta+B):", da)
#     hra = 0.03 * (ta + da + B)
#     print("the value of hra = 0.03*(ta+da+B):", hra)
#     cca = 0.08 * (ta + da + hra + B)
#     print("the value of cca = 0.08*(ta+da+hra+B):", cca)
#     pf = 0.1 * (ta + da + hra + B)
#     print("the value of pf = 0.1*(ta+da+hra+B):", pf)
#     IT = 0.07 * (ta + da + hra + B + cca - pf)
#     print("the value of IT = 0.07*(ta+da+hra+B+cca-pf):", IT)
#     NTS = (B + ta + da + hra + pf - cca - IT)
#     print("the value of NTS = (B+ta+da+hra+pf-cca-IT):", NTS)
# fun(B)

# B=int(input("total value of the product = :"))
# print("for food")
# sgst=0.045*(B)
# print("sgst = 0.045*(B) :",sgst)
# cgst=0.045*(B)
# print("cgst = 0.045*(B) :",cgst)
# print("for goods")
# sgst=0.095*(B)
# print("sgst = 0.095*(B) :",sgst)
# cgst=0.095*(B)
# print("cgst = 0.095*(B) :",cgst)
# print("for heavy duty goods")
# sgst=0.14*(B)
# print("sgst = 0.14(B):",sgst)
# cgst=0.14*(B)
# print("cgst = 0.14(B);",cgst)


# B=int(input("total value of the product = :"))
# def fun(B):
#     print("for food")
#     sgst=0.045*(B)
#     print("sgst = 0.045*(B) :",sgst)
#     cgst=0.045*(B)
#     print("cgst = 0.045*(B) :",cgst)
#     print("for goods")
#     sgst=0.095*(B)
#     print("sgst = 0.095*(B) :",sgst)
#     cgst=0.095*(B)
#     print("cgst = 0.095*(B) :",cgst)
#     print("for heavy duty goods")
#     sgst=0.14*(B)
#     print("sgst = 0.14(B):",sgst)
#     cgst=0.14*(B)
#     print("cgst = 0.14(B);",cgst)
# fun(B)

# a_list=[]
# x = int(input("enter the value of x:"))
# for i in range(0, x):
#     ele = int(input())
#     a_list.append(ele)
# for i in range (x):
#     for j in range(i + 1, x):
#         if (a_list[i] > a_list[j]):
#             t = a_list[i]
#             a_list[i] = a_list[j]
#             a_list[j] = t
# print(a_list)
# print("ascending order = ", a_list)

# a_list = []
# x = int(input("enter the value of x:"))
# for i in range(0, x):
#     ele = int(input())
#     a_list.append(ele)
# for i in range(x):
#     if a_list[i] > a_list[i + 1]:
#         t = a_list[i]
#         a_list[i] = a_list[i + 1]
#         a_list[i + 1] = t
#     print(a_list)
# print("ascending order = ", a_list)
