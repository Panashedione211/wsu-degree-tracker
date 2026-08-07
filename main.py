import json

# loads data from a json file 
def load_json_file(file):
    with open(file, 'r') as file:
        data = json.load(file)
        print("completed")
        return data
    
    # fills a map with data from json file
def fill_map(data):
    map_data = {}
    for items in data:
        course = items['course']
        prereqs = items['prereqs']
        credits = items['credits']
        map_data[course] = {'prerequisites': prereqs, 'credits': credits}
    return map_data

#print(load_json_file('data/courses.json'))

json_data = load_json_file('data/courses.json')
print(fill_map(json_data))
