
try:
    units = int(input("Enter electricity units: "))

    if units < 0:
        raise ValueError("Negative units are not allowed")

except ValueError as e:
    print("Invalid input:", e)

else:
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 1 + (units - 100) * 2
    else:
        bill = 100 * 1 + 100 * 2 + (units - 200) * 3

    print("Total electricity bill: Rs.", bill)

finally:
    print("Thank you!")
