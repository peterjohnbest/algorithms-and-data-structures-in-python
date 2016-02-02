from Dijkstra.Node import Node;
from Dijkstra.Edge import Edge;
from Dijkstra.Algorithm import Algorithm;

node1 = Node("A");
node2 = Node("B");
node3 = Node("C");

edge1 = Edge(1,node1,node2);
edge2 = Edge(1,node2,node3);
edge3 = Edge(0.1,node1,node3);

node1.adjacenciesList.append(edge1);
node1.adjacenciesList.append(edge2);
node2.adjacenciesList.append(edge3);


vertexList = {node1,node2,node3};

algorithm = Algorithm();
algorithm.calculateShortestPath(vertexList, node1);
algorithm.getShortestPathTo(node3);