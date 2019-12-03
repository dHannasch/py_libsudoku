import py_libsudoku


def test_generate():
    generator = py_libsudoku.Generator()
    board = generator.fullSudokuBoard()
    assert board.isValid
    assert board.isComplete
