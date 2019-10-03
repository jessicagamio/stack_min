class Stack():
    """ build a stack that will show you the most current minum value in stack"""

    def __init__(self):
        self._stack = []
        self.min = []

    def push(self, item):
        """ append item to stack. 
        If items exist in min append item only if less than the last element in min.
        elif add min  """
        self._stack.append(item)

        if self.min == []:
            self.min.append(item)

        elif item <= self.min[-1]:
            self.min.append(item)

    def pop(self):
        popped_item = self._stack.pop()
        if self.min[-1] == popped_item:
            self.min.pop()

    def min(self):
        return self.min[-1]

    def peek(self)
        return self._stack[0]

    def isEmpty(self)
        if len(self._stack) == 0:
            return True
        else:
            return False