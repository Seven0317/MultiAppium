# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/9/17 17:11

from appium import webdriver
import subprocess
import pytest
import csv
import os


DEVICE_INFO = os.path.abspath(os.path.join(os.getcwd(), "device.csv"))


@pytest.fixture(scope="module")
def driver(index):
    def decorator(test_case):
        def wrapper(*args, **kwargs):
            devices = []
            with open(DEVICE_INFO, 'r', encoding='utf-8') as fr:
                datas = csv.DictReader(fr)
                for data in datas:
                    devices.append(data)
            desired_caps = devices[index]
            cmd_start = "appium -a 127.0.0.1 -p {} -bp {} ".format(desired_caps['port'], desired_caps['bootstrapPort'])
            p = subprocess.Popen(cmd_start, shell=True,
                                 stdout=open('Z:/{}.log'.format(desired_caps['deviceName']), 'a'),
                                 stderr=subprocess.STDOUT)
            driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(desired_caps['port']), desired_caps)

            test_case(driver)

            driver.quit()
            cmd_pid = "netstat -ano | findstr {}".format(desired_caps['port'])
            tasks = os.popen(cmd_pid)
            info = tasks.readline().split()
            tasks.close()
            pid = info[4]
            cmd_close = "taskkill -PID {} -F".format(pid)
            os.popen(cmd_close)
        return wrapper
    return decorator


