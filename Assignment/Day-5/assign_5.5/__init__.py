import arithmetic
import string_ops

print()
print("1.addition")
print("2.multiplication")
print("3.String Reverse")
print("4.count vowels")
choice = int(input("Enter choice : "))

print()

match choice:
    case 1:
        a = float(input("Enter num1 : "))
        b = float(input("Enter num2 : "))
        result = arithmetic.add(a,b)
        print("Addition : ",result)

    case 2:
        a = float(input("Enter num1 : "))
        b = float(input("Enter num2 : "))
        result = arithmetic.multi(a,b)
        print("Multiplication : ",result)

    case 3:
        str = input("Enter String : ")
        result = string_ops.str_reverse(str)
        print("Result : ",result)

    case 4:
        str = input("Enter String : ")
        result = string_ops.vowels(str)
        print("No. of vowels : ",result)
