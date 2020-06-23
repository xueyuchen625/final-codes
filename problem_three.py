import csv
import re

def get_result():
    month_prices = {}
    month_result_dic = {}

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

            data_ele = row[1].split('-')
            month = data_ele[0] + '-' + data_ele[1]
            month_prices.setdefault(str(month), []).append(price)

        # key: month, values 0: maximum, values 1: minimum, values 2: average
        for month in month_prices:
            month_prices[month].sort()
            max_price = month_prices[month][-1]
            min_price = month_prices[month][0]
            total_price = 0
            for price in month_prices[month]:
                total_price += price
            ave_price = total_price/len(month_prices[month])

            month_result_dic.setdefault(month, []).append(max_price)
            month_result_dic.setdefault(month, []).append(min_price)
            month_result_dic.setdefault(month, []).append(ave_price)

    return month_result_dic

def get_x_and_y(month_result_dic):
    x=[]
    y1=[]
    y2=[]
    y3=[]
    for month in month_result_dic:
        x.append(month)
        y1.append(month_result_dic[month][0])
        y2.append(month_result_dic[month][1])
        y3.append(month_result_dic[month][2])
    return x, y1, y2, y3
