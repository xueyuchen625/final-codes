import csv
import re


def get_week_ave_price_dic():
    week_price = {}
    week_ave_price = {}
    with open('calendar.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        result = list(reader)
        for row in result:
            # remove the first line
            if row[0] == 'listing_id':
                continue

            # price preprocess
            price = row[3]
            if price == '':
                price = 0
            else:
                price = re.findall('[a-zA-Z0-9]+', price)
                price = int(price[0])

            week = 0
            data_ele = row[1].split('-')
            day = int(data_ele[2])
            if day in range(1, 8):
                week = data_ele[0] + data_ele[1] + '01'
            elif day in range(8, 15):
                week = data_ele[0] + data_ele[1] + '02'
            elif day in range(15, 22):
                week = data_ele[0] + data_ele[1] + '03'
            elif day in range(22, 29):
                week = data_ele[0] + data_ele[1] + '04'
            else:
                week = data_ele[0] + data_ele[1] + '05'

            week_price.setdefault(int(week), []).append(price)

    for week in sorted(week_price):
        total_price = 0
        for price in week_price[week]:
            total_price += price
        week_ave_price.setdefault(week, []).append(total_price/len(week_price[week]))

    return week_ave_price

