'''calculate addition and multiplication of two matrices'''

import copy
def mult_matrix(matrix1, matrix2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(matrix1) != len(matrix2[0]):
        print("Error: Matrix shapes invalid for mult")
        return None
    mat1 = []
    for i_1 in range(len(matrix1)):
        mat2 = []
        for j_1 in range(len(matrix2[0])):
            mul = 0
            for k_1 in range(len(matrix2)):
                mul += matrix1[i_1][k_1] * matrix2[k_1][j_1]
            mat2.append(mul)
        mat1.append(mat2)
    return mat1

def add_matrix(matrix1, matrix2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(matrix1) != len(matrix2):
        print("Error: Matrix shapes invalid for addition")
        return None
    matrix = copy.deepcopy(matrix1)
    # for i in range(len(matrix1)):
    #     for j in range(len(matrix1[0])):
    #         matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    matrix = [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
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
    ''' main function '''
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
