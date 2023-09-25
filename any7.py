def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    count = 0
    for num in nums: 
        if (num == 7):
            count = count + 1
    return True if (count > 0) else False

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

