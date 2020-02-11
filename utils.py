"""
This file contains functions that resolve common problems with the use of Data Structures
"""
from queue import Queue
from stack import Stack


"""
STACK APPLICATIONS
"""
def pair_checker(symbol_string):
    """
    Returns True when the input string has balanced characters, that means for example "()()" is balanced but
    "((()" is not.
    :param symbol_string:
    :return: boolean
    """
    s = Stack()

    for symbol in symbol_string:
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()

    return s.is_empty()


def pair_checker_1(symbol_string):
    """
    Same as above function but we are including "([{" options in the symbol_string with their corresponding closures
    :param symbol_string:
    :return: boolean
    """
    s = Stack()

    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    return False

    return s.is_empty()


def matches(open_symbol, close_symbol):
    """
    Method to check if closure and aperture match
    :param open_symbol:
    :param close_symbol:
    :return: boolean
    """
    opens = "([{"
    closes = ")]}"
    return opens.index(open_symbol) == closes.index(close_symbol)


"""
QUEUE APPLICATIONS
"""
def hot_potato(name_list, counter):
    """
    Simulate the hot potato game given a list of names and a counter which designates the time that
    the potate will be passed. It will return the name of the last "potato holder".
    :param name_list:
    :param counter:
    :return:
    """
    queue = Queue()
    for name in name_list:
        queue.enqueue(name)

    while queue.size() > 1:
        for i in range(counter):
            queue.enqueue(queue.dequeue())

        queue.dequeue()

    return queue.dequeue()



