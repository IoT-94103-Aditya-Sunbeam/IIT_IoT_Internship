price = [105,110,108,112,115,116,114]

avg_set = []

for i in range(len(price) - 2):
    a = price[i : i+3]
    avg = sum(a) / 3
    avg_set.append(round(avg,2))

print(" ")
print("3 Day Rolling Average :",avg_set)
print(" ")