for row in open('example_numbers_data.csv'):
    row = row.strip() #This is optional

    ###Using multiple ifs (rather than if, elif, else) rows will be duplicated if they meet more than one criteria
    
    if row.startswith('1'):
        print('starts with 1 ',row)

    if row.endswith('2'):
        print('ends with 2 ',row)