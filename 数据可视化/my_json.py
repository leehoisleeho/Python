# 导入json模块
import json

data = [
    {"name": "leeho", "age": 29},
    {"name": "lihao", "age": 29}
]

# 把数据转成JSON
json_data = json.dumps(data)
print(type(json_data))
# JSON转成python
py_data = json.loads(json_data)
print(type(py_data))
