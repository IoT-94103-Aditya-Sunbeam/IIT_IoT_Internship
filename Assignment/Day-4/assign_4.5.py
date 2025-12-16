print(" ")
wt = float(input("Enter weight in tonns : "))

tonns_to_kg = lambda wt : wt * 1000
kg_to_gm = lambda tonns_to_kg : tonns_to_kg * 1000000
gm_to_mg = lambda kg_to_gm : kg_to_gm * 1000000000
mg_to_pounds = lambda gm_to_mg : gm_to_mg * 0.00000220462

def weight_conversion(wt , conv_type , conv_func):
    result = conv_func(wt)
    print(f"{wt} {conv_type.split()[0]} = {result} {conv_type.split()[2]}")
    return result

print(" ")
print("---Conversions---")
print(" ")

weight_conversion(wt,"tonns to kg", tonns_to_kg)
weight_conversion(wt,"kg to gm", kg_to_gm)
weight_conversion(wt, "gm to mg", gm_to_mg)
weight_conversion(wt,"mg to lbs" , mg_to_pounds)
print(" ")
