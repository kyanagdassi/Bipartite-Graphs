
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.items = [None]*capacity
        self.front=0
        self.back=0
        self.capacity=capacity
        self.num_items=0


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items==0


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        return self.num_items==self.capacity


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if not Queue.is_full(self):
            if self.back==self.capacity-1:
                self.items[0]=item
                self.back=0
                self.num_items+=1
            elif Queue.size(self)==0:
                self.items[self.front]=item
                self.num_items+=1
                self.back=self.front
            else:
                self.back+=1
                self.items[self.back]=item
                self.num_items+=1
        else:
            raise IndexError('')


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if not self.is_empty():
            if self.front==self.capacity-1:
                self.front=0
                self.num_items-=1
                return self.items[self.capacity-1]
            else:
                self.front+=1
                self.num_items-=1
                return self.items[self.front-1]
        else:
            raise IndexError('')


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items


