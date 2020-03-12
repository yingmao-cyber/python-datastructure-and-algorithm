def selection_sort(array):
    """
    find the maximum element and move the maximum element to the back
    Time complexity: WorstCase: O(n^2), BestCase: O(n^2)
    Space complexity: O(1)
    :param array:
    :return:
    """
    for i in range(len(array)):
        max_value_index = 0
        for j in range(len(array) - i):
            if array[j] > array[max_value_index]:
                max_value_index = j
        max_element = array[max_value_index]
        array[max_value_index] = array[len(array) - i - 1]
        array[len(array) - i - 1] = max_element
        print(f'array: {array}, max_value_index: {max_value_index}, i: {i}')
    return array


def insertion_sort(array):
    """
    insert the right element to the left part of sorted array
    Time complexity: WorstCase: O(n^2), BestCase: O(n)
    Space complexity: O(1)
    :param array:
    :return:
    """
    for i in range(len(array) - 1):
        element = array[i + 1]
        element_index = i + 1
        print(f'array: {array}, element_to_be_inserted: {element}')
        for j in range(i + 1, 0, -1):
            if element < array[j - 1]:
                switch_index = j - 1
                temp = array[element_index]
                array[element_index] = array[switch_index]
                array[switch_index] = temp
                element_index -= 1
            # print(f'array: {array}, i: {i}, j: {j}')
        print(f'array: {array}, element_inserted: {element}')
    return array


def test_selection_sort():
    print(selection_sort([2, 1, 0, 9, 6]))


def test_insertion_sort():
    print(insertion_sort([1, 2, 3, 0]))
    print("")
    print(insertion_sort([1, 2, 3, 0, 4, 11, 5]))


if __name__ == "__main__":
    # test_selection_sort()
    test_insertion_sort()
