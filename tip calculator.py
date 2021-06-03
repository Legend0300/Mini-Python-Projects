def calculate_tip():
    bill = int(input("Enter your bill please: $"))
    tip = bill / 100 * 18
    total_bill = tip + bill
    print(f"18% is the tip, so your total bill is ${total_bill}")
calculate_tip()