import postgresql
from datetime import datetime
import operator
import requests
import re
from bs4 import BeautifulSoup
import time


class LotoNumbers:
    last_draw = 1

    def __init__(self, date_str, numbers, draw_number):
        self.date = datetime.strptime(date_str, '%d.%m.%Y %H:%M')
        # List of numbers
        self.numbers = frozenset(numbers)
        self.sum_of_numbers = sum(numbers)
        self.draw_number = draw_number
        if LotoNumbers.last_draw < draw_number:
            LotoNumbers.last_draw = draw_number


class LotoValues:
    def __init__(self, list_of_numbers):
        self.dict_of_numbers = list_of_numbers

    dict_of_doubles = {}
    # Count of doubles = 990
    for i in range(1, 45):
        for j in range(i + 1, 46):
            dict_of_doubles[frozenset({i, j})] = 0
    dict_of_triples = {}
    # Count of triples = 14 190
    for i in range(1, 44):
        for j in range(i + 1, 45):
            for k in range(j + 1, 46):
                dict_of_triples[frozenset({i, j, k})] = 0
    dict_of_fours = {}
    # Count of fours =  148 995
    for i in range(1, 43):
        for j in range(i + 1, 44):
            for k in range(j + 1, 45):
                for i1 in range(k + 1, 46):
                    dict_of_fours[frozenset({i, j, k, i1})] = 0
    dict_of_fives = {}
    # Count of fives =  1 221 759
    for i in range(1, 42):
        for j in range(i + 1, 43):
            for k in range(j + 1, 44):
                for i1 in range(k + 1, 45):
                    for j1 in range(i1 + 1, 46):
                        dict_of_fives[frozenset({i, j, k, i1, j1})] = 0

    def checkdoubles(self):
        for i in self.dict_of_numbers:
            for j in self.dict_of_doubles:
                if j.issubset(self.dict_of_numbers[i].numbers):
                    self.dict_of_doubles[j] += 1

    def checktriples(self):
        for i in self.dict_of_numbers:
            for j in self.dict_of_triples:
                if j.issubset(self.dict_of_numbers[i].numbers):
                    self.dict_of_triples[j] += 1

    def checkfours(self):
        for i in self.dict_of_numbers:
            for j in self.dict_of_fours:
                if j.issubset(self.dict_of_numbers[i].numbers):
                    self.dict_of_fours[j] += 1

    def checkfives(self):
        for i in self.dict_of_numbers:
            for j in self.dict_of_fives:
                if j.issubset(self.dict_of_numbers[i].numbers):
                    self.dict_of_fives[j] += 1

    def showdoubles(self, sort_key='unsorted'):
        if sort_key == 'sorted':
            sorted_e = sorted(self.dict_of_doubles.items(), key=operator.itemgetter(1))
            for i in range(len(sorted_e)):
                if sorted_e[i][1] != 0:
                    print("{0}   -    {1} raz".format(sorted_e[i][0], sorted_e[i][1]))
        else:
            for i in self.dict_of_doubles:
                if self.dict_of_doubles[i] != 0:
                    print("{0}   -    {1} raz".format(i, self.dict_of_doubles[i]))

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


def parse(url, params):
    new_request = requests.get(url, params)
    soup = BeautifulSoup(new_request.content, 'html.parser')
    draw_date = soup.findAll('div', {'class': 'draw_date'})

    list_of_numbers = {}
    for i in reversed(range(1, len(draw_date))):
        numbers_div = draw_date[i].nextSibling.nextSibling.findAll('b')
        draws_div = draw_date[i].nextSibling.findAll('a')
        soup = BeautifulSoup(str(draws_div[0]), 'html.parser')
        temp = []
        for j in numbers_div:
            temp.append(int(re.search('\d+', j.text).group(0)))
        list_of_numbers[i] = LotoNumbers(draw_date[i].text, temp, int(soup.getText()))
    return list_of_numbers


db = postgresql.open(r'pq://postgres:postgres@192.168.198.128:5432/lotonumbers')

upd_date_of_win = db.prepare(
    "UPDATE numbers SET date_of_win=$1 WHERE id=$2")
upd_date_of_proposing = db.prepare(
    "UPDATE numbers SET date_of_proposing=$1 WHERE id=$2")


dict_of_sets = {}
number_id = 1

for i in range(1, 41):
    for j in range(i + 1, 42):
        for k in range(j + 1, 43):
            for i1 in range(k + 1, 44):
                for j1 in range(i1 + 1, 45):
                    for k1 in range(j1 + 1, 46):
                        dict_of_sets[number_id] = frozenset(set([i, j, k, i1, j1, k1]))
                        number_id += 1

url = 'http://www.stoloto.ru/6x45/archive'
params = {
    'firstDraw': '1',
    'lastDraw': '5000',
    'mode': 'draw'
}

print("Start Parsing")
start_time = time.time()
list_of_numbers = parse(url, params)
result = LotoValues(list_of_numbers)
print("Time elapsed: {:.2} min".format((time.time() - start_time) / 60))

print('Checking fours')
start_time = time.time()
result.checkfours()
print("Time elapsed: {:.2} min".format((time.time() - start_time) / 60))

start_time = time.time()
print("2)Proposed numbers had to not be in the all previous fours combination")
count_fours = 0
for i in result.dict_of_fours:
    if result.dict_of_fours[i] != 0:
        count_fours += 1
        for j in dict_of_sets:
            if i.issubset(dict_of_sets[j]):
                upd_date_of_win(datetime.now(), j)
print("Time elasped: {:.2} min".format((time.time() - start_time) / 60))
print("Fours that have already participated {}".format(count_fours))
