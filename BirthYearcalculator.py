birth_year = input('Birth Year: ')  # Taking user input as a string
print(type(birth_year))  # Printing the type of birth_year (it will be str)

age = 2024 - int(birth_year)  # Converting birth_year to int and calculating age
print(type(age))  # Printing the type of age (it will be int)

print(age)  # Printing the calculated age