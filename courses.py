import json
from collections import deque

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

 # prints all the courses in the map and a user inputs a course
def select_course(course_map):
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
        
    
def get_whats_left(course_map):
    completed_courses = set()
    # user enters completed courses until they type 'done' if course isnt there it'll print not a valid course
    while user_input := input("Enter your completed courses (or 'done' to finish): ").strip():
        if user_input.lower() == 'done':
            break
        # add the course and its prerequisites to completed
        elif user_input in course_map:
            completed_courses.add(user_input)
            completed_courses.update(get_full_chain(user_input, course_map))
        else:
            print(f"{user_input} is not a valid course.")
    # user enters the course they're working towards so it can get compared to completed courses
    chosen_course = input("what course are you working towards? ")
    if chosen_course not in course_map:
        print(f"{chosen_course} is not a valid course.")
        return []
        # get the needed courses by comparing the full chain of the course they're working towards to the full chain of completed courses and return the difference
    still_needed_courses = set(get_full_chain(chosen_course, course_map)) - completed_courses
    full_order = topological_sort(course_map)
    still_needed_courses = [c for c in full_order if c in still_needed_courses]
    return still_needed_courses
        
def topological_sort(course_map):
    # dictionary stores tthe class and num of prerequisites
    in_degree  = {course: 0 for course in course_map}
    #adds 1 to the prerequisite count for every prerequisite of a course in the course_map
    for course in course_map:
        for prereq in course_map[course]['prerequisites']:
            in_degree[course] += 1
            
    # populated the queue with courses that have no prerequisites or have already been completed
    queue = deque([c for c in course_map if in_degree[c] == 0])
    sorted_courses = []
    
    # loop through the queue and pop completed courses and add then to the sorted courses list
    while queue:
        course = queue.popleft()
        sorted_courses.append(course)
        # loop through the prereqs of each course and decrement the in_degree of the prereq when the course is found  in the prereqs
        for prereq in course_map:
            if course in course_map[prereq]['prerequisites']:
                in_degree[prereq] -= 1
                # if its zero add it to the queue so it can be popped and added to sorted
                if in_degree[prereq] == 0:
                    queue.append(prereq)
        # if the length of sorted doesnt = course_map there has to be a cycle
    if len(sorted_courses) != len(course_map):
        print("There is a cycle in the prerequisites, topological sort not possible.")
        return []
    return sorted_courses