from collections import deque

class Expression:
    def __init__(self):
        self.left = None
        self.right = None
        self.operator = ''

    def value(self):
        if isinstance(self.left, Expression):
            val_left = self.left.value()
        else:
            val_left = self.left

        if isinstance(self.right, Expression):
            val_right = self.right.value()
        else:
            val_right = self.right

        if self.operator == '+':
            return val_left + val_right
        elif self.operator == '*':
            return val_left * val_right
        raise ValueError(f'Unknown operator "{self.operator}"')

    def __eq__(self, other):
        if not isinstance(other, Expression):
            return False
        if self.left != other.left:
            return False
        if self.right != other.right:
            return False
        if self.operator != other.operator:
            return False
        return True


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line for line in f.readlines()]

    print(sum(generate_expression(line).value() for line in lines))

