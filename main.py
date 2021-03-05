from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, li=[]):
        self.li = [line.copy() for line in li]

    def __str__(self):
        return '\n'.join(['\t'.join([str(i)
                                     for i in j]) for j in self.li])

    def size(self):
        return len(self.li), len(self.li[0])

    def __add__(self, other):

        templi1 = [line.copy() for line in self.li]
        templi2 = [line.copy() for line in other.li]
        if len(templi1) == len(templi2):
            for i in range(len(templi1)):
                for j in range(len(templi1[i])):
                    templi1[i][j] += templi2[i][j]
        else:
            raise MatrixError(Matrix(self.li), Matrix(other.li))

        return Matrix(templi1)

    def __mul__(self, other):
        askli = [line.copy() for line in self.li]
        num = other
        for z in askli:
            for i in range(len(z)):
                z[i] = (z[i] * num)
        return Matrix(askli)

    __rmul__ = __mul__

    def transpose(self):
        tempmat = []
        for i in range(len(self.li[0])):
            tempmat.append([])

        for i in range(len(self.li)):
            for j in range(len(self.li[i])):
                tempmat[j].append(self.li[i][j])
        self.li = tempmat
        return Matrix(self.li)

    @staticmethod
    def transposed(matr):
        tempmat = []
        for i in range(len(matr.li[0])):
            tempmat.append([])

        for i in range(len(matr.li)):
            for j in range(len(matr.li[i])):
                tempmat[j].append(matr.li[i][j])

        return Matrix(tempmat)

# Task 4 check 1
mid = Matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
print(mid * m1)
print(mid * m2)
print(m2 * m1)
try:
    m = m1 * m2
    print("WA It should be error")
except MatrixError as e:
    print(e.matrix1)
    print(e.matrix2)