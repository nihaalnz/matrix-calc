import numpy as np
import math

add = sub = mul = z = 0

while True:
    print()
    print('Choose option for operations on matrix:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Determinant')
    print('5. Inverse')
    print('6. Adjoint')
    print('7. Exit')
    print()

    choice = int(input('Enter your choice: '))
    print()

    if choice == 7:
        print('Successfully Terminated')
        break

    elif choice < 7:

        if choice == 1:
            r = int(input('Enter the number of rows of 1st matrix: '))
            c = int(input('Enter the number of columns of 1st matrix: '))
            a = np.zeros((r, c), dtype=int)

            for i in range(len(a)):
                for j in range(len(a[i])):
                    x = int(
                        input('Enter the element of 1st matrix and press enter: '))
                    a[i][j] = x

            r1 = int(input('Enter the number of rows of 2nd matrix : '))
            c1 = int(input('Enter the number of columns of 2nd matrix : '))
            b = np.zeros((r1, c1), dtype=int)

            for i in range(len(b)):
                for j in range(len(b[i])):
                    x = int(
                        input('Enter the element of 2nd matrix and press enter: '))
                    b[i][j] = x

            add = np.add(a, b)
            print()
            print('The sum of these two matrices are: ')
            print(add)

        elif choice == 2:
            r = int(input('Enter the number of rows of 1st matrix: '))
            c = int(input('Enter the number of columns of 1st matrix: '))
            a = np.zeros((r, c), dtype=int)

            for i in range(len(a)):
                for j in range(len(a[i])):
                    x = int(
                        input('Enter the element of 1st matrix and press enter: '))
                    a[i][j] = x

            r1 = int(input('Enter the number of rows of 2nd matrix : '))
            c1 = int(input('Enter the number of columns of 2nd matrix : '))
            b = np.zeros((r1, c1), dtype=int)

            for i in range(len(b)):
                for j in range(len(b[i])):
                    x = int(
                        input('Enter the element of 2nd matrix and press enter: '))
                    b[i][j] = x

            sub = np.subtract(a, b)
            print()
            print('The Difference of these two matrices are: ')
            print(sub)

        elif choice == 3:
            r = int(input('Enter the number of rows of 1st matrix: '))
            c = int(input('Enter the number of columns of 1st matrix: '))
            a = np.zeros((r, c), dtype=int)

            for i in range(len(a)):
                for j in range(len(a[i])):
                    x = int(
                        input('Enter the element of 1st matrix and press enter: '))
                    a[i][j] = x

            r1 = int(input('Enter the number of rows of 2nd matrix : '))
            c1 = int(input('Enter the number of columns of 2nd matrix : '))
            b = np.zeros((r1, c1), dtype=int)

            for i in range(len(b)):
                for j in range(len(b[i])):
                    x = int(
                        input('Enter the element of 2nd matrix and press enter: '))
                    b[i][j] = x
            if c != r1:
                print()
                print('Sorry, matrix multiplication is not defined for these matrices.')
            else:
                mul = np.matmul(a, b)
                print()
                print('The product of these two matrices are: ')
                print(mul)

        elif choice == 4:
            r = int(input('Enter the number of rows of matrix: '))
            c = int(input('Enter the number of columns of matrix: '))
            if r != c:
                print('It must be a square matrix')
            else:
                a = np.zeros((r, c), dtype=int)

                for i in range(len(a)):
                    for j in range(len(a[i])):
                        x = int(
                            input('Enter the element of matrix and press enter: '))
                        a[i][j] = x
                z = np.linalg.det(a)
                print()
                if z > 0:
                    deter = round(z)
                    print(f'The Determinant of the given matrix is {deter}')
                elif z < 0:
                    deter = round(z)
                    print(f'The Determinant of the given matrix is {deter}')
                elif z == 0:
                    print(f'The Determinant of the given matrix is {0}')

        elif choice == 5:
            r = int(input('Enter the number of rows of matrix: '))
            c = int(input('Enter the number of columns of matrix: '))
            if r != c:
                print('It must be a square matrix')
            else:
                a = np.zeros((r, c), dtype=int)

                for i in range(len(a)):
                    for j in range(len(a[i])):
                        x = int(
                            input('Enter the element of matrix and press enter: '))
                        a[i][j] = x
                inv = np.linalg.inv(a)
                print()
                print('The inverse of this matrix is: ')
                print(inv)

        elif choice == 6:
            r = int(input('Enter the number of rows of matrix: '))
            c = int(input('Enter the number of columns of matrix: '))
            if r != c:
                print('It must be a square matrix')
            else:
                a = np.zeros((r, c), dtype=int)

                for i in range(len(a)):
                    for j in range(len(a[i])):
                        x = int(
                            input('Enter the element of matrix and press enter: '))
                        a[i][j] = x
                det = np.linalg.det(a)
                det = round(det)
                if det == 0:
                    print()
                    print('Sorry, adjoint does not exist for this matrix')
                else:
                    inv = np.linalg.inv(a) * np.linalg.det(a)
                    print()
                    print('The adjoint of this matrix is: ')
                    print(inv)

        else:
            print('Sorry, invalid choice')
