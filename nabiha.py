"""
Nabiha's salary project. it's a parctice project to leanr more about loops and lists


used to calculate how much money we saved after rents..
"""
savingList = []

answer = "yes"
while answer != "no":
    monthlySalary = int(input("Enter your monthly salar in $: "))
    monthName = input("Enter the month name: ")
    saving = int(input("Enter your savings percentages: "))
    rent = int(input("Enter your rent percentages: "))
    electricity = int(input("Enter your electricity percentages: ")) 

    total_percentages = saving + rent + electricity

    if total_percentages > 100:
        print("the total percentage can't be more than 100%!! please try again")

    savingPer =  (saving / 100) * monthlySalary
    rentPer = (rent / 100) * monthlySalary
    elecPer = (electricity / 100) * monthlySalary

    total = savingPer + rentPer + elecPer
    remainder =  monthlySalary - total
    yearlyRent = rentPer * 12
    yearlyElec = elecPer * 12
    total_salary = remainder ** 2

    savingList.append(savingPer)

    print(f"you have saved in {monthName}: {savingPer}$, and you spend in rents: {rentPer}$, and your electricity is: {elecPer}$")
    print()
    print(f"your total amount: {total}$")
    print()
    print(f"your remainder after expenses: {remainder}$ ")
    print()
    print(f"your yearly rents : {yearlyRent}$ ")
    print()
    print(f"your yearly Electricity : {yearlyElec}$ ")
    print()
    print(f"your remainder salary power 2: {total_salary}$ ")
    print()
    answer = input("do you want to continue?(if you want to stop input NO): ").lower()

sum = 0
for i in savingList:
    sum = sum + i
print(f"your additional savings for {monthName} is: {sum} ")
