# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 21:24:36 2014

@author: Ricardo Guerrero Gómez-Olmedo
"""


import os
import numpy as np
from matplotlib.mlab import find
from sys import platform


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
    equiv = {0: [0,1,2], 1: [3,4,5], 2: [6,7,8]}
    c = [key for key in equiv if a in equiv[key]][0]
    d = [key for key in equiv if b in equiv[key]][0]
    
    return squares[c,d]
    
    
solution = None

def sudokuSolver(matrix):
    ''' 
    This sudoku solver algorithm is based on the recursive backtracking 
    algorithm described in [1].

    [1] http://es.wikipedia.org/wiki/Sudoku_backtracking
    
    Parameters
    ----------
    matrix: array_like
        It contains the sudoku matrix.
    '''
    
    matbool = matrix != 0
    #solution = matrix.copy()
    global solution
    solution = np.empty(shape=(9,9))
    lock = False
    
    solverRec(0,0, matrix, matbool, lock)
    
    return solution



def solverRec(i,j, matrix, matbool, lock): 
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
    
    global solution
    
    if matbool[i,j] == False:
        
        for k in range(1,10):
            
            matrix[i,j] = k
            
            #checking if value is plausible in row, col and square
            if len(find(matrix[i,:] == k)) == 1 and \
               len(find(matrix[:,j] == k)) == 1 and \
               len(find(mySquare(matrix,i,j) == k)) == 1:              
               
               if i == 8 and j == 8:
                   solution = matrix.copy()
               elif i < 8 and j == 8:
                   solverRec(i+1, 0, matrix, matbool, lock)
               else:
                   solverRec(i, j+1, matrix, matbool, lock)
                
            matrix[i,j] = 0       
    else:
        
        if i == 8 and j == 8:
            solution = matrix.copy()
        elif i < 8 and j == 8:
            solverRec(i+1, 0, matrix, matbool, lock)
        else:
            solverRec(i, j+1, matrix, matbool, lock)    
       
       
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
    
    if len( np.hstack((find(matrix <1), find(matrix > 9))) ) != 0:
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


def pause():
    '''
    This function pause the execution until the user press any key to continue
    \n(in Windows) or press Enter (in Linux)
    '''
    
    if platform == 'win32':
        os.system('pause')
    elif platform == 'linux' or platform == 'linux2':
        print('Press Enter to continue ...'),
        try:
            raw_input()
        except:
            pass
      
    print('\n')
  
      