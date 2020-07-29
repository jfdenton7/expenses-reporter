import matplotlib.pyplot as plt
import numpy
from transform_usaa_table_to_spread import (
    gen_transformed_data,
    write_expenses_to_csv
)


def get_amount(data):
    temp = []
    for _, amount, _, _ in data:
        # amount = amount.replace('$', '')
        amount = amount.replace('$', '').replace(',', '') if ',' in amount else amount.replace('$', '')
        temp.append(float(amount))
    return temp

def get_labels(data):
    labels = []
    for _, _, _, label in data:
        labels.append(label)
    return labels

def remove_paycheck(amounts, labels):
    temp_amounts = []
    temp_labels = []

    for i in range(len(labels)):
        if 'paycheck' not in labels[i].lower():
            temp_amounts.append(amounts[i])
            temp_labels.append(labels[i])
    
    return temp_amounts, temp_labels

def aggregate_labels(amounts, labels):
    label_amount = {}

    for i in range(len(labels)):
        if labels[i] in label_amount:
            label_amount[labels[i]] += amounts[i]
        else:
            label_amount[labels[i]] = amounts[i]

    return list(label_amount.values()), list(label_amount.keys())

def compute_perc(pct, allvals):
    absolute = int(pct/100.0 * numpy.sum(allvals)) # calc actual cost
    return "{:.1f}%\n(${:.2f})".format(pct, absolute)

def get_dates(data):
    temp = []
    for date, _, _, _ in data:
        temp.append(date)
    return temp

def annotate_bar_chart_expenses(bars):
    pass

def gen_pie():
    '''
    main logic to build graphs 

    planned features:
        - automate month grab 
        - expand total number of graphs
        - expand labels/categories
        
    '''
    # get and transform data 
    data = gen_transformed_data('july_expenses.csv')
    amounts = get_amount(data)
    labels = get_labels(data)
    dates = get_dates(data)
    width = 0.35

    amounts, labels = remove_paycheck(amounts, labels)
    amounts, labels = aggregate_labels(amounts, labels)

    # start pie chart build
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    wedges, texts, autotexts = ax.pie(amounts, labels=labels, autopct=lambda pct: compute_perc(pct, amounts))
    ax.set_title('Percent Expense')
    ax.legend(
        wedges, labels,
        title='Expense Categories',
        loc='best',
        bbox_to_anchor=(1, 0, 0.5, 1)
    )
    plt.setp(autotexts, size=8, weight="bold")    
    plt.show()

    return amounts, labels, dates


def gen_bar(amounts, dates):
    data = gen_transformed_data('july_expenses.csv')
    amounts = get_amount(data)
    labels = get_labels(data)
    dates = get_dates(data)
    width = 2
    # FIXME (should remove date)
    amounts, labels = remove_paycheck(amounts, labels)


    x = numpy.arange(len(dates))

    # start bar chart build
    fig, ax = plt.subplots()    
    rects2 = ax.bar(dates, amounts, width, label='July')

    ax.set_title('Daily Cost')
    ax.set_ylabel('Cost (in dollars)')
    ax.set_xticks(x)
    ax.set_xticklabels(dates)
    ax.legend()

    fig.tight_layout()

    plt.show()

if __name__ == '__main__':
    amounts, labels, dates = gen_pie()
    gen_bar(amounts, dates)