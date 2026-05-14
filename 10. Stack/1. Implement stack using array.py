class myStack:
    def __init__(self, n):
        self.capacity = n
        self.top = -1
        self.stack = [0] * n

    
    def isEmpty(self):
        return self.top == -1

    
    def isFull(self):
        return self.top == self.capacity - 1

    
    def push(self, x):
        if self.top == self.capacity - 1:
            return
        
        self.top += 1
        self.stack[self.top] = x

    
    def pop(self):
        if self.top == -1:
            return -1
        
        x = self.stack[self.top]
        self.top -= 1
        return x

    
    def peek(self):
        if self.top == 0-1:
            return -1
        
        return self.stack[self.top]