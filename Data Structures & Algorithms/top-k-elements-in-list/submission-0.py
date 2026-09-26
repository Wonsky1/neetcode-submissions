from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        integer_count = defaultdict(int)
        k_biggest = []
        for num in nums:
            is_in = num in k_biggest
            current_cnt = integer_count.get(num, 0)
            upd_count = current_cnt + 1
            if not is_in:
                if len(k_biggest) < k:
                    k_biggest.append(num)
                    is_in = True
                else:
                    for index, biggest_itm in enumerate(k_biggest):
                        if upd_count > integer_count[biggest_itm]:
                            k_biggest[index] = num
                            break
            integer_count[num] = upd_count
        return k_biggest

                
            # if len(two_biggest) < 2 and num not is_in:
            #     is_in = True
            # if two_biggest >= 2:
            #     for biggest_itm in 

        #     integer_count[num] = upd_cnt
        # return 