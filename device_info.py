# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/9/18 15:31

import csv
import os


def get_device():
    csv_path = os.path.abspath(os.path.join(os.getcwd(), "device.csv"))
    devices = []
    with open(csv_path, 'r', encoding='utf-8') as fr:
        datas = csv.DictReader(fr)
        for data in datas:
            devices.append(data)
    return devices


if __name__ == "__main__":
    for device in get_device():
        print(device)
