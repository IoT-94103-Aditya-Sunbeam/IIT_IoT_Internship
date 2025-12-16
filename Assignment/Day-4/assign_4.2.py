km_to_m = lambda dist : float(dist * 1000)
m_to_cm = lambda dist : float(dist * 100)
cm_to_mm = lambda dist : float(dist * 10)
ft_to_inch = lambda dist : float(dist * 12)
inch_to_cm = lambda dist : float(dist * 2.54)

def dist_conv(distance,conv_type,conv_func):
    result = conv_func(distance)
    print(f"{distance} {conv_type.split()[0]} = {result} {conv_type.split()[2]}")
    return result

print(" ")
a = float(input("Enter values : "))
print(" ")

print("---Conversion---")
print(" ")

dist_conv(a,"km to m", km_to_m)
dist_conv(a,"m to cm", m_to_cm)
dist_conv(a,"cm to mm", cm_to_mm)
dist_conv(a, "ft to inches" , ft_to_inch)
dist_conv(a,"inch to cm" , inch_to_cm)
print(" ")