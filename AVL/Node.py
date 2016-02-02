
class Node(object):
    
    def __init__(self,data, parentNode):
        self.data = data;
        self.parentNode = parentNode;
        self.leftChild = None;
        self.rightChild = None;
        self.balance = 0;
        
    def insert(self,data, parentNode):     
        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data, parentNode);
            else:
                self.leftChild.insert(data, self);
        else:
            if not self.rightChild:
                self.rightChild = Node(data, parentNode);
            else:
                self.rightChild.insert(data, self);
                
        return parentNode;
                
    def traverseInOrder(self):
        
        if self.leftChild:
            self.leftChild.traverseInOrder();
            
        print(self.data);
        
        if self.rightChild:
            self.rightChild.traverseInOrder();
        
        
        