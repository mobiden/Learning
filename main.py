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

        if isinstance(other, int) or isinstance(other, float):
            askli = [line.copy() for line in self.li]
            num = other
            for z in askli:
                for i in range(len(z)):
                    z[i] = (z[i] * num)

        elif isinstance(other, Matrix):
            if len(self.li[0]) == len(other.li):
                askli = []
                for i in range(len(self.li)):
                    askli.append([])
                    for k in range(len(other.li[i])):
                        for j in range(len(self.li[i])):
                            if j == 0:
                                askli[i].append(0)
                            askli[i][k] += self.li[i][j] * other.li[j][k]
            else:
                raise MatrixError(Matrix(self.li), Matrix(other.li))

        return Matrix(askli)

    __rmul__ = __mul__

    def transpose(self):
        tempmat = []

        for i in range(len(self.li)):
            tempmat.append([])
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

exec(stdin.read())
