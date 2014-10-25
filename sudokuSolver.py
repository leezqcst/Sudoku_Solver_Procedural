# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 21:57:21 2014

@author: Ricardo Guerrero Gómez-Olmedo
"""

import numpy as np
import sys
import sudokuLib as sdk


#Always parsing the user input
#---------------------#

if len(sys.argv) != 3:
    print('Invalid input. Usage: python sudoku_solver.py CSV_INPUT_PATH CSV_OUTPUT_PATH')
    sdk.pause()
    sys.exit(1)

csv_input_path = sys.argv[1]
csv_output_path = sys.argv[2] 


try:
    matrix = np.loadtxt(csv_input_path, delimiter=',').astype('int');
    
except IOError as e:
    print('There was an I/O error trying to read in path: ' + csv_input_path + \
    '.\nThe system returns: ' + e.strerror + '\nPlease check the path is correct\n')
    sdk.pause()
    sys.exit(1)
    
except:
    print('There was an error trying to convert the file into an integer matrix.'\
    + '\nPlease check if there is any empty space between commas or any '\
    ' non-proper symbol.')
    sdk.pause()
    sys.exit(1)

if matrix.shape != (9,9) or\
    matrix.min() < 0 or \
    matrix.max() > 9:
        
    print('Sorry, this sudoku solver only works with the standard sudoku version' \
    + ' of a 9x9 grid with values between 1 and 9, using 0 as a blank box')
    sdk.pause()
    sys.exit(1)

#---------------------#


print('\nThis is the given sudoku:\n\n')
sdk.sudokuPrinter(matrix)

print('Please, wait while solving ...\n')
solution = sdk.sudokuSolver(matrix)
    
print('Solving process already done')
sdk.pause()

print('This is the solved sudoku:\n\n')
sdk.sudokuPrinter(solution)
sdk.pause()

print('Saving in ' + csv_output_path + ' ...\n')



try:
    np.savetxt(csv_output_path, solution, fmt='%d', delimiter=',')
except IOError as e:
    print('There was an IO error trying to write in path: ' + csv_output_path + \
    '\nThe system returns: ' + e.strerror)
    sdk.pause()
    sys.exit(1)
    
    
print('Complete')
