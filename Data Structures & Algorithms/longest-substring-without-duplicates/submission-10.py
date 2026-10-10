class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        current_len = 0
        max_len = 0
        last_seen = {}

        for R in range(len(s)):
            last_seen_item_before = last_seen.get(s[R], -1)
            if last_seen_item_before >= L:
                L = last_seen_item_before + 1
                current_len = R - L
            last_seen[s[R]] = R
            current_len += 1
            max_len = max(max_len, current_len)
        return max_len
            

        # L = 0
        # current_set = set()
        # current_len = 0
        # max_len = 0
        # last_seen = {}
        # for R in range(len(s)):
        #     current_set.add(s[R])
            
        #     current_len = R + 1 - L
        # #     # print(f"""
        # #     # L={L}={s[L]}
        # #     # R={R}={s[R]}
        # #     # curr_set={current_set}
        # #     # curr_len={current_len}
        # #     # max={max_len}
        # #     # """)
        #     if current_len != len(current_set):
        # #         while s[L] in current_set:
        #             current_set = set(s[L+1:R+1])
        #             current_len = len(current_set)
        #             L = last_seen.get(s[R], 0) + 1
        #     last_seen[s[R]] = R
        # #             if L >= len(s):
        # #                 b
        #     max_len = max(max_len, current_len, len(current_set))
        # return max_len
            