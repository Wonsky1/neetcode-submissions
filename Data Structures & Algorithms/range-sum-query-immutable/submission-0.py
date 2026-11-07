class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        sums = []
        for num in nums:
            if not sums:
                sums.append(num)
                continue
            sums.append(sums[-1] + num)
        # print(nums)
        # print(sums)
        self.sums = sums

    # (1, 2, 3, 4)
    # (1, 3, 6, 10)
    # sums[right] - sums[left - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        # print(self.sums[max(left - 1, 0)], self.sums[right])
        return self.sums[right] - self.sums[max(left - 1, 0)]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)