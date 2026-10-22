class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # return 0
        total = 0
        current_window_t = sum(calories[:k - 1])
        l , r = 0, k - 1
        while r < len(calories):
            current_window_t += calories[r]
            if current_window_t > upper:
                total += 1
            elif current_window_t < lower:
                total -= 1
            current_window_t -= calories[l]
            l += 1
            r += 1
        return total
        # while r < len(calories):
        #     diff = r - l
        #     if diff == k:
        #         current_window_t += calories[r]
        #         l += 1
        #         r += 1
        #     elif diff > k:
        #         current_window_t -= calories[l]
        #         l += 1
        #         continue
        #     else:
        #         current_window_t += calories[r]
        #         r += 1
        #         continue
            
        #     if current_window_t > upper:
        #         total += 1
        #     elif current_window_t < lower:
        #         total -= 1
        # return total