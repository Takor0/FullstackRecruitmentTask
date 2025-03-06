def two_sum(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1
    while True:
        left_value = nums[left]
        right_value = nums[right]
        if left_value + right_value == target:
            return [left + 1, right + 1]
        elif left_value + right_value < target:
            left += 1
        else:
            right -= 1


test_cases = [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2]),
    ([0, 0, 2, 3, 9, 9, 9, 9], 5, [3, 4]),
]

for nums, target, expected_output in test_cases:
    output = two_sum(nums, target)
    assert output == expected_output, f"{output} != {expected_output}"
