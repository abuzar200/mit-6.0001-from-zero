#problem solving mit problem sets:
total_cost=float(input("Enter the total cost of the dream house: "))
annual_salary=float(input("Enter the amount of the annual salary you get: "))
portion_saved=float(input("Enter the amount you wish to save each mounth in decimal: "))
portion_down_payment=total_cost*0.25
current_saving=0
mounth_count=0
mounthly_salary=(annual_salary)/12

while current_saving<portion_down_payment:
    inreturn=current_saving*0.04/12
    current_saving=current_saving+(mounthly_salary*portion_saved)+(inreturn)
    mounth_count+=1
print(mounth_count)
