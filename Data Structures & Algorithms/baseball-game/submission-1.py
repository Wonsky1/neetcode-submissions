class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        sum_ = 0
        for operation in operations:
            try:
                value = int(operation)
            except ValueError:
                value = None
            # print(number)
            match operation:
                case "+":
                    value = points[-1] + points[-2]
                case "C":
                    sum_ -= points.pop(-1)
                    
                    continue
                case "D":
                    value = points[-1] * 2
            sum_ += value
            points.append(value)
        
        return sum_
