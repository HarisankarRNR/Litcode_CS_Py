
import sys
def Min(nums):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] < nums[high]:
            high = mid
        else:
            low = mid + 1

    return nums[low]
inp = list(map(int, input().split(' ')))
print(Min(inp))
                                                                                                                            