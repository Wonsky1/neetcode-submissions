from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        queue = deque()
        operators = {"+", "-", "*", "/"}
        # char = tokens[0]
        # current_res = None
        for char in tokens:
            if char in operators:
                # print(queue)
                item_2 = queue.pop()
                item_1 = queue.pop()
                if char == "+":
                    queue.append(item_1 + item_2)
                if char == "-":
                    queue.append(item_1 - item_2)
                if char == "*":
                    queue.append(item_1 * item_2)
                if char == "/":
                    queue.append(int(item_1 / item_2))
            else:
                queue.append(int(char))
        return queue.pop()
            
