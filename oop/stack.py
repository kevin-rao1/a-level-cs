class LinkedList:
    """
    A stack using a singly linked list to create a stack.
    """
    def __init__(self):
        self._head_node = None
        self._size = 0

    def __len__(self):
        """ Allows the use of len(stack) to find the number of elements in the stack """
        return self._size

    def push(self, data):
        new_node = Node(data, None)
        new_node.set_next(self._head_node)
        self._head_node = new_node

    def pop(self):
        data = self._head_node.get_data()
        if self.size >= 2:
            self._head_node = self._head_node.get_next()
        else:
            self.is_empty()
        return data

    def peek(self):
        return self._head_node.get_data()
    
    def is_empty(self):
        return self._size == 0
    
    def __str__(self):
        """ Defines what should be displayed when the user prints a linked list object. """
        while self._size >= 1:
            buffer = ""
            buffer = buffer + ", " + str(self._data)
        return buffer
    
class Node:
    def __init__(data, next_node):
        self._data = data
        self._next_node = next_node
    
    def set_next(next_node):
        self._next_node = next_node

    def get_data():
        return self._data
    
    def get_next():
        return self._next_node

if __name__ == "__main__":
    my_stack = LinkedList()

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    # my_stack.append(4)

    print(my_stack, len(my_stack))

    while not my_stack.is_empty():
        print(my_stack.pop())