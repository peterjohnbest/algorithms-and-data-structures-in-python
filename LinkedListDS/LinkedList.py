from Node import *;

class LinkedList(object):
    
    def __init__(self):
        self.head = None;
    #O(1)    
    def insertStart(self,data):
        
        newNode = Node(data);
        
        if not self.head :
            self.head = newNode;
        else:
            newNode.nextNode = self.head;
            self.head = newNode;
    #O(1) not O(1)        
    def size(self):
        
        actualNode = self.head;
        size = 0;
        
        while actualNode is not None:
            size += 1;
            actualNode = actualNode.nextNode;
            
        return size;
        
    #O(n)    
    def traverseList(self):
        
        actualNode = self.head;
        
        while actualNode is not None:
            print("%d " % actualNode.data);
            actualNode = actualNode.nextNode;
    #O(n)        
    def insertEnd(self,data):
        
        newNode = Node(data);
        actualNode = self.head;
        
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode;
            
        actualNode.nextNode = newNode;
    #O(n)    
    def remove(self,data):
        if( self.head ):
            if( data == self.head.data ):
                self.head = self.head.nextNode;
            else:
                self.head.remove(data,self.head);
           
                    
                
            
        
  
