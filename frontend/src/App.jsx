import { useEffect, useState } from "react";
import { ReactFlow } from "@xyflow/react";
import "@xyflow/react/dist/style.css";
import dagre from "dagre";

// function to layout the nodes and edges in a top-bottom direction using dagre
const getLayoutedElements = (nodes, edges) => {
  const graph = new dagre.graphlib.Graph();
  graph.setDefaultEdgeLabel(() => ({}));
  graph.setGraph({ rankdir: "TB", ranksep: 100, nodesep: 80 });

  // for each node, set the width and height for layout calculations
  nodes.forEach((node) => {
    graph.setNode(node.id, { width: 150, height: 50 });
  });
  // for each edge, set the source (prerequisite) and target (class) for layout calculations
  edges.forEach((edge) => {
    graph.setEdge(edge.source, edge.target);
  });

  dagre.layout(graph);
  // set the position of each node based on the layout calculations
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
    <div className="w-screen h-screen bg-gray-950">
      <ReactFlow nodes={nodes} edges={edges} fitView colorMode="dark" />
    </div>
  );
}

export default App;
