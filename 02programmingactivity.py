firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
email = input("Enter your email address: ")
phonenumber = input("Enter your phone number: ")
jobtitle = input("Enter your job title: ")
ID = input("Enter your ID number: ")
print()
print("Your ID Card: ")
print('_____________________________________________')
print(f'{lastname.upper()}, {firstname.capitalize()}')
print(f'{jobtitle.title()}')
print('ID: ' + ID + ' ')
print()
print(f'{email.lower()}')
print(f'{phonenumber}')
print('_____________________________________________')