def two_sum(nums, target):
        for n, j in enumerate(range(len(nums))):
            for m, i in enumerate(range(len(nums))):
                if i == j:
                    break

                if (nums[n] + nums[i]) == target:
                    return [j, i]
                
nums = [1,2,3]
print(two_sum(nums,5))
