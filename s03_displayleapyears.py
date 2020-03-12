counter = 1
for years in range(2001,2101):
    if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
        print(years, end = " ")
        if counter % 10 == 0:
            print()
        counter += 1