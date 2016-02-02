
def bfs(startNode):
		
	queue = [];
	startNode.visited = True;
	queue.append(startNode);

	#ez addig fog futni amig nem lesz ures, ez tipikus pythonos megoldas
	while queue: 

		actualNode = queue.pop();
		print("%s -> " % actualNode.name );
		
		for n in actualNode.adjacenciesList:
			if not n.visited:
				n.visited = True;
				queue.append(n);
