import math

def my_round(my_num):
    return round(my_num, 3)


# temperature

def fahren_to_celsius_conversion(my_fahren):
    return my_round((my_fahren - 32) * (5 / 9))

def celsius_to_fahren_conversion(my_celsius):
    return my_round((my_celsius * (9 / 5)) + 32)


# fahrenheit to celsius
fahren = float(input('Enter your fahrenheit value: '))
print(fahren, 'fahrenheit value is', fahren_to_celsius_conversion(fahren), 'celsius')

# # celsius to fahrenheit
celsius = float(input('Enter your celsius value: '))
print(celsius, 'celsius value is', celsius_to_fahren_conversion(celsius), 'fahrenheit')


# geometry
def area_of_cirle(r):
    return my_round(math.pi * r**2)

def cercum_of_circle(r):
    return my_round(2 * math.pi * r)

# celsius to fahrenheit
r = float(input('Enter radius of your circle value: '))
print('area of your circle is', area_of_cirle(r))
print('Circumference is your circle is', cercum_of_circle(r))

# nutrition
def bmi_canculator(my_w, my_h):
    return my_round(my_w / my_h**2)


w = float(input('Enter weight in Kg: '))
h = float(input('Enter height in meters: '))
print('your BMI value is', bmi_canculator(w, h))


# finance
def interest_calculator(my_amount, my_int, my_year):
    return my_round(my_amount * (my_int / 100) * my_year)

amount = float(input('Enter your amount value: '))
int = float(input('Enter your interest value: '))
year = float(input('Enter your time in years: '))
print('your interst value is', interest_calculator(amount, int, year))
