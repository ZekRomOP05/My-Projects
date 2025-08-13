print("select operator")
print("1. Add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice = input("enter choice (1/2/3/4):")
num1 = float(input("enter first number:"))
num2 = float(input("enter first number:"))

if choice == '1':
    print(num1 + num2)
elif choice == '2':
    print(num1 - num2)
elif choice == '3':
    print(num1 * num2)
elif choice == '4':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error : can not be divide by zero")
else:
    print("invalid choice") 

while True:
    #(put all calculator code here)
    count = input("do you want to coninue? (yes/no):") 
    if count.lower() != "yes":
        break                          
