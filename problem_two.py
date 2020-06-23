import csv
import re
import operator

def get_results():
    bedroom_dic = {}  # key:bedroom type(one or two bedrooms, etc), value: numbers
    bathroom_dic = {}  # key:bathroom type(one or two bathrooms, etc), value: numbers
    with open('listings.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        result = list(reader)
        for row in result:
            for ele in row:
                if ele == '':
                    ele = '*'

        for row in result:
            if row[0] == 'id' or row[54] == '' or row[55] == '':
                continue

            bathroom = row[54]
            bedroom = row[55]
            if bathroom_dic.__contains__(bathroom):
                bathroom_dic[bathroom] += 1
            else:
                bathroom_dic[bathroom] = 0

            if bedroom_dic.__contains__(bedroom):
                bedroom_dic[bedroom] += 1
            else:
                bedroom_dic[bedroom] = 0
        return bathroom_dic, bedroom_dic
