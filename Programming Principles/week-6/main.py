try:
    value = input('Enter your score out of 50: ')
    percentage = int(value) / 50 * 100
    print('You scored', round(percentage, 1), 'percent.')

except NameError:
    print('A NameError occurred!')

except TypeError:
    print('A TypeError occurred!')

except ValueError:
    print('A ValueError occurred!')

except:
    print('Some other exception occurred!')


