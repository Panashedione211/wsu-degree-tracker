from fastapi import FastAPI
from courses import load_json_file, fill_map, topological_sort, get_whats_left




# create the FastAPI app
app = FastAPI()

#loads courses from json file and fills the map with the data
courses = fill_map(load_json_file("backend/data/courses.json"))


# endpoint to get courses
@app.get("/courses")
async def get_courses():
    return courses

# endpoint to get sorted courses
@app.get("/courses/sorted")
async def get_sorted_courses():
    return topological_sort(courses)


# endpoint to get all course + their connections
@app.get("/courses/graph")
async def get_course_graph():
    node = []
    edges = []
    
    for course in courses:
        node.append({"id": course, "data": {"label": course}})

        for prereq in courses[course]["prerequisites"]:
            edges.append({"source": prereq, "target": course})
    
    return {"nodes": node, "edges": edges}

# end point to get 1 course by id
@app.get("/courses/{course_id}")
async def get_course(course_id: str):
    if course_id in courses:
        return courses[course_id]
    else:
        return {"error": "Course not found"}
    

