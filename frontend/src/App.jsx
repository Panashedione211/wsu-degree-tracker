import { useEffect, useState } from "react";
import { ReactFlow } from "@xyflow/react";
import "@xyflow/react/dist/style.css";

function App() {
  // sets the state for nodes and edges
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);

  // fetches data from the backend and sets the nodes and edges state
  useEffect(() => {
    fetch("http://127.0.0.1:8000/courses/graph")
      .then((response) => response.json())
      .then((data) => {
        const nodePos = data.nodes.map((node) => ({
          ...node,
          position: { x: 0, y: 0 },
        }));
        setNodes(nodePos);
        setEdges(data.edges);
      });
  }, []);

  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <ReactFlow nodes={nodes} edges={edges} fitView />
    </div>
  );
}

export default App;
