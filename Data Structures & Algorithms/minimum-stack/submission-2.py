
class MinStack:

    def __init__(self):
        self.min_ = None
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # print(f"""
        # current min stack: {self.min_stack}
        # current stack: ({self.stack})
        # """)
        if not self.min_stack or self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
            # self.min_stack.append()
        
        self.stack.append(val)

        # print(f"""
        # resulting min stack: {self.min_stack}
        # resulting stack: ({self.stack})
        # """)

    def pop(self) -> None:
        del self.stack[-1]
        del self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
