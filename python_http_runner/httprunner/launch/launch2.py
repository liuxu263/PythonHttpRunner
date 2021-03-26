# -*- coding: utf-8 -*-
import sys
import os
import yaml

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))

from python_http_runner.httprunner.common.utils import send_result


# 读取外部参数，并写入yml
def get_jenkins_input():
    content = {}
    env = "TEST"
    key1 = 1
    key2 = 2
    if len(sys.argv) == 4:
        env = sys.argv[1].split(',')
        key1 = sys.argv[2].split(',')
        key2 = sys.argv[3].split(',')
    else:
        os.system('echo Error: 输入参数的数量不正确！')
    file = "python_http_runner/httprunner/common/config.yml"
    with open(file, mode="w+", encoding="utf-8") as f:
        content["env"] = env
        content["key1"] = key1
        content["key2"] = key2
        yaml.dump(content, f)


# 启动httprunner
def launch_http_runner():
    pass


if __name__ == '__main__':
    get_jenkins_input()
    launch_http_runner()
    flag = "True"
    send_result(flag)
