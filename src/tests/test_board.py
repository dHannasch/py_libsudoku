import py_libsudoku


def test_clear_board():
    clear_board = py_libsudoku.Board()
    assert clear_board.isEmpty
    assert clear_board.isValid
    assert not clear_board.isComplete

def test_one_to_nine():
    one_to_nine = py_libsudoku.Board([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert not one_to_nine.isEmpty
    assert one_to_nine.isValid
    assert not one_to_nine.isComplete

    one_to_nine_cpy = py_libsudoku.Board(one_to_nine)
    assert one_to_nine_cpy == one_to_nine

    assert one_to_nine_cpy.valueAt(line=1, column=0) == 0
    result = one_to_nine_cpy.setValueAt(1, 0, 1)
    assert result == py_libsudoku.SetValueResult.VALUE_INVALIDATES_BOARD
    assert one_to_nine_cpy.valueAt(line=1, column=0) == 0

    one_to_nine_cpy.clear()
    assert one_to_nine_cpy != one_to_nine
