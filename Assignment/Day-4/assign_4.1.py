def km_to_m(dist):
    return float(dist) * 1000

def m_to_cm(dist):
    return float(dist) * 100

def cm_to_mm(dist):
    return float(dist) * 10

def ft_to_inch(dist):
    return float(dist) * 12

def inch_to_cm(dist):
    return float(dist) * 2.54

def distance_converter(dist,conv_type,conv_func):
    result = conv_func(dist)
    print(f"{dist} {conv_type.split()[0]} = {result} {conv_type.split()[2]}")
    return result

print(" ")
distance = float(input("Enter value : "))

print(" ")
print("---Conversions---")
print(" ")

distance_converter(distance,"km to m", km_to_m)
distance_converter(distance,"m to cm", m_to_cm)
distance_converter(distance,"cm to mm", cm_to_mm)
distance_converter(distance, "ft to inches" , ft_to_inch)
distance_converter(distance,"inch to cm" , inch_to_cm)
print(" ")