"""
Programming for linguists

Tests for Queue from stack class.
"""

import unittest

from queue_.queue_ import FullQueue, InfiniteQueue
from queue_.queue_from_stack import Queue_
from stack.stack import Stack


class QueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue from stack
    """

    def test_queue_data_is_stack(self):
        """
        Create an empty Queue from stack.
        Test that its data field type is Stack.
        """
        stack = Stack([1, 2, 3, 4, 5])
        queue = Queue_(stack)
        self.assertTrue(isinstance(queue.in_stack, Stack))

    def test_new_queue_is_empty(self):
        """
        Create a Queue with an empty stack.
        Test that its size is 0.
        """
        queue_from_stack = Queue_()
        self.assertTrue(queue_from_stack.empty())
        self.assertEqual(queue_from_stack.size(), 0)

    def test_get_element(self):
        """
        Get an element from a queue created from stack.
        Test that it is 1.
        """
        stack = Stack([1, 2, 3, 4])
        queue = Queue_(stack)
        self.assertEqual(queue.get(), 1)

    def test_put_element(self):
        """
        Put an element in queue with an empty stack.
        Test that its size is 1.
        """
        queue_from_stack = Queue_()
        queue_from_stack.put(2)
        self.assertFalse(queue_from_stack.empty())
        self.assertEqual(queue_from_stack.size(), 1)
        self.assertEqual(queue_from_stack.top(), 2)

    def test_call_get_of_empty_queue_raised_error(self):
        """
        Create a Queue with an empty stack.
        Test that call of get function raises IndexError
        """
        queue_from_stack = Queue_()
        self.assertRaises(IndexError, queue_from_stack.get)

    def test_new_queue_with_max_size(self):
        """
        Create a full Queue_ from stack with max_size.
        Test that its field max_size is filled correctly and if data size is bigger than max_size,
        the needed slice is taken
        """
        queue_from_stack = Queue_(Stack([7, 8, 9, 10, 11, 12]), max_size=4)
        self.assertEqual(queue_from_stack.maximum_size, 4)
        self.assertEqual(len(queue_from_stack.in_stack.data), 4)

    def test_put_element_into_full_queue(self):
        """
        Put element into a queue (created from stack) that is already full.
        Test that call of put function raises Full exception
        """
        stack = Stack([1, 2, 3, 4, 5])
        queue = Queue_(stack, 5)
        self.assertRaises(FullQueue, queue.put, 6)
        queue.get()
        queue.put(6)
        self.assertEqual([2, 3, 4, 5, 6], queue.in_stack.data)

    def test_limited_queue_is_full(self):
        """
        Create a full limited Queue_ from stack.
        Test that call of full function returns True
        """
        stack = Stack([1, 2, 3, 4, 5])
        queue = Queue_(stack, 5)
        self.assertTrue(queue.full())
        queue.get()
        self.assertFalse(queue.full())

    def test_infinite_queue_is_not_full(self):
        """
        Create a nonempty infinite Queue_ from stack.
        Test that call of full function returns False
        """
        stack = Stack([1, 2, 3, 4, 5])
        queue = Queue_(stack)
        self.assertRaises(InfiniteQueue, queue.full)
