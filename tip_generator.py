print("Welcome to the tip calculator")
bill_amount = float(input("What is the total bill: $"))
tip_amount = float(input("How much would yo uwant to tip - 10,15,20?: "))/100
person_amount = float(int(input("How many people in the party?: ")))
total = bill_amount + (bill_amount*tip_amount)
split_total = total/person_amount

print(f"total amount: ${total} || total per person: ${split_total}")

# print(len("12345"))

# print(type("string"))
# print(type(123.45))
# print(type(123))
# print(type(True))

# print("Number of letters: " + str(len(input("Enter your name: "))))

# print(round(3.5,2))

