
class Stack:
    """
    A Stack
    """

    def __init__(self):
        self.__stack = []

    def __len__(self):
        return len(self.__stack)

    @property
    def top(self):
        """
        top of Stack
        """

        if not self.__stack:
            return None

        return self.__stack[-1]

    @top.setter
    def top(self, top):
        """
        POP and then PUSH the stack
        """
        if not self.__stack:
            raise ValueError("Ca'nt assign to an emtpy stack")

        self.__stack[-1] = top

    def pop(self, n=1):
        """
        POP operation
        """
        if n < len(self.__stack):
            for _ in range(n):
                self.__stack = self.__stack[:-1]
        elif n == len(self.__stack):
            self.__stack = []
        else:
            raise ValueError('n > stack.size')

    def push(self, value=None):
        """
        PUSH operation
        """
        self.__stack.append(value)

    def empty(self):
        """
        EMPTY query
        """
        return bool(len(self.__stack))

    @property
    def size(self):
        """
        SIZE of Stack
        """
        return len(self.__stack)

    def clear(self):
        """
        clear the Stack
        """
        self.__stack = []
