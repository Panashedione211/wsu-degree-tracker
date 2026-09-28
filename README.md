# WSU CS Degree Tracker

A full stack web app that visualizes Washington State University Computer Science degree requirements as an interactive graph. Students can see prerequisite chains, track what they've completed, and plan their path to graduation.

## Why
Degree requirements are usually shown as flat lists, which makes it hard to see how courses actually depend on each other. This models them as a graph so students can see what's unlocked, what's blocking them, and plan their remaining semesters accordingly.

## Features
- **Full prerequisite chain** — recursively finds every course needed to reach a target class
- **What's left** — compare courses you've taken against a target class and get back only what you still need, in the order you should take them
- **Topological sort** — orders all courses in a valid sequence that respects every prerequisite rule
- **Interactive graph** — visualizes all courses and their connections as a node graph (in progress)

## Tech Stack
- **Backend:** Python, FastAPI, uvicorn
- **Frontend:** React, Vite, React Flow, Tailwind CSS
- **Data:** JSON (WSU CPT S course catalog — web scraping planned)

## How to Run

### Backend
From the project root:
```bash
uvicorn backend.app:app --reload
```
Runs at `http://localhost:8000`. API docs at `http://localhost:8000/docs`.

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Runs at `http://localhost:5173`.

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/courses` | All courses |
| GET | `/courses/sorted` | Courses in topological order |
| GET | `/courses/graph` | Nodes and edges for graph display |
| GET | `/courses/{course_id}` | Single course info |

## Data
`backend/data/courses.json` contains WSU CPT S core and upper-level courses with prerequisite relationships.

**Known limitation:** some WSU prerequisites are OR-conditions. This dataset currently models all prereqs as AND relationships. OR-logic support planned after web scraping is implemented.

```json
{
  "course": "CPT S 122",
  "prereqs": ["CPT S 121"],
  "credits": 4
}
```

## Roadmap
- [x] Full prerequisite chain lookup
- [x] Compare taken courses vs target class
- [x] Topological sort
- [x] FastAPI backend with REST endpoints
- [x] React Flow graph visualization
- [ ] Click nodes to mark courses complete
- [ ] Highlight available next courses
- [ ] Hover tooltip with course details
- [ ] Web scrape real WSU course data
- [ ] Specialization pathway recommendations
