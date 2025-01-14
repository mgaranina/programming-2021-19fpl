"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    def __init__(self, data: Iterable = (), max_size: int = 0):
        if max_size and len(list(data)) > max_size:
            self.data = list(data)[:max_size]
        else:
            self.data = list(data)
        self.max_size = max_size

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        if not self.max_size or not self.full():
            self.data.append(element)
        else:
            raise FullQueue

    def get(self):
        """
        Remove and return an item from queue_
        """
        return self.data.pop(0)

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return not self.data

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return len(self.data)

    def top(self):
        """
        Return the element on the top of queue_
        :return: the element that is on the top of queue_
        """
        return self.data[0]

    def full(self):
        """
        Return whether queue_ is full or not
        :return: True if queue_ is full.
                 False if the queue_ is not full
        """
        if not self.max_size:
            raise InfiniteQueue

        if self.max_size and self.size() == self.max_size:
            return True

        return False


class FullQueue(Exception):
    """
    Raised when trying to put an element into a full queue
    """


class InfiniteQueue(Exception):
    """
    Raised when trying to call full function when a queue is infinite
    """
