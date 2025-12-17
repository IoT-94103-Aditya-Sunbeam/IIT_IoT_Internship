import calculator

print()

a = float(input("Enter num1 : "))
b = float(input("Enter num2 : "))

print()

result = calculator.add(a,b)
print("Result(add) : ",result)

result = calculator.subtract(a,b)
print("Result(sub) : ",result)

result = calculator.multiply(a,b)
print("Result(multiply) : ",result)

result = calculator.divide(a,b)
print("Result(divide) : ",result)

print()
