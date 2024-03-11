def my_round(my_num):
    return round(my_num, 3)


# Length

def cm_to_inch_convert(my_cm):
    return my_round((my_cm * .393))


def m_to_feet_converter(my_m):
    return my_round((my_m * 3.281))


def k_to_miles_converter(my_k):
    return my_round((my_k * .621))


def inch_to_cm_converter(my_inch):
    return my_round((my_inch * 2.54))


def foot_to_m_converter(my_foot):
    return my_round((my_foot * .305))


def mile_to_k_converter(my_mile):
    return my_round((my_mile * 1.609))


# weight

def gram_to_ounce_converter(my_g):
    return my_round(my_g * .035)


def kg_to_pound_convertion(my_kg):
    return my_round(my_kg * 2.204)


def ounce_to_g_converter(my_ounce):
    return my_round(my_ounce * 28.35)


def pound_to_kg_converter(my_pound):
    return my_round(my_pound * .454)


# Volumn

def ml_to_fo_converter(my_ml):
    return my_round(my_ml * .035)


def l_to_quarts_converter(my_l):
    return my_round(my_l * .878)


def fo_to_ml_converter(my_fo):
    return my_round(my_fo * 28.413)


def quart_to_l_converter(my_quart):
    return my_round(my_quart * 1.137)


# cm to inch
# cm = float(input('Enter your cm value: '))
# print(cm, 'cm value is', cm_to_inch_convert(cm), 'inch')

# meter to feet
# m = float(input('Enter your meters value: '))
# print(m, 'meters value is', m_to_feet_converter(m), 'feet')

# km to miles
# k = float(input('Enter your km value: '))
# print(k, 'km value is', k_to_miles_converter(k), 'miles')

# inch to cm
# inch = float(input('Enter your inch value: '))
# print(inch, 'inch value is', inch_to_cm_converter(inch), 'centimeters')

# foot to m
# foot = float(input('Enter your floot value: '))
# print(foot, 'food value is', foot_to_m_converter(foot), 'meters')
#
# # mile to km
# mile = float(input('Enter your mile value: '))
# print(mile, 'mile value is', mile_to_k_converter(mile), 'km')

# weight

# g to ounce
# ounce = float(input('Enter your g value: '))
# print(ounce, 'g value is', gram_to_ounce_converter(ounce), 'ounce')

# # kg to pound
# kg = float(input('Enter your kg value: '))
# print(kg, 'kg value is', kg_to_pound_convertion(kg), 'pund')

# ounce to g
# ounce = float(input('Enter your ounce value: '))
# print(ounce, 'kg value is', ounce_to_g_converter(ounce), 'g')

# # pound to Kg
# pound = float(input('Enter your pound value: '))
# print(pound, 'pounds value is', pound_to_kg_converter(pound), 'Kg')


# volume

# ml to fluid pound
# ml = float(input('Enter your ml value: '))
# print(ml, 'ml value is', ml_to_fo_converter(ml), 'fluid pound')

# # l to quart
# l = float(input('Enter your l value: '))
# print(l, 'pounds value is', l_to_quarts_converter(l), 'quart')

# fluid ounce to ml
# fo = float(input('Enter your fluid ounce value: '))
# print(fo, 'fluid ounce value is', fo_to_ml_converter(fo), 'ml')

# quart ounce to l
quart = float(input('Enter your quart value: '))
print(quart, 'quart value is', quart_to_l_converter(quart), 'l')
