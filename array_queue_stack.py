class Array(object):
    def __init__(self):
        self.array = []

    def insert(self, index, element):
        self.array.insert(index, element)
        return self.array

    def add(self, element):
        # add the element to the front of the array
        newarray = [element]
        self.array = newarray + self.array
        return self.array

    def push(self, element):
        # push the element to the back of the array
        self.array.append(element)
        return self.array

    def pop(self):
        # self.array = self.array.pop()
        self.array = self.array[:-1]

    def remove_element(self, element):
        # self.array.remove(element)
        index = self.array.index(element)
        self.array = self.array[:index] + self.array[index + 1:]
        return self.array

    def get_element(self, index):
        try:
            return self.array[index]
        except Exception as err:
            print(err)

    def get_array(self):
        return self.array

    def reverse_array(self):
        # return self.array.reverse()
        array_len = len(self.array)
        for index in range(int(array_len / 2)):
            temp = self.array[array_len - 1 - index]
            self.array[array_len - 1 - index] = self.array[index]
            self.array[index] = temp
        return self.array


class Queue(Array):
    # first in first out
    def __init__(self, array: list = []):
        super(Queue, self).__init__()
        self.array = array

    def push_element_to_list(self, element):
        self.push(element)
        return self.array

    def remove_element_from_list(self):
        self.array = self.array[1:]
        return self.array


class Stack(Array):
    # last in first out
    def __init__(self, array: list = []):
        super(Stack, self).__init__()
        self.array = array

    def push_element_to_list(self, element):
        self.push(element)
        return self.array

    def pop_element_from_list(self):
        self.pop()
        return self.array


def main():
    array = Array()
    array.push("first_element")
    array.push("second_element")
    array.push("third_element")
    array.push("fourth_element")
    array.push("fifth_element")
    array.pop()
    array.remove_element("first_element")
    array.add("six_element")
    array.add("seventh_element")
    print(f'modified array: {array.get_array()}')
    # array.insert(1, "inserted_element")
    print(f'modified array: {array.get_array()}')
    array.get_element(4)
    array.reverse_array()
    print(f'reversed array: {array.get_array()}\n')

    queue = Queue(array = array.get_array())
    print(f'pushed queue: {queue.push_element_to_list("new_element_1")}')
    print(f'pushed queue: {queue.push_element_to_list("new_element_2")}')
    print(f'popped queue: {queue.remove_element_from_list()}\n')

    queue = Queue()
    print(f'pushed queue: {queue.push_element_to_list("new_element_1")}')
    print(f'pushed queue: {queue.push_element_to_list("new_element_2")}')
    print(f'popped queue: {queue.remove_element_from_list()}\n')

    stack = Stack()
    print(f'pushed stack: {stack.push_element_to_list("new_element_1")}')
    print(f'pushed stack: {stack.push_element_to_list("new_element_2")}')
    print(f'removed stack: {stack.pop_element_from_list()}')


if __name__ == "__main__":
    main()
