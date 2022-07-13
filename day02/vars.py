#Day 2: 30 Days of Python programming
#declare first name variable
first_name = 'Danny'
#declare last name variable
last_name = 'White'
#declare full name variable
full_name = first_name + ' ' + last_name
#declare country variable
country = 'United States'
#declare city variable
city = 'panama city'
#declare age variable
age = 30
#declare a year variable
year = 2022
#declare a is_married variable
is_married = True
#declare multiple variables in one line
first_name, last_name, country, age, is_married = 'Danny', 'White', 'United States', 30, True
#print the values stored in the variables
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)

#get type of all variables
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))

#find length of all variables
print(len(first_name))
print(len(last_name))
print(len(country))
print(len(city))
print(len(str(age)))
print(len(str(is_married)))

#compare length of first_name and last_name
if len(first_name) > len(last_name):
    print('First name is longer than last name')

#declare values for num_one and num_two
num_one = 5
num_two = 4

#add num_one and num_two
print(num_one + num_two)
#subtract num_one and num_two
print(num_one - num_two)
#multiply num_one and num_two
print(num_one * num_two)
#divide num_one and num_two
print(num_one / num_two)
#divide num_one and num_two and round to 2 decimal places
print(round(num_one / num_two, 2))
#use modulus to find remainder of num_one and num_two
print(num_one % num_two)
#use floor division to find quotient of num_one and num_two
print(num_one // num_two)
#use exponential to find num_one to the power of num_two
print(num_one ** num_two)

#find area of a circle
radius = 30
pi = 3.14
area = pi * radius ** 2
print(area)

#find circumference of a circle
radius = 30
pi = 3.14
circumference = 2 * pi * radius