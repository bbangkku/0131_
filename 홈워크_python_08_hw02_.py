
class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]
    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()
    def push(self, x):
        self.stack.append(x)
    def __repr__(self):
        return self.stack

# p3 = Point(1, 3)
# p4 = Point(3, 1)
# r1 = Rectangle(p3, p4)
# print(r1.get_area())
# print(r1.get_perimeter())
# print(r1.is_square())

a = Stack()
print(a.push(5))
print(a.push(1))
print(a.top())
print(a.__repr__())
print(a.empty())