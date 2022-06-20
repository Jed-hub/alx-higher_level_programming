#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if not row:
            print("")
        for elt in row:
            if elt != row[-1]:
                print("{}".format(elt), end=" ")
            else:
                print("{}".format(elt))
