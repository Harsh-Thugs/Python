num1=int(input("enter first number"))
num2=int(input("enter first number"))
num3=int(input("enter first number"))
if (num1>num2 and num1>num3): 
 print(num1,"is large") 
if (num2>num1 and num2>num3): 
 print(num2, "is larger") 
if (num3>num2 and num3>num1): 
 print(num3, "is larger")
else:
 print("all the numbers are same")
