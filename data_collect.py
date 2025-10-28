import re

def data_collect():
    #amount regex
    amount_pattern = re.compile(r'^-?\d+(\.\d+)?$')
    #date regex
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    #necessity regex
    nec_pattern = re.compile(r'^(yes|no|y|n)$', re.IGNORECASE)
    #APR input
    rate_pattern = re.compile(r'^\d+(\.\d+)?$')  
    
    #Get Expense or Salary
    while True:
        try:
            amount_input = input("Enter amount (negative = expense, positive = salary, not zero): ").strip()
            if not amount_pattern.match(amount_input):
                raise ValueError("Invalid amount format!")
            
            amount = float(amount_input)
            if amount == 0:
                raise ValueError("Amount cannot be zero!")
            
            break
        except ValueError as e:
            print(e)
    
    print("This is recorded as a SALARY." if amount > 0 else "This is recorded as an EXPENSE.")
    
    #Get Date
    while True:
        try:
            date_input = input("Enter date (YYYY-MM-DD): ").strip()
            if not date_pattern.match(date_input):
                raise ValueError("Invalid date format!")
            
            year, month, day = map(int, date_input.split("-"))
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError("Invalid month/day in date!")
            
            break
        except ValueError as e:
            print(e)
    
    #Get Necessity
    while True:
        try:
            nec_input = input("Is this a necessity? (yes/no): ").strip().lower()
            if not nec_pattern.match(nec_input):
                raise ValueError("Invalid input! Type yes or no.")
            nec = True if nec_input in ['yes', 'y'] else False
            break
        except ValueError as e:
            print(e)
    
    #Bank Section
    bank_name = input("Enter bank name: ").strip()
    
    #Deposit amount
    while True:
        try:
            deposit_input = input("Enter how much you put in the bank: ").strip()
            if not rate_pattern.match(deposit_input):
                raise ValueError("Invalid number format for deposit!")
            deposit = float(deposit_input)
            if deposit <= 0:
                raise ValueError("Deposit must be greater than zero!")
            break
        except ValueError as e:
            print(e)
    
    #Does user get APR?
    while True:
        try:
            apr_input = input("Do you get interest (APR)? (yes/no): ").strip().lower()
            if not nec_pattern.match(apr_input):
                raise ValueError("Invalid input! Type yes or no.")
            gets_apr = apr_input in ['yes', 'y']
            break
        except ValueError as e:
            print(e)
    
    apr_rate = None
    apr_type = None
    apr_days = None
    
    if gets_apr:
        #APR rate
        while True:
            try:
                apr_rate_input = input("Enter the APR rate (%): ").strip()
                if not rate_pattern.match(apr_rate_input):
                    raise ValueError("Invalid APR format! Must be a number.")
                apr_rate = float(apr_rate_input)
                if apr_rate <= 0:
                    raise ValueError("APR must be greater than zero!")
                break
            except ValueError as e:
                print(e)
        
        #APR type (monthly or yearly)
        while True:
            try:
                apr_type_input = input("Is this APR monthly or yearly? (monthly/yearly): ").strip().lower()
                if apr_type_input not in ['monthly', 'yearly']:
                    raise ValueError("Please type 'monthly' or 'yearly'.")
                apr_type = apr_type_input
                break
            except ValueError as e:
                print(e)
        
        #Number of days
        while True:
            try:
                days_input = input("Enter number of days you’ll be getting interest: ").strip()
                if not re.match(r'^\d+$', days_input):
                    raise ValueError("Days must be a whole number.")
                apr_days = int(days_input)
                if apr_days <= 0:
                    raise ValueError("Days must be greater than zero.")
                break
            except ValueError as e:
                print(e)
    
    #Return everything
    return {
        "Amount": amount,
        "Date": date_input,
        "Nec": nec,
        "Bank": {
            "Name": bank_name,
            "Deposit": deposit,
            "Gets_APR": gets_apr,
            "Rate": apr_rate,
            "Rate_Type": apr_type,
            "Days": apr_days
        }
    }

#Run the function
data = data_collect()
print("\nCollected Data:")
print(data)