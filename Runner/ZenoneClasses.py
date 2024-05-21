class Zenone:
    @staticmethod
    def state(state):
        print(state)

    @staticmethod
    def recur(text, iterations):
        print((text + "\n") * iterations)


    @staticmethod
    def var_recur(var_recur_callback, iterations):
        print((var_recur_callback + "\n") * iterations)

    textVar = {}

    @staticmethod
    def text_variable(define, value):
        Zenone.textVar[define] = value

    @staticmethod
    def add(*numbers):
        return sum(numbers)

    @staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def sub(*args):
        return args[0] - sum(args[1:])

    @staticmethod
    def divide(*args):
        result = args[0]
        for num in args[1:]:
            result /= num
        print(result)
