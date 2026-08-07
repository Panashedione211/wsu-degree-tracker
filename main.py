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

 # recursicly prints the prerequisites for a given course 
def print_course_prerequisites(course_map):
    for course in course_map:
        print(f"Course: {course}")
    chosen_course = input("Enter a course to see its prerequisites: ")
    return chosen_course

 
 # recursively prints the full chain of prerequisites for a given course   
def get_full_chain(chosen_course, course_map):
    chain = set()  # use a set to avoid duplicates
    # check if the chosen course has prerequisites if it doesnt returns the chain list
    if course_map[chosen_course]['prerequisites'] == []:
        return chain
    # for all the prerequesites in the choesen cours add it to the list then call the function again to get the prerequesites of the prerequesites
    else:
        for prereq in course_map[chosen_course]['prerequisites']:
            chain.add(prereq)
    
            chain.update(get_full_chain(prereq, course_map))
        sorted_chain = sorted(chain)  # sort the chain alphabetically
        return sorted_chain
        
    
    

#print(load_json_file('data/courses.json'))

json_data = load_json_file('data/courses.json')
#print(fill_map(json_data))
chosen_course = print_course_prerequisites(fill_map(json_data))
print(get_full_chain(chosen_course, fill_map(json_data)))

