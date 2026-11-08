#problem solving mit problem sets:
total_cost=float(input("Enter the total cost of the dream house: "))
annual_salary=float(input("Enter the amount of the annual salary you get: "))
portion_saved=float(input("Enter the amount you wish to save each mounth in decimal: "))
semi_annual_raise=float(input("Enter the amounth of salary increasing every 6th mounth: "))
portion_down_payment=total_cost*0.25
current_saving=0
mounth_count=0


while current_saving<portion_down_payment:
    mounthly_salary=(annual_salary)/12
    inreturn=current_saving*0.04/12
    current_saving=current_saving+(mounthly_salary*portion_saved)+(inreturn)
    mounth_count+=1
    if mounth_count%6==0:
        annual_salary=annual_salary+(annual_salary*semi_annual_raise)
print(mounth_count)
