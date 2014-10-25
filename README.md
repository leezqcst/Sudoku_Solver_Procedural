Sudoku_Solver_Procedural
========================

This is the procedural version of a sudoku solver I developed for the Insight Data Engineering Fellows Program.

The solver algorithm is based on the recursive backtracking algorithm described in [1].

In **sudokus_for_testing** directory there are sudokus of different complexity levels for testing the application.

An example of use:

>~~~
>>>> python sudokuSolver.py E:/sudokus_for_testing/fiendish.csv E:/sudokus_for_testing/sudokuOUT.csv
>
>This is the given sudoku:
>
>
> 006|504|800 
> 017|900|020 
> 900|030|065 
> ---+---+---
> 800|060|092 
> 003|709|600 
> 620|010|003 
> ---+---+---
> 180|050|007 
> 060|003|240 
> 002|807|100 
>
>
>Please, wait while solving ...
>
>Solving process already done
>Presione una tecla para continuar . . . 
>
>
>
>This is the solved sudoku:
>
>
> 236|574|819 
> 517|986|324 
> 948|231|765 
> ---+---+---
> 871|365|492 
> 453|729|681 
> 629|418|573 
> ---+---+---
> 184|652|937 
> 765|193|248 
> 392|847|156 
>
>
>Presione una tecla para continuar . . . 
>
>
>
>Saving in E:/sudokus_for_testing/sudokuOUT.csv ...
>
>Complete
>>>> 
>~~~

[1] http://es.wikipedia.org/wiki/Sudoku_backtracking
