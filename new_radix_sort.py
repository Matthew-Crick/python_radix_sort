def num_rad_sort(numbers):  #  makes one pass sorting at index n
    numbers_padded = []
    q = len(str(max(numbers)))
    f = "%%0%dd" % q

    for num in numbers:
        numbers_padded.append((f % num))

    return radix_pass(numbers_padded, 0, q)

def radix_pass(numbers, n, p):  #  makes one pass sorting at index n
    buckets = []

    for i in range(10):
        buckets.append([])

    for num in numbers:
        buckets[int(num[n])].append(num)

    output = []

    for b in buckets:
        if n + 1 < p:
            b = radix_pass(b, n + 1, p)

        for i in b:
            output.append(int(i))

    return output

def max(numbers):

    max_value = None
    for num in numbers:
        if max_value is None:
            max_value = num

        elif num > max_value:
            max_value = num

    return max_value

def test_pass():
    print("test radix pass")
    numbers  = [23, 4, 432423]
    expected = [4, 23, 432423]
    assert expected == (num_rad_sort(numbers)), "radix pass failed"

#  assert (condition, print)
def test1():
    print("t1")
    numbers  = [23, 4]
    expected = [4, 23]
    assert expected == (num_rad_sort(numbers)), "radix pass failed"

def test2():
    print("t2")
    numbers = [43, 654, 43, 211, 6457, 7546, 85466, 23, 543, 765, 3, 43]
    expected = [3, 23, 43, 43, 43, 211, 543, 654, 765, 6457, 7546, 85466]
    assert expected == (num_rad_sort(numbers)), "radix pass failed"

def test3():
    print("t3")
    numbers  = [23, 4, 9, 26, 87, 16, 52, 64, 36, 29, 21, 43]
    expected = [4, 9, 16, 21, 23, 26, 29, 36, 43, 52, 64, 87]
    assert expected == (num_rad_sort(numbers)), "radix pass failed"

test_pass()
test1()
test2()
test3()
