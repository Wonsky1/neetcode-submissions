class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # brackets = {
        #     "(": ")",
        #     "[": "]",
        #     "{": "}"
        # }
        open_brackets = "([{"
        closing_brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in open_brackets:
                stack.append(char)
                continue
            if not stack:
                return False
            
            if stack[-1] == closing_brackets[char]:
                stack.pop()
                continue
            return False
        print(stack)
                # if not stack:
                #     return False
                # if stack[-1] == open_brackets[closing_brackets.find(char)]:
                #     stack.pop()
        if stack:
            return False
        return True
        # stacks = {
        #     "(": [],
        #     "{": [],
        #     "[": []
        # }
        # open_brackets = "([{"
        # closing_brackets = ")]}"

        # for char in s:
        #     found_index = open_brackets.find(char)
        #     if found_index != -1:
        #         stacks[open_brackets[found_index]].append(1)
        #         continue
        #     if open_brackets[found_index] and open_brackets[found_index]:
        #         stacks[open_brackets[found_index]].pop()
        #         continue
        #     return False
        # for stacks_items in stacks.values():
        #     if stack_items:
        #         return False
        # return True
