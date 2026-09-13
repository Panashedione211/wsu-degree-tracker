from courses import load_json_file, fill_map, select_course, get_full_chain, get_whats_left
        
            
                

#print(load_json_file('data/courses.json'))

json_data = load_json_file('data/courses.json')
#print(fill_map(json_data))
#chosen_course = select_course(fill_map(json_data))
#print(get_full_chain(chosen_course, fill_map(json_data)))
print(get_whats_left(fill_map(json_data)))
#print(topological_sort(fill_map(json_data)))
