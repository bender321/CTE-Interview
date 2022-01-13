from typing import List
import ast


class MatrixCalculator:

    def __init__(self):
        self._result = []
        self._MA = []
        self._MB = []
        self._matrix_A_width = 0
        self._matrix_B_width = 0
        self._matrix_A_height = 0
        self._matrix_B_height = 0

    def main_hub(self) -> None:

        if self._size_of_matrices() == 1:
            self._insert_inputs(self._matrix_A_width, self._matrix_A_height, 'A')
            self._insert_inputs(self._matrix_B_width, self._matrix_B_height, 'B')
            self._multiply(self._MA, self._MB)
            self._print_result()

    def _size_of_matrices(self) -> int:

        print('Matrix A')

        try:
            self._matrix_A_width = int(input('width: '))
            self._matrix_A_height = int(input('height: '))
            print('Matrix B')
            self._matrix_B_width = int(input('width: '))
            self._matrix_B_height = int(input('height: '))

        except ValueError:
            print('Wrong parameter...(Insert please integer number like 1, 2, 3,...)')
            exit(-1)

        else:

            if (
                    self._matrix_A_width == 0 or
                    self._matrix_A_height == 0 or
                    self._matrix_B_width == 0 or
                    self._matrix_B_height == 0
            ):
                print('No relevant sense for 0 size matrix')
                exit(-2)

            elif self._matrix_A_width == self._matrix_B_height:
                return 1

            else:
                print('Size of matrices are not correct for multiplication...')
                exit(-3)

    def _insert_inputs(self, matrix_width: int, matrix_height: int, AorB: str) -> int:

        i = 0
        print('Matrix ' + AorB + ' values:')

        while i < int(matrix_height):
            self._check_inputs(matrix_width, AorB)
            i += 1

        return 1

    def _check_inputs(self, matrix_width: int, MAB: str) -> None:

        try:
            matrix_values = input('')
            matrix_values = list(ast.literal_eval((matrix_values.strip('[]')).replace(' ', ', ')))

        except ValueError:
            print('Make sure that in matrix all numbers are numbers!')
            print('Exiting program...')
            exit(-4)

        except TypeError:
            matrix_values = [int(matrix_values.strip('[]'))]

        except SyntaxError:
            print('Make sure that you give matrix row in form of [num num ...]')
            exit(-5)

        if len(matrix_values) > matrix_width:
            print('Number of values in matrix is different from its width...')
            print('Exiting program...')
            exit(-6)

        elif MAB == 'A':
            self._MA.append(matrix_values)

        elif MAB == 'B':
            self._MB.append(matrix_values)

    def _multiply(self, A: List, B: List) -> None:

        try:

            for m in range(0, len(A)):
                rows = []

                for i in range(0, len(B[0])):
                    columns = 0

                    for j in range(0, len(B)):
                        columns += A[m][j] * B[j][i]
                    rows.append(columns)
                self._result.append(rows)

        except Exception as e:
            print(e)
            exit(-7)

    def _print_result(self) -> None:

        for i in self._result:

            for j in i:
                print(j)


if __name__ == "__main__":
    calculator = MatrixCalculator()
    calculator.main_hub()



