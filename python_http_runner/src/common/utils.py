#! /user/bin/env python
# -*- coding:utf-8 -*-

import os
import yaml


def get_data_from_yml(file=None):
    with open(file=file, mode='r', encoding="utf-8") as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
    return content


def get_env():
    file = os.path.dirname(__file__) + "common/config"
    content = get_data_from_yml(file)
    env = "TEST"
    if content["env"] == "LIVE":
        env = "LIVE"
    return env


def get_url():
    base_url = ""
    env = get_env().lower()
    # 处理url
    url = ""
    return url


# 报警
def send_result(flag):
    flag = False
    if flag is True:
        pass
