# -*- coding: utf-8 -*-
from python_http_runner.httprunner.common.utils import get_data_from_yml
from python_http_runner.httprunner.common.utils import get_url


def common_get(*args):
    data = {
        "env": "TEST",
        "key1": "value1",
        "key2": "value2",
        "url": ""
    }
    file = "../common/config.yml"
    content = get_data_from_yml(file)
    data["env"] = content["env"]
    data["key1"] = content["key1"]
    data["key2"] = content["key2"]
    data["url"] = get_url()
    value = ""
    if str(args[0]) in data.keys():
        value = data.get(str(args[0]))
    return value


def feature1_get(*args):
    data = {
        "key1": "key1",
        "key2": "key2",
    }
    value = ""
    if str(args[0]) in data.keys():
        value = data.get(str(args[0]))
    return value


def feature2_get(*args):
    data = {
        "key1": "key1",
        "key2": "key2",
    }
    value = ""
    if str(args[0]) in data.keys():
        value = data.get(str(args[0]))
    return value
