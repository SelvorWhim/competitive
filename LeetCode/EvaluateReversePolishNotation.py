# works like a stack, using Python list with appropriate operations as a stack

import operator

operator_map = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    # '/': operator.floordiv,  # doesn't round towards zero for negative results
    '/': lambda n1, n2: int(n1 / n2),
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []
        for token in tokens:
            if token in operator_map.keys():
                operand_2 = operand_stack.pop() # to preserve order
                operand_1 = operand_stack.pop()
                operation_result = operator_map[token](operand_1, operand_2)
                # print(f'{operand_1} {token} {operand_2} = {operation_result}')  # DBG
                operand_stack.append(operation_result)
            else:
                operand_stack.append(int(token))
        return operand_stack.pop()
