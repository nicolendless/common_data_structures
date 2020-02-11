"""
This file contains functions that resolve common problems with the use of Data Structures
"""
import random
from basic_structures.queue import Queue
from basic_structures.stack import Stack


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


# PRINTER SIMULATION
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1  # decrement time counter
            if self.time_remaining <= 0:  # when finished set task to done
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time  # time that the task was created and placed in the printer queue
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):  # the time that the task has been waiting in the queue
        return current_time - self.timestamp


def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if not lab_printer.busy() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining."%(average_wait, print_queue.size()))


def new_print_task():
    num = random.randrange(1, 181)
    return num == 180  # print tasks arrive once every 180 seconds

