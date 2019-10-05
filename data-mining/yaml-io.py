import yaml

customer = [
    {"name": "InSeong", "age": "24", "gender": "men"},
    {"name": "Akatsuki", "age": "22", "gender": "woman"},
    {"name": "Harin", "age": "23", "gender": "man"},
    {"name": "Yuu", "age":"32", "gender": "woman"}
]

yaml_str = yaml.dump(customer)

print(yaml_str)
print("------------")

data = yaml.load(yaml_str,Loader=yaml.FullLoader)

for p in data:
    print(p["name"])
