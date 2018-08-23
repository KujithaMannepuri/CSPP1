import copy
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m1) != len(m2[0]):
        print("Error: Matrix shapes invalid for mult")
        return None
    matrix = copy.deepcopy(m1)
    mat1 = []
    for i in range(len(m1)):
        mat2 = []
        for j in range(len(m2[0])):
            mul = 0
            for k in range(len(m2)):
                mul += m1[i][k] * m2[k][j]
            mat2.append(mul)
        mat1.append(mat2)
    return mat1

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m1) != len(m2):
        print("Error: Matrix shapes invalid for addition")
        return None
    matrix = copy.deepcopy(m1)
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            matrix[i][j] = m1[i][j] + m2[i][j]
    return matrix

def read_matrix(mat_size):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''

    matrix = []
    for index in range(mat_size[0]):
        mat = input()
        mat = list(map(int, mat.split(' ')))
        matrix.append(mat)
    if mat_size[0] != len(matrix):
        return None
    for index in matrix:
        if len(index) != mat_size[1]:
            return None
    return matrix

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    mat_size1 = input()
    mat_size1 = list(map(int, mat_size1.split(',')))
    matrix1 = read_matrix(mat_size1)
    mat_size2 = input()
    mat_size2 = list(map(int, mat_size2.split(',')))
    matrix2 = read_matrix(mat_size2)
    if matrix1 == None or matrix2 == None:
        print("Error: Invalid input for the matrix")
    else:
        matrixadd = add_matrix(matrix1, matrix2)
        print(matrixadd)
        matrixmul = mult_matrix(matrix1, matrix2)
        print(matrixmul)

if __name__ == '__main__':
    main()
