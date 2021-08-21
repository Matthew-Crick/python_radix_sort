def num_rad_sort(nums, b):
    """
    Sorts an input list of nums by converting its elements to base b and through
    the use of buckets and recursion to non-comparatively order per digit and return the sorted elements.
    Complexity
    """

    nums_padded = []
    p = len(str(get_max(nums)))  # max digit length of the converted nums
    f = "%%0%dd" % p  # apply string format relative to p such that elements less than max digit length are padded

    for num in nums:
        #  apply format to nums such that elements less than max digit length are padded with 0's
        nums_padded.append((f % num))

    #  perform subroutine radix pass to non comparatively sort elements; returns the original elements sorted
    return radix_pass(nums_padded, 0, p, b)


def radix_pass(numbers, n, p, base):  # makes one pass sorting at index n

    buckets = []

    #  creates buckets relative to digits 0-9
    for i in range(10):
        buckets.append([])

    #  appends the num element to an index in buckets relative to its digit at digit n
    for num in numbers:
        buckets[int(num[n])].append(num)

    output = []

    #  iterate over the bucket elements; sublist of elements that share the same digit at digit n
    for b in buckets:

        #  if our iterations are less than the max digit length
        if n + 1 < p:
            #  recursive call with incremented n to reference next digit to iterate
            b = radix_pass(b, n + 1, p, base)

        #  once all digits have been sorted to our max digit length, append our sorted elements
        for i in b:
            output.append(int(i))

    return output


def get_max(numbers):
    """
    Returns the max value within a list of numbers
    Complexity
    """
    max_value = None
    for num in numbers:
        if max_value is None:
            max_value = num

        elif num > max_value:
            max_value = num

    return max_value


def test_radix_one():
    numbers = [23, 4, 432423]
    expected = [4, 23, 432423]
    assert expected == num_rad_sort(numbers, 7), "radix failed"
    print("test_radix_one has passed")


def test_radix_two():
    numbers = [23, 4]
    expected = [4, 23]
    assert expected == num_rad_sort(numbers, 3), "radix failed"
    print("test_radix_two has passed")


def test_radix_three():
    numbers = [43, 654, 43, 211, 6457, 7546, 85466, 23, 543, 765, 3, 43]
    expected = [3, 23, 43, 43, 43, 211, 543, 654, 765, 6457, 7546, 85466]
    assert expected == num_rad_sort(numbers, 4), "radix failed"
    print("test_radix_three has passed")


def test_radix_four():
    numbers = [23, 4, 9, 26, 87, 16, 52, 64, 36, 29, 21, 43]
    expected = [4, 9, 16, 21, 23, 26, 29, 36, 43, 52, 64, 87]
    assert expected == num_rad_sort(numbers, 8), "radix failed"
    print("test_radix_four has passed")


def test_radix_five():
    nums = [43, 101, 22, 27, 5, 50, 15]
    expected = [5, 15, 22, 27, 43, 50, 101]
    assert expected == num_rad_sort(nums, 9), "radix failed"
    print("test_radix_five has passed")


def test_radix_six():
    nums = [84999, 634, 54, 123, 4, 645, 8, 988, 5, 994]
    expected = [4, 5, 8, 54, 123, 634, 645, 988, 994, 84999]
    assert expected == num_rad_sort(nums, 252323), "radix failed"
    print("test_radix_six has passed")


def test_radix_seven():
    nums = [84999, 634, 54, 123, 4, 645, 8, 988, 5, 994]
    expected = [4, 5, 8, 54, 123, 634, 645, 988, 994, 84999]
    assert expected == num_rad_sort(nums, 535435345345), "radix failed"
    print("test_radix_seven has passed")


test_radix_one()
test_radix_two()
test_radix_three()
test_radix_four()
test_radix_five()
test_radix_six()
test_radix_seven()

