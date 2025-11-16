from datetime import datetime

# Get user input
date_input = input("Enter your birth date (mm/dd/yyyy): ")

# Validate the input format and ensure it's a valid date
try:
    birthdate = datetime.strptime(date_input, "%m/%d/%Y")
    
    # Check if date is not in the future
    if birthdate > datetime.now():
        print("Error: Birth date cannot be in the future!")
    else:
        # Calculate current age in years
        today = datetime.now()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        
        # Convert to European format (dd/mm/yyyy)
        european_format = birthdate.strftime("%d/%m/%Y")
        
        # Display results
        print(f"Your current age: {age} years")
        print(f"Birth date in European format: {european_format}")
        
except ValueError:
    print("Error: Invalid date format. Please use mm/dd/yyyy format.")
except Exception as e:
    print(f"Error: {e}")