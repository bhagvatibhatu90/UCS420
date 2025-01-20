
"""
**1**
"""

for i in range(3):
  print("Bhagvati Bhatu")

"""**2.1**"""

a=10
b=220
c=23
c=a+b
print(a,"+",b,"+",c,"=",a+b+c)

"""**2.2**"""

a="hello"
b="world"
c="ji"
print(a+b+c)

"""**4.1**"""

for i in range(1,11,1):
  print(7,"x",i,"=",7*i,"   ",9,"x",i,"=",9*i)
  print("\n")

"""**4.2**"""

n=int(input("enter any integer of your choice\n"))
for i in range(1,11,1):
   print(n,"x",i,"=",n*i)

"""**4.3**"""

n=int(input("Enter a number\n"))
sum=0
for i in range(1,n+1,1):
  sum=sum+i
print(sum)

"""**5.1 ,5.2,5.3**"""

a=int(input("enter first number\n"))
b=int(input("enter second number\n"))
c=int(input("enter third number\n"))
max_no=max(a,b,c)
print("max= ",max_no)

n=int(input("enter first number\n"))
sum=0;
for i in range(1,n+1,1):
  if(i%7==0 and i%9==0):
    sum=sum+i
print(sum)

n = int(input("Enter a No: "))
sum = 0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n//2) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, n + 1):
    if is_prime(i):
        sum += i

print(sum)

"""6.1,**6.2**"""

n=int(input("enter first number\n"))
sum=0
for i in range(1,n+1,2):
  sum=sum+i
print(sum)

n = int(input("Enter a No: "))
sum = 0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n//2) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, n + 1):
    if is_prime(i):
        sum += i

print(sum)
