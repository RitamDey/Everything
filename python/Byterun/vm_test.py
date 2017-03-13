from interpreter import Interpreter


def inter_test():
    obj = Interpreter()

    bytecode = {
        'instructions':[('PUSH_VALUE', 1),
                        ('PUSH_VALUE', 2),
                        ('ADD_TWO_NUMBERS', None),
                        ('PUSH_VALUE', 3),
                        ('ADD_TWO_NUMBERS', None),
                        ('PRINT_ANSWER', None)
                    ],
        'values':[0, 1, 2, 7]
    }

    obj.run_it(bytecode)


if __name__ == '__main__':
    inter_test()
