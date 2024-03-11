income = float(input("Enter your income value: "))

def tax_range_detection(my_income):
    if income < 0:
        raise Exception("Income must be positive number")
    elif income > 0 and income < 18200:
        return "Nil"
    elif income > 18201 and income < 37000:
        return "19c for each $1 over $18,200"
    elif income > 37001 and income < 90000:
        return "$3,572 plus 32.5c for each $1 over $37,000"
    elif income > 90001 and income < 180000:
        return "$20,797 plus 37c for each $1 over $90,000"
    elif income > 180001:
        return "$54,097 plus 45c for each $1 over $180,000"



print("You have to pay ", tax_range_detection(income), "for you tax")
