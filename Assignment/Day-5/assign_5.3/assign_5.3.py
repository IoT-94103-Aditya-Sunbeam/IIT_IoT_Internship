import geometry

print()

print("1.Circle")
print("2.Rectangle")
choice = int(input("Enter choice : "))

match choice:
    case 1:
        rad = float(input("Enter Radius : "))
        result = geometry.area_of_circle(rad)
        print()
        print("Area of Circle : ",result)
        print()

    case 2:
        l = float(input("Enter length : "))
        b = float(input("Enter breadth : "))
        result = geometry.area_of_rectangle(l , b)
        print()
        print("Area of Rectangle : ",result)
        print()