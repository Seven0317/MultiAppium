# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/9/18 10:34

import logging
import time


def logger(level):
    def decorator(func):
        def wrapper(*args):
            str1 = 'hello'
            start = time.time()
            func(str1)
            end = time.time()
            print("Function {} running time is : {} s".format(func.__name__, start - end))
            # print(level)
            logger = logging.getLogger()
            logger.setLevel(level)
            logging.info("Function {} running time is : {} s".format(func.__name__, start - end))
        return wrapper
    return decorator


@logger("INFO")
def my_upper(text):
    value = text.upper()
    print(value)


if __name__ == "__main__":
    my_upper()