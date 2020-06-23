import csv
import re
import operator

def get_sorted_amenities():
    amenities_counts_dic = {}
    topTen_dic = {}
    with open('listings.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        result = list(reader)
        amenities = []
        for row in result:
            for ele in row:
                if ele == '':
                    ele = '*'
            #amenity = re.findall('[a-zA-Z0-9]+', row[58])
            amenity = row[58].split(',')
            new_amenity = []
            for ele in amenity:
                ele = ele.strip('{')
                ele = ele.strip('}')
                ele = ele.strip('"')
                new_amenity.append(ele)

            if len(new_amenity) != 0:
                if new_amenity[0] != 'amenity':
                    for ele in new_amenity:
                        amenities.append(ele)

        for amenity in amenities:
            if amenity in amenities_counts_dic:
                amenities_counts_dic[amenity] += 1
            else:
                amenities_counts_dic[amenity] = 0

        sorted_x  = sorted(amenities_counts_dic.items(),key = operator.itemgetter(1), reverse=True)
        for i in range(0, 10):
            topTen_dic[sorted_x[i][0]] = sorted_x[i][1]
        return topTen_dic