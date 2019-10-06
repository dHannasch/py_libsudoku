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


def test_buffer_protocol():
    import numpy as np
    one_to_nine = py_libsudoku.Board([1, 2, 3, 4, 5, 6, 7, 8, 9])
    arrayPointingToSameMemory = np.array(one_to_nine, copy=False)
    arrayPointingToSameMemory[1,0] = 4
    assert one_to_nine.valueAt(1,0) == 4
    one_to_nine.setValueAt(2, 1, 5)
    assert arrayPointingToSameMemory[2,1] == 5
    arrayPointingToSameMemory[:] = arrayPointingToSameMemory[np.random.permutation(9)]
    arrayPointingToSameMemory[:] = arrayPointingToSameMemory[:, np.random.permutation(9)]
    np.random.shuffle(arrayPointingToSameMemory)
    np.random.shuffle(arrayPointingToSameMemory.T)
    assert np.all(one_to_nine == arrayPointingToSameMemory)
    another_board = py_libsudoku.Board(arrayPointingToSameMemory)
    assert another_board == one_to_nine
    assert np.all(another_board == arrayPointingToSameMemory)
    # But this board does not share the same memory:
    result = another_board.setValueAt(3,3, another_board.valueAt(3,3) + 1)
    if result == py_libsudoku.SetValueResult.NO_ERROR:
        assert another_board.valueAt(3,3) == one_to_nine.valueAt(3,3) + 1
        assert another_board.valueAt(3,3) == arrayPointingToSameMemory[3,3] + 1
