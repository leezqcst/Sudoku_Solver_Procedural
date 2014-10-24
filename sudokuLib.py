# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 21:24:36 2014

@author: Ricardo Guerrero Gómez-Olmedo
"""


import os
import numpy as np
from matplotlib.mlab import find


def sudokuPrinter(matrix):
    '''
    sudokuPrinter takes a sudoku contained in a numpy array and prints it 
    in a friendly way.
    
    Parameters
    ----------
    matrix: array_like
        It contains the sudoku matrix.
    '''
    
    rows, columns = matrix.shape
    
    line = ' ' + '+'.join(['-'*3]*3)

    
    for a in range(0,rows):
        if a and a%3 == 0:
            print line
            
        str_row = ''.join(str(val) for val in matrix[a,:])
        print ' ' + '|'.join(str_row[i:i+3] for i in range(0,len(str_row),3)),

        print '\n',
    
    print '\n'



def mySquare(matrix, a, b):
    '''
    This function returns the square to which the variable in coordinates 
    a,b belongs.
    
    Parameters
    ----------
    matrix: array_like
        It contains the sudoku matrix.
    a : int
        Current row.
    b : int
        Current column.
        
    Returns
    -------
    squares : array_like
        Returns a sub array from `squares` that contains the 3x3 square
        to which belongs the element located in `matrix`[`a`,`b`]
    '''    
    
    #Converting full grid to collection of 3x3 squares
    squares = np.swapaxes(matrix.reshape(3,3,3,-1),1,2)    
    
    #mapping indexes a,b in matrix to c,d in squares
    c = [x for x in range(1,4) if 3*x>a][0]-1
    d = [x for x in range(1,4) if 3*x>b][0]-1
    
    return squares[c,d]
    
    

def sudokuSolver(matrix):
    ''' 
    This sudoku solver is based on recursive backtracking algorithm 
    described in [1] using the better description available in the 
    spanish version [2].

    [1] http://en.wikipedia.org/wiki/Sudoku_solving_algorithms
    [2] http://es.wikipedia.org/wiki/Sudoku_backtracking
    
    Parameters
    ----------
    matrix: array_like
        It contains the sudoku matrix.
    '''

    matbool = matrix != 0
    solverRec(0,0, matrix, matbool)



def solverRec(i,j, matrix, matbool): 
    '''
    This is a helper recursive function used by sudokuSolver.
    
    Parameters
    ----------
    i : int
        Current row.
    j : int
        Current column.
    matrix: array_like
        It contains the sudoku matrix.
    matbool: array_like
        It reflects the initial state. True indicates initial values that
        must not be changed. False indicates that the value could be changed.
   '''
    
    if matbool[i,j] == False:
        
        for k in range(1,10):
              
            #checking if value is plausible in row, col and square
            if not k in matrix[i,:] and \
               not k in matrix[:,j] and \
               not k in mySquare(matrix,i,j):
               
               matrix[i,j] = k
               
               if i == 8 and j == 8:
                    return
               elif i < 8 and j == 8:
                    solverRec(i+1, 0, matrix, matbool)
               else:
                    solverRec(i, j+1, matrix, matbool)
                       
    else:
        
        if i == 8 and j == 8:
            return
        elif i < 8 and j == 8:
            solverRec(i+1, 0, matrix, matbool)
        else:
            solverRec(i, j+1, matrix, matbool)    
       
       
def sudokuChecker(matrix):
    '''
    sudokuChecker takes a 9x9 sudoku and return True if it is a valid sudoku,
    i.e. it meets all the rules.
    
    Parameters
    ----------   
    matrix: array_like
            `matrix` is a numpy.array that contains a 9x9 sudoku.
    
    Returns
    -------
    valid : bool
        If any of the numbers in `matrix` does not follow the 3 sudoku's rules, 
        `out` will be False. Otherwise will be True.
    '''
    
    valid = True
    
    if len(find(matrix == 0)) != 0:
        valid = False
        return valid
        
    for i in range(0,9):
        for j in range(0,9):
            
            k = matrix[i,j]
            
            if len(find(matrix[i,:] == k)) > 1 or \
               len(find(matrix[:,j] == k)) > 1 or \
               len(find(mySquare(matrix,i,j) == k)) > 1:
                   
                   valid = False
                   
        return valid

#TODO, buscar mecanismo alternativo al try/catch, que no acaba de funcionar
def pause():
    '''
    This function pause the execution until the user press any key to continue.
    '''
    
    try:
        os.system('pause')  #windows
    except:
        os.system('read -p "Press any key to continue"') #linux
      
    print('\n')
  
      