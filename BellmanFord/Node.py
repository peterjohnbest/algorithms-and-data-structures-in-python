import sys;

class Node(object):
    
    def __init__(self, name):
        self.name = name;
        self.visited = False;
        self.predecessor = None;
        self.adjacenciesList = [];
        self.minDistance = sys.maxsize;