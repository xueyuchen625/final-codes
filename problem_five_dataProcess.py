import csv
import re


def get_training_data():
    id_price = {}  # id-price, key: id, value: the price has rent previous
    id_informations = {}  # key: id, values: accommodates, bathrooms, bedrooms, beds
    with open('calendar.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        result = list(reader)
        for row in result:
            if row[0] == 'listing_id':
                continue
            if id_price.__contains__(row[0]):
                if row[3] != '':
                    price = re.findall('[a-zA-Z0-9]+', row[3])
                    price = int(price[0])
                    id_price[row[0]] = max(price, int(id_price[row[0]]))
            else:
                id_price[row[0]] = 0

    with open('listings.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        result = list(reader)
        count = 0
        for row in result:
            if row[0] == 'id':
                continue

            if row[53] != '':
                id_informations.setdefault(row[0], []).append(row[53])
            else:
                id_informations.setdefault(row[0], []).append(0)


            if row[54] != '':
                id_informations.setdefault(row[0], []).append(row[54])
            else:
                id_informations.setdefault(row[0], []).append(0)

            if row[55] != '':
                id_informations.setdefault(row[0], []).append(row[55])
            else:
                id_informations.setdefault(row[0], []).append(0)

            if row[56] != '':
                id_informations.setdefault(row[0], []).append(row[56])
            else:
                id_informations.setdefault(row[0], []).append(0)

        #print(id_informations['12544567'])

    list_id_info = sorted(id_informations.items(), key=lambda d: d[0])
    list_id_price = sorted(id_price.items(), key=lambda d: d[0])
    list_x = []
    list_y = []
    list_id = []
    for i in range(len(list_id_info)):
        list_x.append(list_id_info[i][1])
        list_y.append(list_id_price[i][1])
        list_id.append(list_id_info[i][0])

    return list_id, list_x, list_y