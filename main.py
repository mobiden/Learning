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
            firstli = [line.copy() for line in self.li]
            if len(firstli[0]) == len(other.li):
                askli = []
                for i in range(len(firstli)):
                    askli.append([])
                    for k in range(len(other.li[i])):
                        for j in range(len(firstli[i])):
                            if j == 0:
                                askli[i].append(0)
                            askli[i][k] += firstli[i][j] * other.li[j][k]
            else:
                raise MatrixError(Matrix(firstli), Matrix(other.li))

        return Matrix(askli)

    __rmul__ = __mul__

    def transpose(self):
        tempmat = []
        sself = [line.copy() for line in self.li]
        for i in range(len(sself)):
            for j in range(len(sself[0])):
                if i == 0:
                    tempmat.append([])
                tempmat[j].append(sself[i][j])
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

    def solve(self, solves):
        sself = [line.copy() for line in self.li]
        if len(sself) == len(solves) and len(sself) == len(sself[0]):
            for i in range(len(sself)):
                sself[i].append(solves[i])
            for i in range(len(sself)):
                if sself[i][i] != 1:
                    tempx = sself[i][i]
                    for j in range(len(sself[0])):

                        sself[i][j] /= tempx

                for k in range(len(sself)):
                    if k == i:
                        continue
                    tempx2 = sself[k][i] / sself[i][i]
                    for l in range(len(sself[0])):
                        sself[k][l] -= sself[i][l] * tempx2

        else:
            raise MatrixError(self.li, solves)
        answ = []
        for i in range(len(sself)):
            answ.append(sself[i][-1])

        return answ


class SquareMatrix(Matrix):
    def __rpow__(currmatrix, power):
        if power == 1:
            return currmatrix
#        sself = Matrix([line.copy() for line in currmatrix.li])
#        fmat = Matrix([line.copy() for line in currmatrix.li])

        if power % 2 == 0:
            temp = SquareMatrix.__rpow__(currmatrix, power / 2)
            return temp * temp
        elif power % 2 == 1:
            temp = SquareMatrix.__rpow__(currmatrix, (power - 1) / 2)
            return currmatrix * temp * temp

    def __pow__(self, power):
        if isinstance(power, int):
            if power == 0:
                return self
            return SquareMatrix.__rpow__(self, power)
        else:
            raise MatrixError(self, self)


exec(stdin.read())
