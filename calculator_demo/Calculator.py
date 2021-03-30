class Calculator:
"""
simple calculator
"""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b

    @staticmethod
    def dont_like_this_number(b):
        if b in (13,17):
            #pass
            raise ValueError
        return b

