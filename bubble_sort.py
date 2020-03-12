def bubble_sort(array):
    """
    Time complexity: WorstCase: O(n^2), BestCase: O(n)
    Space complexity: O(1)
    :param array:
    :return:
    """
    count = 0
    for i in range(len(array)):
        flag = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
                flag = True
        count += 1
        print(f'array: {array}, count: {count}')
        if flag is False:
            return "Sorted"


if __name__ == "__main__":
    print(bubble_sort([2, 4, 1, 3, 5]))
    print("")
    print(bubble_sort([2, 4, 1, 3, 5, 9, 0]))
    print("")
    print(bubble_sort([1, 2, 3, 4, 5, 6]))
    print("")
    print(bubble_sort([6, 5, 4, 3, 2]))
