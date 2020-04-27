def twoSum(nums, target):
    # implement a pointer to check if number is larger than target -> increment pointer
    # if not, -> target - number then check if remainder is in the rest of the list
    # if yes, -> get index of remainder, return index and pointer
    # if not, -> increment pointer and check step 2

    i = 0
    while i < len(nums):
        if nums[i] > target:
            i += 1
        elif nums[i] < target:
            rem = target - nums[i]

            if rem in nums[i+1:]:
                idx = nums.index(rem)
                sol = [i, idx]
                break
            else:
                i += 1
    return sol

nums = [2, 7, 11, 15]
target = 9
twoSum(nums, target)

# def twoSum(nums, target):
#     h = {}
#     for i, num in enumerate(nums):
#         n = target - num
#         if n not in h:
#             h[num] = i
#         else:
#             return [h[n], i]
