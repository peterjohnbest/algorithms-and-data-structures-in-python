#!/usr/bin/python

from Queue import Queue;

queue = Queue()

queue.enqueue('Daniel')
queue.enqueue('Kevin')
queue.enqueue('Joe')

print(queue.dequeue())
print(queue.dequeue())
print(queue.size())
print(queue.dequeue())
print(queue.size())
