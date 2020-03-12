def merge_sort(array, left_index, right_index):
    """
    Time Complexity: WorstCase: O(nlog(n)), BestCase: O(nlog(n))
    Space Complexity: O(n)
    :param array:
    :param left_index:
    :param right_index:
    :return:
    """

    if left_index >= right_index:
        print("triggered return")
        return

    middle = (left_index + right_index)//2
    print(f'left_index: {left_index}, right_index: {right_index}')
    print(f'left_index: {left_index}, middle_index: {middle}')
    merge_sort(array, left_index, middle)
    print(f'middle_index_1: {middle + 1}, right_index: {right_index}')
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)


def merge(array, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]
    print(f'left_copy: {left_copy}, right_copy: {right_copy}')

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
            print("1")
        # Opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
            print("2")

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1
        print("3")

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1
        print("4")
    print(f'sorted_array: {array}\n')


if __name__ == "__main__":
    # merge_sort([2, 1, 4, 5], 0, 3)
    merge_sort([2, 1, 0, 9, 6], 0, 4)
