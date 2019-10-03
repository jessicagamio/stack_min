class Stack():
    """ build a stack that will show you the most current minum value in stack
    """

    def __init__(self):
        self._stack = []
        self.min = []

    def push(self, item):
        """ 
        append item to stack. 
        If min is empty
            append to item to min
        elif item less than or equal to last element in min
            append item to min """
        self._stack.append(item)

        if self.min == []:
            self.min.append(item)

        elif item <= self.min[-1]:
            self.min.append(item)

    def pop(self):
        """If the most recently added element in min is equal to popped item. 
                Pop item from min"""
        popped_item = self._stack.pop()
        if self.min[-1] == popped_item:
            self.min.pop()

    def min_value(self):
        return self.min[-1]

    def peek(self):
        return self._stack[0]

    def isEmpty(self):
        if len(self._stack) == 0:
            return True
        else:
            return False


myNewStack=Stack()

myNewStack.push(7)
myNewStack.push(8)
myNewStack.push(1)
myNewStack.push(2)
print(myNewStack.min_value())
myNewStack.pop()
print(myNewStack.min_value())
myNewStack.pop()
print(myNewStack.min_value())

