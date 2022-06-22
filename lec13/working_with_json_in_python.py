import json

json_data = '{"a":1, "b":2, "c":3}'
x = json.loads(json_data)
print(x)
print(x["a"])
print(x["b"])
print(x["c"])
with open("1.json", "w") as f:
    json.dump(x, f)
