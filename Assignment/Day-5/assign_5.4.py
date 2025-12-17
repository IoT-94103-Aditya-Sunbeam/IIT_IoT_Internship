import datetime

dta = datetime.datetime.now()

print()
print(f"Date : {dta.strftime("%d-%b-%Y")}")
print(f"Time : {dta.strftime("%I:%M:%S %p")}")
print(f"Day : {dta.strftime("%A")}")
print()
