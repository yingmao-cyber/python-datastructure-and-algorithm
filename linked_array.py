class LinkedArray(object):
    def __init__(self):
        self.list = None
        # self.head = None
        # self.tail = None

    @staticmethod
    def node(value):
        new_node = {
            "value": value,
            "next": None
        }
        return new_node

    def insert_value_at_end(self, value):
        new_node = self.node(value)
        temp = self.list
        if temp is None:
            self.list = new_node
            # self.head = new_node
            # self.tail = new_node
            return self.list
        else:
            while temp is not None:
                if temp["next"] is None:
                    # self.tail = new_node
                    temp["next"] = new_node
                    return self.list
                temp = temp["next"]

    def insert_value_with_index(self, value, index):
        new_node = self.node(value)
        count = 0
        temp = self.list
        if temp is None:
            self.list = new_node
            # self.head = new_node
            # self.tail = new_node
        else:
            while temp is not None:
                if count is index - 1:
                    new_node["next"] = temp["next"]
                    temp["next"] = new_node
                    return self.list
                if index is 0:
                    # self.head = new_node
                    new_node["next"] = temp
                    self.list = new_node
                    return self.list
                if temp["next"] is None and count is index - 1:
                    # self.tail = new_node
                    temp["next"] = new_node
                    return self.list
                temp = temp["next"]
                count += 1

    def delete_element_with_value(self, value):
        temp = self.list
        count = 0
        while temp is not None:
            if count is 0 and temp["value"] is value:
                self.list = temp["next"]
                return self.list
            if temp["next"]["next"] is None and temp["next"]["value"] is value:
                temp["next"] = None
                return self.list
            if temp["next"]["value"] is value:
                temp["next"] = temp["next"]["next"]
                return self.list
            temp = temp["next"]
            count += 1

    def traverse_list(self):
        temp = self.list
        while temp is not None:
            print(temp)
            temp = temp["next"]

    def reverse_list(self):
        prev = None
        n = self.list
        while n is not None:
            # {data: 1, ref: {data: 2, ref: {data: 3, ref: None}}}
            # next1 = {data: 2, ref: {data: 3, ref: None}}
            # next2 = {data: 3, ref: None}
            # next3 = None
            next = n['next']
            print(f'next: {next}')

            # n['next']1 = None
            # n['next']2 = {data:1, ref:None}
            # n['next']3 = {data: 2, ref: {data: 1, ref: None}}
            n['next'] = prev
            print(f'prev: {prev}')

            # prev = n = {data:1, ref:None}
            # prev2 = n = {data: 2, ref: {data: 1, ref: None}}
            # prev3 = n = {data: 3, ref: {data: 2, ref: {data: 1, ref: None}}}
            prev = n
            print(f'current n {prev}')

            # n = next = {data: 2, ref: {data: 3, ref: None}}
            # n2 = {data: 3, ref: None}
            # n = None
            n = next
            print(f'n: {n}\n')
        print(f'prev: {prev}')
        self.list = prev

    def print_result(self):
        return f'list: {self.list}'


class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        # Deleting first node
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False

    def reverse_linkedlist(self):
        prev = None
        n = self.start_node
        while n is not None:
            # {data: 1, ref: {data: 2, ref: {data: 3, ref: None}}}
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.start_node = prev


def test_linked_array():
    linkedarray = LinkedArray()
    linkedarray.insert_value_at_end(2)
    print(f'insert element at end: \n{linkedarray.print_result()}')
    linkedarray.insert_value_at_end(3)
    print(f'insert element at end: \n{linkedarray.print_result()}')
    linkedarray.insert_value_with_index(4, 0)
    print(f'insert new node at index 0: \n{linkedarray.print_result()}')
    linkedarray.insert_value_with_index(5, 2)
    print(f'insert new node at index 2: \n{linkedarray.print_result()}')
    linkedarray.insert_value_with_index(6, 4)
    # print(f'insert new node at final: \n{linkedarray.print_result()}')
    # linkedarray.delete_element_with_value(6)
    # print(f'delete node at final: \n{linkedarray.print_result()}')
    # linkedarray.delete_element_with_value(2)
    # print(f'delete the second node: \n{linkedarray.print_result()}')
    # linkedarray.delete_element_with_value(4)
    # print(f'delete the first node: \n{linkedarray.print_result()}\n')
    # print("traverse list")
    # linkedarray.insert_value_at_end(8)
    # linkedarray.traverse_list()
    print('')
    linkedarray.reverse_list()
    print(f'reversed list: {linkedarray.print_result()}')

def test_linked_array_reverse():
    linkedarray = LinkedArray()
    linkedarray.insert_value_at_end(1)
    linkedarray.insert_value_at_end(2)
    linkedarray.insert_value_at_end(3)
    print('')
    linkedarray.reverse_list()
    print(f'reversed list: {linkedarray.print_result()}')

def test_linked_list():
    linkedlist = LinkedList()
    linkedlist.insert_at_start(1)
    linkedlist.insert_at_start(2)
    linkedlist.insert_at_start(4)
    linkedlist.insert_at_index(2, 3)
    linkedlist.traverse_list()
    linkedlist.reverse_linkedlist()
    print('')
    linkedlist.traverse_list()

if __name__ == "__main__":
    test_linked_array_reverse()
    # test_linked_list()
