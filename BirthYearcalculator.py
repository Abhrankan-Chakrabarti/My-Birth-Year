from datetime import datetime

birth_year = input('Birth Year: ')  # Taking user input as a string
current_year = datetime.now().year  # Getting the current year from the system
age = current_year - int(birth_year)  # Calculating age

print(age)  # Printing the calculated age