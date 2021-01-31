# make the class that have maximum feature of a clock to used in a program
# stopwatch
# timer
# local clock


import time



class ClockError(Exception):
    """A custom exception used to report errors in use of Clock class"""


class Clock:

    def __init__(self):
        pass

    class Stopwatch:
        def __init__(self):
            self._start_time = None

        def start(self):
            if self._start_time is not None:
                raise ClockError("Stopwatch is running use .stop() to stop.")
            self._start_time = time.perf_counter()

        def stop(self):
            if self._start_time is None:
                raise ClockError("Stopwatch is not running use .start() to start.")
            elapsed_time = time.perf_counter() - self._start_time
            self._start_time = None
            return elapsed_time


    def timer(self, t: "in seconds", initial):
        total_time = initial + t






    def local_clock(self):
        pass


import random
def trial():
    return random.choices('HT', cum_weights=(0.60, 1.00), k=7).count('H') >= 5


