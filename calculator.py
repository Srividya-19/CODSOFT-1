def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error:Infintity"
    return a/b
print("---CALCULATOR---")
first_num=int(input("Enter First Number:"))
op=input("Enter Operation(+,-,*,/):")
second_num=int(input("Enter Second Number:"))
if op== '+':
    res=add(first_num,second_num)
elif op=='-':
    res=subtract(first_num,second_num)
elif op=='*':
    res=multiply(first_num,second_num)
elif op=='/':
    res=divide(first_num,second_num)
else:
    res="INVALID OPERTAOR"
print("Result:",res)


