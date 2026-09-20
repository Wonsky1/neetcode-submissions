class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_table = {}
        t_table = {}

        for s_item, t_item in zip(s, t):
            if s_item in s_table:
                s_table[s_item] += 1
            else:
                s_table[s_item] = 1
            if t_item not in t_table:
                t_table[t_item] = 1
            else:
                t_table[t_item] += 1
        return s_table == t_table