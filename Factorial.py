# CODE 1 (Def With Recursion)
def fact(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return num*fact(num-1)
num=int(input("Enter a Number: "))
print("Factorial of {} is {}".format(num,fact(num)))


# CODE 2 (Simple Code)
num=int(input("Enter a Number: "))
mul=1
for i in range(1,num+1):
    mul*=i
print("Factorial of {} is {}".format(num,mul))

# CODE 3 (Only Def)
def fact(num):
    mul=1
    for i in range(1,num+1):
        mul*=i
    return mul
num=int(input("Enter a Number: "))
print("Factorial of {} is {}".format(num,fact(num)))