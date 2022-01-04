###Match requires python 3.10 or newer

for row in open('example_numbers_data.csv'):
    row = row.strip() #This is optional

    match row:
        case '101':
            print('This row is 101')
        case '102':
            print('This row is 102')
        case '303':
            print('This row is 303')