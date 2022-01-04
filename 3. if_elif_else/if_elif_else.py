for row in open('example_numbers_data.csv'):
    row = row.strip() #This is optional
    
    ###Using if, elif and else once a criteria has been met it will move onto the next row (rather than evaluation other statements)

    if row.startswith('1'):
        print('starts with 1 ',row)

    elif row.endswith('2'):
        print('ends with 2 ',row)

    else:
        print('no matching criteria ',row)
