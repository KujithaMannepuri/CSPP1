'''calculate addition and multiplication of two matrices'''

import copy
def mult_matrix(m_1, m_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m_1) != len(m_2[0]):
        print("Error: Matrix shapes invalid for mult")
        return None
    mat1 = []
    len_m1 = len(m_1)
    len_m2 = len(m_2[0])
    len_m3 = len(m_2)
    for i_1 in range(len_m1):
        mat2 = []
        for j_1 in range(len_m2):
            mul = 0
            for k_1 in range(len_m3):
                mul += m_1[i_1][k_1] * m_2[k_1][j_1]
            mat2.append(mul)
        mat1.append(mat2)
    return mat1

def add_matrix(m_1, m_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m_1) != len(m_2):
        print("Error: Matrix shapes invalid for addition")
        return None
    matrix = copy.deepcopy(m_1)
    # for i in range(len(matrix1)):
    #     for j in range(len(matrix1[0])):
    #         matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    matrix = [[m_1[i][j] + m_2[i][j]  for j in range(len(m_1[0]))] for i in range(len(m_1))]
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
    if matrix1 is None or matrix2 is None:
        print("Error: Invalid input for the matrix")
    else:
        matrixadd = add_matrix(matrix1, matrix2)
        print(matrixadd)
        matrixmul = mult_matrix(matrix1, matrix2)
        print(matrixmul)

if __name__ == '__main__':
    main()
