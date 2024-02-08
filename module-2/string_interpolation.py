#name = 'Kristine'
#product = 'Python elearning course'

#email_content = f"""  
#Hi {name}

#Thank you for purchasing {product}

#Regards,

#Sales Team
#"""					# f is used to format the string

#print(email_content)

name = 'Kristine'
age = 12
product = 'Python elearning course'

greeting = "Hi {0}, you are listed as {1} years old and you have purchased: {2}. - {3}".format(name, age, product, 'Jordan')

print(greeting)