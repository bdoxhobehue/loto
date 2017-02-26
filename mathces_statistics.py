from collections import namedtuple
from collections import deque
from collections import Counter
from copy import copy
from datetime import datetime
import operator
import requests
import re
from bs4 import BeautifulSoup
from random import random


def parse(url, params):
    # This method parse the site with teh input credentials, and returns deque-object of named_tuple with the next
    # structure namedtuple(draw_number:int,draw_date:str,draw_numbers:frozenset(ints))
    # Input: url:string
    #       params:string
    # Output: queue_of_numbers:deque

    new_request = requests.get(url, params)
    soup = BeautifulSoup(new_request.content, 'html.parser')
    draw_date = soup.findAll('div', {'class': 'draw_date'})
    lotoNumbers = namedtuple("Loto", "draw_number draw_date numbers")
    queue_of_numbers = deque()
    for i in reversed(range(1, len(draw_date))):
        numbers_div = draw_date[i].nextSibling.nextSibling.findAll('b')
        draws_div = draw_date[i].nextSibling.findAll('a')
        soup = BeautifulSoup(str(draws_div[0]), 'html.parser')
        temp = []
        for j in numbers_div:
            temp.append(int(re.search('\d+', j.text).group(0)))
        queue_of_numbers.append(lotoNumbers(int(soup.getText()), draw_date[i].text, frozenset(temp)))
    return queue_of_numbers


def check_matches(result, deepness):
    # This method print the percent of matches of current draw numbers in the previous  according to the deepness value
    temp_result = deque(result)
    if deepness != 1:
        check_matches(temp_result, deepness - 1)
    dict_of_matches = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }
    total_count = len(result)
    first_queue = deque()
    for i in range(deepness):
        first_queue.appendleft(result.pop())
    current = first_queue.pop()
    while len(result) != 0:
        previous = result.pop()
        dict_of_matches[len(current.numbers & previous.numbers)] += 1
        first_queue.appendleft(previous)
        current = first_queue.pop()

    print("Table of matches with deepness {}".format(deepness))
    for i in dict_of_matches:
        print(
            "Number of matches {0} is in {2:.4} %. In {1} cases".format(i, dict_of_matches[i],
                                                                        dict_of_matches[i] / total_count * 100))


# Initial parameters
url = 'http://www.stoloto.ru/6x45/archive'
params = {
    'firstDraw': '1',
    'lastDraw': '5000',
    'mode': 'draw'
}
print("Start Parsing")
result = parse(url, params)
print("Start Checking")
# Parametes of matches deepness
VALUE_OF_DEEP = 2
check_matches(result, VALUE_OF_DEEP)
