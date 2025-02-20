

monthlySalary = int(input("Enter your monthly salar in $: "))
monthName = input("Enter the month name: ")
saving = int(input("Enter your savings percentages: "))
rent = int(input("Enter your rent percentages: ")) 
electricity = int(input("Enter your electricity percentages: ")) 

savingPEr =  (saving / 100) * monthlySalary
rentPer = (rent / 100) * monthlySalary
elecPer = (electricity / 100) * monthlySalary

total = savingPEr + rentPer + elecPer
remainder =  monthlySalary - total
yearlyRandE = rentPer + elecPer * 12
total_salary = remainder ** 2

print(f"{total}$, {remainder}$, {yearlyRandE}$, {total_salary}$")