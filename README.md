# WSU CS Degree Tracker

A tool to visualize Washington State University Computer Science degree requirements as a dependency graph (DAG) — see prerequisite chains and track progress toward graduation.

## Why
Degree requirements are usually shown as flat lists, which makes it hard to see how courses actually depend on each other. This models them as a graph so students can see what's unlocked, what's blocking what, and plan their remaining semesters accordingly.

## Status
 In progress — starting with a static course/prerequisite dataset before building out graph logic and UI.

update 1: I converted the JSON into a map and allow the user to input a class, then get the full chain of prereqs from that class

## Data
`data/courses.json` contains WSU CPT S core and upper-level courses with prerequisite relationships, pulled from the official course catalog.

**Known limitation:** some WSU prerequisites are OR-conditions (e.g. CPT S 360 requires CPT S 260 *or* EE 234). This dataset currently models a single path per course for simplicity; true OR-logic support is a planned improvement.

## Data Structure
```json
{
  "course": "CPT S 122",
  "prereqs": ["CPT S 121"],
  "credits": 4
}
```
Completion status is intentionally left out of the base dataset — it's meant to be user-specific state (tracked in the app), not baked into the course data, so the tool works for any student.

## Tech Stack
TBD

## Roadmap
- [ ] Model course data as a proper DAG
- [ ] Build UI to visualize prerequisite chains
- [ ] Add user-specific completion tracking
- [ ] Support OR-logic prerequisites
