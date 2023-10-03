def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if(quantity_ordered==0 or distance_in_kms==0):
        return -1
    if(food_type=="N"):
        if(distance_in_kms<=3):
            bill_amount=quantity_ordered*150
            return bill_amount
        elif(distance_in_kms<=6):
            bill_amount=(quantity_ordered*150)+((distance_in_kms-3)*3)
            return bill_amount
        else:
            bill_amount=(quantity_ordered*150)+(3*3)+((distance_in_kms-6)*6)
            return bill_amount
    elif(food_type=="V"):
        if(distance_in_kms<=3):
            bill_amount=quantity_ordered*120
            return bill_amount
        elif(distance_in_kms<=6):
            bill_amount=(quantity_ordered*120)+((distance_in_kms-3)*3)
            return bill_amount
        else:
            bill_amount=(quantity_ordered*120)+(3*3)+((distance_in_kms-6)*6)
            return bill_amount
    else:
        return -1
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",0,8)
print(bill_amount)
