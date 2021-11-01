# count = 1
# while count <=10:
#     print(count)
#     count +=1
#
# count = 1
# while count <=10:
#     print(count)
#     count +=2
#
# count = 2
# while count <=10:
#     print(count)
#     count +=2
#
# count = 1
# while count <=10:
#     print(count*count)
#     count +=1
#
# count = 1
# while count <=10:
#     print(count*count)
#     count +=1
#
# count = 1
# n=int(input("the value of n="))
# while count <=n:
#     print(count**3+count+count//2)
#     count +=1
#
# n = int(input("enter the value of n :"))
# factorial = 1
# if n < 0:
#     print("Factorial does not exist for negative numbers")
# elif n == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, n + 1):
#         factorial = factorial * i
#     print("The factorial of", n, "is", factorial)

# n=int(input("Enter The value of n"))
# if (n % (n/2)+1 == 0)or(n % 2 == 0):
#     print(n, "is not a Prime Number")
# else:
#     print(n,"is a Prime number")

# n=int(input("Enter the value of n:"))
# r=0
# while(n>0):
#     d=n%10
#     r=r*10+d
#     n=n//10
# print("Reverse of the number:",r)

# n=int(input("Enter number:"))
# t=n
# r=0
# while(n>0):
#     d=n%10
#     r=r*10+d
#     n=n//10
# if(t==r):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")

# num=153
# sum=0
# temp=num
# while temp > 0:
#     digit = temp % 10
#     sum += digit**3
#     temp//=10
# if(num==sum):
#     print(num,"is an armstrong number")
# else:
#     print(num,"is not an armstrong number")

# x= 1
# print(x>>4)

# num=4
# if num<0:
#     print("enter a poitive number.")
# else:
#     sum=0
#     while num>0:
#         sum+=num
#         num+=1
#     print(sum)

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
#
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