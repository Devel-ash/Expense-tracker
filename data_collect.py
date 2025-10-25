import re

def data_collect():
     # Regex for a valid number (positive or negative, int or float)
    amount_pattern = re.compile(r'^-?\d+(\.\d+)?$')
     # Regex for date format YYYY-MM-DD
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
     # Regex for yes/no answers
    nec_pattern = re.compile(r'^(yes|no|y|n)$', re.IGNORECASE)
    
    # Get amount without crash
    while True:
        amount_input = input("Enter amount (negative = expense, positive = salary, not zero): ").strip()
        if not amount_pattern.match(amount_input):
            print("Invalid amount format! Try again.")
            continue
        try:
            amount = float(amount_input)
            if amount == 0:
                print("Amount cannot be zero! Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    print("This is recorded as a SALARY." if amount > 0 else "This is recorded as an EXPENSE.")
    
    # Get date without crash
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ").strip()
        if date_pattern.match(date_input):
            break
        else:
            print("Invalid date format! Try again.")
    
    # Get necessity without crash
    while True:
        nec_input = input("Is this a necessity? (yes/no): ").strip().lower()
        if nec_pattern.match(nec_input):
            nec = True if nec_input in ['yes', 'y'] else False
            break
        else:
            print("Invalid input! Type yes or no.")
    

    nec = True if nec_input in ['yes', 'y'] else False
    
    # Return dictionary
    return amount,date_input,nec


if __name__ == "__main__":
    data_collect()
