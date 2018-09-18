# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/9/18 15:28
import os
import subprocess
import time

from appium import webdriver

from device_info import get_device


device = get_device()[0]


class TestCase():

    def setup_class(self):
        self.desired_caps = device
        self.log_path = os.path.abspath(os.path.join(os.getcwd(), '{}.log'.format(self.desired_caps['deviceName'])))
        self.cmd_start = "appium -a 127.0.0.1 -p {} -bp {} ".format(self.desired_caps['port'], self.desired_caps['bootstrapPort'])
        self.p = subprocess.Popen(self.cmd_start, shell=True,
                             stdout=open(self.log_path, 'a'),
                             stderr=subprocess.STDOUT)
        self.driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(self.desired_caps['port']), self.desired_caps)

    def teardown_class(self):
        self.driver.quit()
        self.cmd_pid = "netstat -ano | findstr {}".format(self.desired_caps['port'])
        tasks = os.popen(self.cmd_pid)
        info = tasks.readline().split()
        tasks.close()
        pid = info[4]
        self.cmd_close = "taskkill -PID {} -F".format(pid)
        os.popen(self.cmd_close)

    def setup(self):
        self.driver.start_activity("com.netease.cloudmusic", "activity.LoadingActivity")
        self.driver.wait_activity("com.netease.cloudmusic.activity.LoadingActivity", 10, 1)

    def teardown(self):
        self.driver.keyevent('3')

    def test_one(self):
        try:
            self.driver.find_element_by_id("com.netease.cloudmusic:id/p1").click()
            time.sleep(2)
            if self.driver.find_element_by_id("com.netease.cloudmusic:id/a_0").is_displayed():
                assert True
        except Exception:
            assert False

    def test_two(self):
        try:
            self.driver.find_element_by_id("com.netease.cloudmusic:id/ayx").click()
            time.sleep(2)
            if self.driver.find_element_by_id("com.netease.cloudmusic:id/b47").is_displayed():
                assert True
            print("OK")
        except Exception:
            assert False
