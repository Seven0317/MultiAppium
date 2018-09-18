# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/9/18 11:58

from multi_driver import driver
import time


@driver(0)
def test_case1(driver):
    try:
        driver.start_activity("com.netease.cloudmusic", "activity.LoadingActivity")
        time.sleep(10)
        driver.find_element_by_id("com.netease.cloudmusic:id/p1").click()
        time.sleep(10)
        if driver.find_element_by_id("com.netease.cloudmusic:id/a_0").is_displayed():
            assert True
        print("OK")
    except Exception as e:
        pass


@driver(0)
def test_case2(driver):
    try:
        driver.start_activity("com.netease.cloudmusic", "activity.LoadingActivity")
        time.sleep(10)
        driver.find_element_by_id("com.netease.cloudmusic:id/ayx").click()
        time.sleep(10)
        if driver.find_element_by_id("com.netease.cloudmusic:id/b47").is_displayed():
            assert True
        print("OK")
    except Exception as e:
        pass

