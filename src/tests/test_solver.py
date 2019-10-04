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
    assert result == py_libsudoku.SolverResult.NO_ERROR
    if result == py_libsudoku.SolverResult.NO_ERROR:
      assert solution.isComplete
      assert solution.isValid
    workingBoard = py_libsudoku.Board(solution)
    vector = py_libsudoku.VectorOfBoards()
    result = solver.solve(solvable_one_solution, range(1, 10), workingBoard, 2, vector)
    assert result == py_libsudoku.SolverResult.HAS_NO_SOLUTION # no *more* solutions
    assert len(vector) == 1
    for board in vector:
      assert board.isComplete
      assert board.isValid
      # Sanity check that the solution in the vector is the same solution we normally produce.
      assert board == solution
      assert solution != workingBoard # the working board ended up in an unsolveable state


def test_multiple_solutions():
    solvable_multiple_solutions = py_libsudoku.Board(
    [0, 0, 0, 0, 0, 8, 5, 0, 0,
     0, 0, 0, 0, 7, 0, 6, 1, 3,
     0, 0, 0, 0, 0, 0, 0, 0, 9,
     0, 0, 0, 0, 9, 0, 0, 0, 1,
     0, 0, 1, 0, 0, 0, 8, 0, 0,
     4, 0, 0, 5, 3, 0, 0, 0, 0,
     1, 0, 7, 0, 5, 3, 0, 0, 0,
     0, 5, 0, 0, 6, 4, 0, 0, 0,
     3, 0, 0, 1, 0, 0, 0, 6, 0]
    )
    vector = py_libsudoku.VectorOfBoards()
    result = py_libsudoku.Solver().solve(solvable_multiple_solutions, range(1, 10), py_libsudoku.Board(), 8, vector)
    assert result == py_libsudoku.SolverResult.HAS_NO_SOLUTION # no *more* solutions
    assert len(vector) == 7
    for board in vector:
      assert board.isComplete
      assert board.isValid
    assert py_libsudoku.Solver().countSolutions(solvable_multiple_solutions, 8) == 7
