def overlaping(list1,list2):
    for i in list1:
        if i in list2:
            return True
    return False

list_a = [1,4,6,7,9,5]
list_b = [14,77,8,10,56]

print(" ")
print("Result : ",overlaping(list_a,list_b))
print(" ")