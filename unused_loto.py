from datetime import datetime
import operator
import requests
import re
from bs4 import BeautifulSoup
from collections import Counter


class LotoNumbers:
    def __init__(self, date_str, numbers):
        self.date = datetime.strptime(date_str, '%d.%m.%Y %H:%M')
        # List of numbers
        self.numbers = numbers
        self.sum_of_numbers = sum(numbers)
        self.previous_number_1 = None
        self.previous_number_2 = None
        self.previous_number_3 = None

class LotoValues:
    def __init__(self, listofnumbers):
        self.numbers_counter = Counter()
    doubles_counter = {}
    # Count of doubles = 990
    dict_of_triples = {}
    # Count of triples = 14 190
    dict_of_fours = {}
    # Count of fours =  148 995
    dict_of_fives = {}
    # Count of fives =  1 221 759
    dict_of_sixes = {}
    # Count of sixes =  8 145 060
    for i in range(1, 41):
        for j in range(i+1, 42):
            for k in range(j+1, 43):
                for i1 in range(k+1, 44):
                    for j1 in range(i1+1, 45):
                        for k1 in range(j1+1, 46):
                            doubles_counter[(j1, k1)] = 0
                            dict_of_triples[(i1, j1, k1)] = 0
                            dict_of_fours[(k, i1, j1, k1)] = 0
                            dict_of_fives[(j, k, i1, j1, k1)] = 0
                            dict_of_sixes[(i, j, k, i1, j1, k1)] = 0

    print(len(doubles_counter))
    print(len(dict_of_triples))
    print(len(dict_of_fours))
    print(len(dict_of_fives))
    print(len(dict_of_sixes))


    def checkdoubles(self):
        for i in self.numbers_counter:
            for j in self.doubles_counter:
                if j[0] in self.numbers_counter[i].numbers:
                    if j[1] in self.numbers_counter[i].numbers:
                        self.doubles_counter[j] += 1

    def checktriples(self):
        for i in self.numbers_counter:
            for j in self.dict_of_triples:
                if j[0] in self.numbers_counter[i].numbers:
                    if j[1] in self.numbers_counter[i].numbers:
                        if j[2] in self.numbers_counter[i].numbers:
                            self.dict_of_triples[j] += 1

    def checkfours(self):
        for i in self.numbers_counter:
            for j in self.dict_of_fours:
                if j[0] in self.numbers_counter[i].numbers:
                    if j[1] in self.numbers_counter[i].numbers:
                        if j[2] in self.numbers_counter[i].numbers:
                            if j[3] in self.numbers_counter[i].numbers:
                                self.dict_of_fours[j] += 1

    def checkfives(self):
        for i in self.numbers_counter:
            for j in self.dict_of_fives:
                if j[0] in self.numbers_counter[i].numbers:
                    if j[1] in self.numbers_counter[i].numbers:
                        if j[2] in self.numbers_counter[i].numbers:
                            if j[3] in self.numbers_counter[i].numbers:
                                if j[4] in self.numbers_counter[i].numbers:
                                    self.dict_of_fives[j] += 1

    def checksixes(self):
        for i in self.numbers_counter:
            for j in self.dict_of_sixes:
                if j[0] in self.numbers_counter[i].numbers:
                    if j[1] in self.numbers_counter[i].numbers:
                        if j[2] in self.numbers_counter[i].numbers:
                            if j[3] in self.numbers_counter[i].numbers:
                                if j[4] in self.numbers_counter[i].numbers:
                                    if j[5] in self.numbers_counter[i].numbers:
                                        self.dict_of_sixes[j] += 1

    def showdoubles(self, sort_key='unsorted'):
        if sort_key == 'sorted':
            sorted_e = sorted(self.doubles_counter.items(), key=operator.itemgetter(1))
            for i in range(len(sorted_e)):
                if sorted_e[i][1] != 0:
                    print("{0}   -    {1} raz".format(sorted_e[i][0], sorted_e[i][1]))
        else:
            for i in self.doubles_counter:
                if self.doubles_counter[i] != 0:
                    print("{0}   -    {1} raz".format(i, self.doubles_counter[i]))

    def showtriples(self, sort_key='unsorted'):
        if sort_key == 'sorted':
            sorted_e = sorted(self.dict_of_triples.items(), key=operator.itemgetter(1))
            for i in range(len(sorted_e)):
                if sorted_e[i][1] != 0:
                    print("{0}   -    {1} raz".format(sorted_e[i][0], sorted_e[i][1]))
        else:
            for i in self.dict_of_triples:
                if self.dict_of_triples[i] != 0:
                    print("{0}   -    {1} raz".format(i, self.dict_of_triples[i]))

    def showfours(self, sort_key='unsorted'):
        if sort_key == 'sorted':
            sorted_e = sorted(self.dict_of_fours.items(), key=operator.itemgetter(1))
            for i in range(len(sorted_e)):
                if sorted_e[i][1] != 0:
                    print("{0}   -    {1} raz".format(sorted_e[i][0], sorted_e[i][1]))
        else:
            for i in self.dict_of_fours:
                if self.dict_of_fours[i] != 0:
                    print("{0}   -    {1} raz".format(i, self.dict_of_fours[i]))

    def showfives(self, sort_key='unsorted'):
        if sort_key == 'sorted':
            sorted_e = sorted(self.dict_of_fives.items(), key=operator.itemgetter(1))
            for i in range(len(sorted_e)):
                if sorted_e[i][1] != 0:
                    print("{0}   -    {1} raz".format(sorted_e[i][0], sorted_e[i][1]))
        else:
            for i in self.dict_of_fives:
                if self.dict_of_fives[i] != 0:
                    print("{0}   -    {1} raz".format(i, self.dict_of_fives[i]))

    def showsixes(self, sort_key='unsorted'):
        if sort_key == 'sorted':
            sorted_e = sorted(self.dict_of_sixes.items(), key=operator.itemgetter(1))
            for i in range(len(sorted_e)):
                if sorted_e[i][1] != 0:
                    print("{0}   -    {1} raz".format(sorted_e[i][0], sorted_e[i][1]))
        else:
            for i in self.dict_of_sixes:
                if self.dict_of_sixes[i] != 0:
                    print("{0}   -    {1} raz".format(i, self.dict_of_sixes[i]))

    # def checkprevious(self):
    #     for i in reversed(self.numbers_counter):
    #         if self.numbers_counter[i].


dict_of_numbers = {
   1: LotoNumbers('10.12.1988 10:00', [10, 15, 32, 45, 7, 9]),
   2: LotoNumbers('11.12.1988 10:00', [11, 1, 32, 5, 7, 13])}

loto1 = LotoValues(dict_of_numbers)



#url = 'http://www.stoloto.ru/6x45/archive'
#params = {
#    'firstDraw': '1',
#    'lastDraw': '5000',
#    'mode': 'draw'
#}
#new_request = requests.get(url, params)
#
#soup = BeautifulSoup(new_request.content, 'html.parser')
#clear_data = soup.findAll('div', {'class': 'draw_date'})
#
#list_of_numbers = {}
#for i in reversed(range(1, len(clear_data))):
#    itr = clear_data[i].nextSibling.nextSibling.findAll('b')
#    temp = []
#    for j in itr:
#        temp.append(int(re.search('\d+', j.text).group(0)))
#    list_of_numbers[i] = LotoNumbers(clear_data[i].text, temp)
#result = LotoValues(list_of_numbers)



#print(LotoNumbers('10.11.2008 08:50', [10, 15, 32, 45, 7, 9]).date)