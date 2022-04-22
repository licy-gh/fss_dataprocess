import importlib
import json
import numpy as np
import pandas as pd
import json
import os

METRICS_PATH = './dp_metrics/'
TEST_PATH = './test/test.json' # 用户输入数据的json文件，根据实际地址改

metrics_impl = [os.path.splitext(f)[0] for f in os.listdir(METRICS_PATH) if f.endswith('.py')]
data = json.load(open(TEST_PATH))

op = data['operation']

if op in metrics_impl:
    dp_module = importlib.import_module('dp_metrics.' + op)
    if hasattr(dp_module, op):
        print('*** execute function {}'.format(op))
        res = {'res' : getattr(dp_module, op)(data)}
    else:
        res = '*** operation not found'

print(json.dumps(res)) # 直接打印结果