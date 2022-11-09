

# Function to find magic date:
def isMagicDate(day, month, year):    
    if day * month == year % 100:
        return True    
    return False

#function checks if a given year is leap year or not
def is_leap(year):
    if((year % 400 == 0) or(year % 100 != 0) and (year % 4 == 0)): 
        return True
    return False

def dayInMonths(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2: 
        if is_leap(year):
            return 29
        return 28
    return 31
print("All the magic dates in the 20th century are:\n")   
        
def main():
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            days = dayInMonths(month, year)
            for day in range(1, days + 1):
                if isMagicDate(day, month, year):
                    print(f'{day}/{month}/{year}: is a magic date')
                    count +=1
    print(f'Total magic days in 20th century are: {count}')
       
if __name__ == '__main__':
    main()
