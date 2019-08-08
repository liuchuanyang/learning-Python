#!/Users/huan/anaconda3/bin/python
# coding=utf-8
path="/Users/huan/develop/learning-Python/chapter1/"
import json
data=[{"name":"liuhuan", "lang":("python", "English"), "age":40}]
print(data)
data_json=json.dumps(data)
print(data_json)
new_data=json.loads(data_json)
print(new_data)
data_j=json.dumps(data, sort_keys=True, indent=2)
print(data_j)
f=open(path+"yong.json", "r")
for line in f:
    print(line)
