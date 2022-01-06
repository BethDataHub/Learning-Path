with open('example_numbers_data.csv') as f:
    rows = f.readlines()
    print(rows)

    for row in rows:
        row = row.strip() #This is optional, it removes the new line break between the printed values
        print(row)