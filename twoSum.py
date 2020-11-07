def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [7, 11, 7, 5, 21, 9, 4]
target = 9
print(twoSum(nums, target))
