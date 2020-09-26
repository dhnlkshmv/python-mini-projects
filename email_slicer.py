# Created by xvidviii

# Email Slicer

email = input('Enter your Email ID: ').strip()

user_name = email[ : email.index("@")]

domain_name = email[ email.index("@")+1 : email.index('.') ]

print("Your Username is '{}' and your domain name is '{}'". format(user_name, domain_name))
