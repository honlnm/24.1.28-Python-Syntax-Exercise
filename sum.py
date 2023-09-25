def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  

    num_sum = 0
    for num in nums:
      num_sum = num_sum + num
    return num_sum


print("sum_nums returned", sum_nums([1, 2, 3, 4]))
