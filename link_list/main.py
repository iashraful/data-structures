from copy import deepcopy
from typing import List


class Node:
    def __init__(self, data: str | int | float) -> None:
        self.value = data
        self.next = None


class LinkList:
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

    def print_as_list(self):
        """
        Traverse the link list and print as list
        """
        _head = deepcopy(self.head)
        _data = []
        while True:
            _data.append(_head.value)
            _head = _head.next
            if _head is None:
                break
        print(_data)
        return _data


def main():
    linklist = LinkList(array=[1, 4, 3, 5, 7, 9, 2])
    linklist.print_as_list()


if __name__ == "__main__":
    main()
