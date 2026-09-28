import { useEffect, useState } from "react";

function App() {
  // sets the state for nodes and edges
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);

  // fetches data from the backend and sets the nodes and edges state
  useEffect(() => {
    fetch("http://127.0.0.1:8000/courses/graph")
      .then((response) => response.json())
      .then((data) => {
        setNodes(data.nodes);
        setEdges(data.edges);
      });
  }, []);

  return (
    <div>
      <p>Nodes: {nodes.length}</p>
      <p>Edges: {edges.length}</p>
    </div>
  );
}

export default App;
