class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        return self.stack1
        
        

    def pop(self) -> int:
        if self == []:
            return None
        else:
            return self.stack1.pop(0)
        

    def peek(self) -> int:
        if self == []:
            return None
        else:
            self.stack2 = self.stack1.copy()
            return self.stack2.pop(0)
        

    def empty(self) -> bool:
        return False if self.stack1 else True
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
