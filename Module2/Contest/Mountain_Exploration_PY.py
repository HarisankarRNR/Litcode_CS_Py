
import sys
def heights(heights):
    if not all(isinstance(height, int) for height in heights):
        return "Input was not in a correct format"

    peaks = []
    count = 0

    for i in range(1, len(heights) - 1):
        if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
            peaks.append(heights[i])
            count += 1

    return f"{count}\n{' '.join(map(str, peaks))}"

heights = list(map(int, input().split(' ')))
output = heights(heights)
print(output)
                                                                                                                            