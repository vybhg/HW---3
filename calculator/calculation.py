class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation  # It stores the selected operation

    def get_result(self):
        # It is used to call the operation
        return self.operation(self.a, self.b)