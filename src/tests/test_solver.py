import py_libsudoku


def test_solve():
    solvable_one_solution = py_libsudoku.Board(
    [0, 0, 6, 0, 0, 8, 5, 0, 0,
     0, 0, 0, 0, 7, 0, 6, 1, 3,
     0, 0, 0, 0, 0, 0, 0, 0, 9,
     0, 0, 0, 0, 9, 0, 0, 0, 1,
     0, 0, 1, 0, 0, 0, 8, 0, 0,
     4, 0, 0, 5, 3, 0, 0, 0, 0,
     1, 0, 7, 0, 5, 3, 0, 0, 0,
     0, 5, 0, 0, 6, 4, 0, 0, 0,
     3, 0, 0, 1, 0, 0, 0, 6, 0]
    )
    solution = py_libsudoku.Board()
    solver = py_libsudoku.Solver()
    result = solver.solve(solvable_one_solution, solution)
    if result == py_libsudoku.SolverResult.NO_ERROR:
      assert solution.isComplete
