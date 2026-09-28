import { useEffect, useState } from "react";
import { ReactFlow } from "@xyflow/react";
import "@xyflow/react/dist/style.css";
import dagre from "dagre";

const getLayoutedElements = (nodes, edges) => {
  const graph = new dagre.graphlib.Graph();
  graph.setDefaultEdgeLabel(() => ({}));
  graph.setGraph({ rankdir: "TB" });

  nodes.forEach((node) => {
    graph.setNode(node.id, { width: 150, height: 50 });
  });
  edges.forEach((edge) => {
    graph.setEdge(edge.source, edge.target);
  });

  dagre.layout(graph);

  const layoutedNodes = nodes.map((node) => ({
    ...node,
    position: {
      x: graph.node(node.id).x,
      y: graph.node(node.id).y,
    },
  }));

  return { nodes: layoutedNodes, edges };
};

function App() {
  // sets the state for nodes and edges
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);

  // fetches data from the backend and sets the nodes and edges state
  useEffect(() => {
    fetch("http://127.0.0.1:8000/courses/graph")
      .then((response) => response.json())
      .then((data) => {
        const { nodes: layoutedNodes, edges: layoutedEdges } =
          getLayoutedElements(data.nodes, data.edges);
        setNodes(layoutedNodes);
        setEdges(layoutedEdges);
      });
  }, []);

  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <ReactFlow nodes={nodes} edges={edges} fitView />
    </div>
  );
}

export default App;
