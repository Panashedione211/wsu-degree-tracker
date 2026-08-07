import json


def load_json_file(file):
    with open(file, 'r') as file:
        data = json.load(file)
        print("completed")
        return data
    
    """
def fill_map(data):
    map_data = {}
    for courses in data:
        map_data[course]
    """

print(load_json_file('data/courses.json'))