def shunting_yard(infix_str, operator_precedence=None):
    if operator_precedence is None:
        operator_precedence = {'+': 1, '*': 1}
    operator_stack = []
    out = ''
    for token in infix_str:
        if token == ' ':  # ignore spaces
            continue
        if token == '+' or token == '*':
            while operator_stack and operator_stack[-1] != '(' and \
                    operator_precedence[token] <= operator_precedence[operator_stack[-1]]:
                out += operator_stack.pop()
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack:
                popped = operator_stack.pop()
                if popped == '(':
                    break
                out += popped
        else:
            out += token

    while operator_stack:
        popped = operator_stack.pop()
        if popped == '(' or popped == ')':
            raise ValueError('Mismatched parenthesis in expression')
        out += popped

    return out


def evaluate_rpn(postfix_str):
    operands = []
    for token in postfix_str:
        if token == '+':
            left = operands.pop()
            right = operands.pop()
            operands.append(left + right)
        elif token == '*':
            left = operands.pop()
            right = operands.pop()
            operands.append(left * right)
        else:
            operands.append(int(token))
    return operands.pop()


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines() if line]

    # part 1
    print(sum(evaluate_rpn(shunting_yard(line)) for line in lines))

    # part 2
    operator_precedence = {'+': 2, '*': 1}
    print(sum(evaluate_rpn(shunting_yard(line, operator_precedence)) for line in lines))
