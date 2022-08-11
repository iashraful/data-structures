from typing import List


class Node:
    def __init__(self, data: str | int | float) -> None:
        self.value = data
        self.next = None


class LinkedList:
    def __init__(self, array: List[str | int | float]) -> None:
        """
        Here we'll define the link list from the array/list provided in contructor.
        So, Let's do it.
        """
        arr_len = len(array)
        self.head = Node(data=array[0])
        _next = self.head.next
        for index in range(1, arr_len):
            if _next is None:
                _next = Node(data=array[index])
                self.head.next = _next
            else:
                _next.next = Node(data=array[index])
                _next = _next.next

    def print_as_list(self) -> List[str | int | float]:
        """
        Traverse the link list and print as list
        """
        _data = []
        _head = self.head
        while True:
            _data.append(_head.value)
            _head = _head.next
            if _head is None:
                break
        print(_data)
        return _data

    def insert_at_beginning(self, value: str | int | float) -> None:
        """
        This function insert an item to the beginning of the link list.
        """
        new_node = Node(data=value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_ending(self, value: str | int | float) -> None:
        """
        This function insert an item to the ending of the link list.
        """
        new_node = Node(data=value)
        _head = self.head
        while _head.next is not None:
            _head = _head.next
        _head.next = new_node

    def insert_at_middle(self, value: str | int | float, insert_after: int) -> None:
        """
        This function insert an item to the middle of the link list.
        insert_after is a position of iteration. IT'S NOT THE VALUE.
        """
        new_node = Node(data=value)
        _head = self.head
        iteration = 1
        while _head.next is not None:
            if iteration == insert_after:
                new_node.next = _head.next
                _head.next = new_node
            iteration += 1
            _head = _head.next


def main():
    link_list = LinkedList(array=[1, 4, 3, 5, 7, 9, 2])
    link_list.print_as_list()
    link_list.insert_at_beginning(value="TEST")
    link_list.print_as_list()
    link_list.insert_at_ending(value="END")
    link_list.print_as_list()
    link_list.insert_at_middle(value="MID", insert_after=2)
    # Output should be ['TEST', 1, 'MID', 4, 3, 5, 7, 9, 2, 'END']
    link_list.print_as_list()


if __name__ == "__main__":
    main()
