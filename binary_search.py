class BinarySearch(object):
    """
    Time complexity: O(log(n))
    """
    def __init__(self, array, value):
        self.array = array
        self.value = value

    def search(self):
        # iterative search
        left_index = 0
        right_index = len(self.array)
        while left_index <= right_index:
            middle_index = int((left_index + right_index) / 2)
            # [1, 2, 3, 4, 5]
            print(f'middle_index: {middle_index}, value: {self.array[middle_index]}')
            if self.array[middle_index] == self.value:
                return "Found value"
            elif self.array[middle_index] > self.value:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1
        return "Did not find value"


def recursive_search(array, value):
    left_index = 0
    right_index = len(array) - 1
    middle_index = int((left_index + right_index) / 2)
    print(f'array: {array}')
    if array[middle_index] == value:
        return "Found value"
    elif array[middle_index] > value:
        array = array[:middle_index-1]
        return recursive_search(array, value)
    else:
        array = array[middle_index+1:]
        return recursive_search(array, value)


def main():
    binary_search = BinarySearch([1, 2, 3, 4, 5], 4)
    print(binary_search.search())
    binary_search = BinarySearch([1, 2, 3, 4, 5, 6, 7], 2)
    print(binary_search.search())
    binary_search = BinarySearch([1, 2, 3, 4, 5, 6, 7], 1)
    print(binary_search.search())
    print("")
    print(recursive_search([1, 2, 3, 4, 5], 4))
    print(recursive_search([1, 2, 3, 4, 5, 6, 7], 2))
    print(recursive_search([1, 2, 3, 4, 5, 6, 7], 1))


if __name__ == "__main__":
    main()
