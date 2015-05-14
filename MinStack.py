class MinStack(object):
    ''' Stack Class that keeps track of its minimum element
    and access it in O(1) time

    Method Names:

    __str__()
    __repr__()

    isEmpty()
    peek()
    pop()
    push(...)
    peekMin()
    popMin()
    '''

    def __init__(self):
        ''' Initialize magic method for the MinStack
        data structure
        '''
        self.stack = list()
        # The minimum element in the stack will always be
        # at the top of this stack
        self.min_stack = list()


    def __str__(self):
        name = "MinStack\n"
        top = "-----bottom---\n"
        elements = ""
        for elem in self.stack:
            elements += str(elem) + '\n'
        bottom = "----top----\n"

        return '{}{}{}{}'.format(name, top, elements, bottom)

    def __repr__(self):
        return __str__()

    def isEmpty(self):
        ''' Returns true if this instance of MinStack is empty
        false otherwise

        Operation takes O(1) time
        '''
        return len(self.stack) == 0

    def push(self, elem):
        ''' Adds element to stack of values

        Operation takes O(1) time
        '''

        # Check is new min is pushed
        if self.isEmpty() or elem <= self.peekMin():
            # Pushes new smalled value onto minStack
            self.min_stack.append(elem)

        self.stack.append(elem)

    def pop(self):
        ''' Pop first element off of value stack
        and returns that value

        Operation takes O(1) time
        '''
        if self.isEmpty():
            raise Exception("MinStack is empty. No element to pop")

        elem = self.stack.pop()
        min_elem = self.min_stack[len(self.min_stack) - 1]

        # Check is the value poped was the old minimum
        if elem == min_elem:
            self.min_stack.pop()

        return elem

    def peek(self):
        ''' Returns the element at the top of the stack
        without removing it

        Operation takes O(1) time
        '''
        if self.isEmpty():
            return None
        return self.stack[len(self.stack) - 1]

    def peekMin(self):
        ''' Returns the minimum element in the current stack

        Operation takes O(1) time
        '''
        if self.isEmpty():
            return None
        return self.min_stack[len(self.min_stack) - 1]

    def popMin(self):
        ''' Removes the minimum value from the stack
        Maintains the current ordering of the stack
        Return the stacks minimum value

        Operation takes O(n) time
        '''
        pass
        if self.isEmpty():
            raise Exception("MinStack is empty. No element to pop")
        pass
        # min_elem = self.min_stack.pop()
        # curr_elem = None
        # buffer = list()
        # while curr_elem != min_elem:\
