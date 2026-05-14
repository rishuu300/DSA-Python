class myQueue:
    def __init__(self):
        self.stack = []


    def enqueue(self, x):
        self.stack.append(x)


    def dequeue(self):
        if not self.stack:
            return -1
        
        top = self.stack.pop()
        
        if not self.stack:
            return
        
        self.dequeue()
        self.stack.append(top)
        
        return top


    def front(self):
        if not self.stack:
            return -1
        
        top = self.stack.pop()
        
        if not self.stack:
            self.stack.append(top)
            return top
        
        item = self.front()
        self.stack.append(top)
        
        return item


    def size(self):
        return len(self.stack)