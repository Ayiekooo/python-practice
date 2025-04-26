# sum_list.py
# Ask the user for numbers, then add them up.

def sum_list(nums):
    # start at zero
    total = 0
    # for each number, add to total
    for n in nums:
        total += n
    return total

if __name__ == "__main__":
    data = input("Enter numbers separated by spaces: ")
    # make a list of ints
    nums = [int(x) for x in data.split()]
    result = sum_list(nums)
    print("The sum is", result)
