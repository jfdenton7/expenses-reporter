import csv

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

labels = {
    'starbucks': 'Travel',
    'food lion': 'Food',
    'greens': 'Travel',
    'cellar': 'Travel',
    'gillie': 'Travel',
    'sams': 'Food',
    'ninja cafe': 'Food',
    'amazon': 'Amazon',
    'venmo': 'Personal',
    'amzn': 'Amazon',
    'banana republic': 'Clothes/shoes/cologne',
    'fragrancenet': 'Clothes/shoes/cologne',
    'tilley': 'Clothes/shoes/cologne',
    'everlane': 'Clothes/shoes/cologne',
    'audible': 'Subscriptions',
    'netflix': 'Subscriptions',
    'spotify': 'Subscriptions',
    'j crew': 'Clothes/shoes/cologne',
    'alex mill': 'Clothes/shoes/cologne',
    'warby parker': 'Clothes/shoes/cologne',
    'wal-mart': 'Food',
    'kroger': 'Food',
    'steamgames': 'Books/Movies/Enter.',
    'capital one': 'Paycheck',
    'exxon': 'Transportation',
    'whitecreek market vale shawsville va': 'Transportation'
}


def descr_to_category(descr: str) -> str:
    for key in labels:
        if key in descr.lower():
            return labels[key]
    
    return None

def date_to_mm_dd_yyyy(date: str) -> str:
    
    month, day, year = date.split(' ')

    # print((month, day, year))
    day = day.replace(',', '')
    # move month to int
    for i in range(len(months)):
        if month in months[i]:
            month = i + 1
            break

    return str(month) + '/' + str(day) + '/' + str(year)


def write_expenses_to_csv(expenses):
    with open('output_expense_report.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')

        for row in expenses:
            writer.writerow(row)        


def gen_transformed_data(file_name: str):
    with open(file_name, newline='') as csv_file:
        transformed = []
        reader = csv.reader(csv_file)

        for transaction in reader:
            date, descr, amount = transaction        

            if descr_to_category(descr):
                category = descr_to_category(descr)
            else:
                print(f'failed to find description/label: {descr}')
                continue
        
            date = date_to_mm_dd_yyyy(date)

            amount = (amount.replace('-', '') if '-' in amount else amount)
            
            transformed.append((date, amount, descr, category))

        return transformed
    return None

if __name__ == '__main__':
    data = gen_transformed_data('july_expenses.csv')
    if data: write_expenses_to_csv(data)

    # for date, amount, descr, category in data:
    #     print(f'{date} {amount} {descr} {category}')

