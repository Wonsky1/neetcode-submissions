class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while r > l:
            shall_skip = False
            r_char = s[r].lower()
            l_char = s[l].lower()
            if not r_char.isalpha():
                if not r_char.isdigit():
                     r -= 1
                     shall_skip = True
            if not l_char.isalpha():
                if not l_char.isdigit():
                     l += 1
                     shall_skip = True
            
            print(f"checking {l_char}, {r_char}")
            # if r_char == " ":
            #     r -= 1
            #     print("skipping bc r_char is space")
            #     shall_skip = True
            # if l_char == " ":
            #     l += 1
            #     print("skipping bc l_char is space")
            #     shall_skip = True
            if shall_skip:
                continue
            if r_char != l_char:
                return False
            
            r -= 1
            l += 1
        return True
            