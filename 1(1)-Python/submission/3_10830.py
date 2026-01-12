from __future__ import annotations
import copy


"""
TODO:
- __setitem__ 구현하기
- __pow__ 구현하기 (__matmul__을 활용해봅시다)
- __repr__ 구현하기
"""


class Matrix:
    """
    행렬 연산을 지원하는 클래스입니다.
    모든 원소는 MOD(1000)로 나눈 나머지를 저장합니다.

    Attributes:
        - matrix (list[list[int]]): 행렬 데이터를 저장하는 2차원 리스트.
    """
    MOD = 1000

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    @staticmethod
    def full(n: int, shape: tuple[int, int]) -> Matrix:
        return Matrix([[n] * shape[1] for _ in range(shape[0])])

    @staticmethod
    def zeros(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(0, shape)

    @staticmethod
    def ones(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(1, shape)

    @staticmethod
    def eye(n: int) -> Matrix:
        matrix = Matrix.zeros((n, n))
        for i in range(n):
            matrix[i, i] = 1
        return matrix

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.matrix), len(self.matrix[0]))

    def clone(self) -> Matrix:
        return Matrix(copy.deepcopy(self.matrix))

    def __getitem__(self, key: tuple[int, int]) -> int:
        return self.matrix[key[0]][key[1]]

    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        # 구현하세요!
        i, j = key
        self.matrix[i][j] = value % Matrix.MOD

    def __matmul__(self, matrix: Matrix) -> Matrix:
        x, m = self.shape
        m1, y = matrix.shape
        assert m == m1

        result = self.zeros((x, y))

        for i in range(x):
            for j in range(y):
                for k in range(m):
                    result[i, j] += self[i, k] * matrix[k, j]

        return result

    def __pow__(self, n: int) -> Matrix:
        # 구현하세요!
        """
        분할 정복을 이용한 행렬의 거듭제곱(** 연산)을 수행합니다.

        Args:
            - n (int): 지수 (0 이상의 정수).

        Returns:
            - result (Matrix): 거듭제곱 결과가 담긴 Matrix 객체.
        """
        # A^0 = I
        if n == 0:
            return self.eye(self.shape[0])

        # A^1 = A
        if n == 1:
            res = self.zeros(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    res[i, j] = self.matrix[i][j]
            return res

        # 분할 정복
        half = self.__pow__(n // 2)
        squared = half @ half

        if n % 2 == 0:
            return squared  # 짝수: A^n = half^2
        else:
            return squared @ self  # 홀수: A^n = half^2 * A


    def __repr__(self) -> str:
        # 구현하세요!
        """
        행렬을 문자열 형태로 표현합니다.

        Returns:
            - representation (str): 공백으로 구분된 행렬 문자열.
        """
        lines = []
        for row in self.matrix:
            line = " ".join(str(x) for x in row)
            lines.append(line)
        return "\n".join(lines)


from typing import Callable
import sys


"""
-아무것도 수정하지 마세요!
"""


def main() -> None:
    intify: Callable[[str], list[int]] = lambda l: [*map(int, l.split())]

    lines: list[str] = sys.stdin.readlines()

    N, B = intify(lines[0])
    matrix: list[list[int]] = [*map(intify, lines[1:])]

    Matrix.MOD = 1000
    modmat = Matrix(matrix)

    print(modmat ** B)


if __name__ == "__main__":
    main()