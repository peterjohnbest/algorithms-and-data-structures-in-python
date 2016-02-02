import heapq;

class Algorithm(object):
    
    def calculateShortestPath(self, vertexList, startVertex):
    
        q = [];
        startVertex.minDistance = 0;
        heapq.heappush(q, startVertex);
        
        while len(q) > 0 :
            
            actualVertex = heapq.heappop(q);
            
            for edge in actualVertex.adjacenciesList:
                u = edge.startVertex;
                v = edge.targetVertex;
                newDistance = u.minDistance + edge.weight;
                
                if newDistance < v.minDistance:             
                    v.predecessor = u;
                    v.minDistance = newDistance;
                    heapq.heappush(q, v);
                      
    def getShortestPathTo(self, targetVertex):
        print("Shortest path to vertex: ", targetVertex.minDistance);
        
        node = targetVertex;
        
        while node is not None:
            print("%s-> " % node.name);
            node = node.predecessor;
        
        
                
                
        
        