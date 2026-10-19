class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []

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
                    del points[-1]
                    continue
                case "D":
                    value = points[-1] * 2
            points.append(value)
        return sum(points)
