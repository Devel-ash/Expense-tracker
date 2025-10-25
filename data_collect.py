import re

def data_collect():
    #amount regex
    amount_pattern = re.compile(r'^-?\d+(\.\d+)?$')
    #date regex
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    #necessasity regex
    nec_pattern = re.compile(r'^(yes|no|y|n)$', re.IGNORECASE)
    
    # Get amount safely
    while True:
        try:
            amount_input = input("Enter amount (negative = expense, positive = salary, not zero): ").strip()
            if not amount_pattern.match(amount_input):
                raise ValueError("Invalid amount format!")
            
            amount = float(amount_input)
            if amount == 0:
                raise ValueError("Amount cannot be zero!")
            
            break  # valid amount, exit loop
        except ValueError as e:
            print(e)
    
    print("This is recorded as a SALARY." if amount > 0 else "This is recorded as an EXPENSE.")
    
    # Get date safely
    while True:
        try:
            date_input = input("Enter date (YYYY-MM-DD): ").strip()
            if not date_pattern.match(date_input):
                raise ValueError("Invalid date format!")
            # Optional: further check for valid month/day
            year, month, day = map(int, date_input.split("-"))
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError("Invalid month/day in date!")
            break
        except ValueError as e:
            print(e)
    
    # Get necessity safely
    while True:
        try:
            nec_input = input("Is this a necessity? (yes/no): ").strip().lower()
            if not nec_pattern.match(nec_input):
                raise ValueError("Invalid input! Type yes or no.")
            nec = True if nec_input in ['yes', 'y'] else False
            break
        except ValueError as e:
            print(e)
    
    return amount, date_input, nec