# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVSION
# 5. MODULUS

print("select an operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. MODULUS")

operation = input()

if operation == "1":
   numb1 = input("Enter first number: ")
   numb2 = input("Enter second number: ")
   print("The sum is "  + str(int(numb1) + int(numb2)))
elif operation == "2":
   numb1 = int(input("Enter first number: "))
   numb2 = int(input("Enter second number: "))
   print("The difference of "  + str(int(numb1) - int(numb2)))
elif operation == "3":
   numb1 = int(input("Enter first number: "))
   numb2 = int(input("Enter second number: "))
   print("The product of "  + str(int(numb1) * int(numb2)))
elif operation == "4":
   numb1 = int(input("Enter first number: "))
   numb2 = int(input("Enter second number: "))
   print("The result is "  + str(int(numb1) / (numb2)))
elif operation == "5":
   numb1 = int(input("Enter first number: "))
   numb2 = int(input("Enter second number: "))
   print("The result is "  + str(int(numb1) % (numb2)))
else:
    print("invalid entry")