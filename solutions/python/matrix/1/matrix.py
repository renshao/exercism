class Matrix:
    def __init__(self, matrix_string):
        lines = matrix_string.split('\n')
        self.matrix = list(map(lambda line: (
            list(map(int, line.split(' ')))
        ), lines))
        
    def row(self, index):
        index = index - 1
        return self.matrix[index]

    def column(self, index):
        index = index - 1
        result = []
        for i in range(len(self.matrix)):
            result.append(self.matrix[i][index])
        return result
