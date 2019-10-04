#include "board.h"
#include "generator.h"
#include "solver.h"

#include <cstdint>
#include <iostream>
#include <sstream>
#include <vector>

#include <pybind11/pybind11.h>
#include <pybind11/operators.h>
#include <pybind11/stl.h>
namespace py = pybind11;

// https://pybind11.readthedocs.io/en/stable/advanced/cast/stl.html#making-opaque-types
PYBIND11_MAKE_OPAQUE(std::vector<sudoku::Board>);

PYBIND11_MODULE(py_libsudoku, m) {
    m.doc() = "Python bindings for libsudoku";

    py::enum_<sudoku::SetValueResult>(m, "SetValueResult")
        .value("NO_ERROR", sudoku::SetValueResult::NO_ERROR)
        .value("INVALID_VALUE", sudoku::SetValueResult::INVALID_VALUE)
        .value("VALUE_INVALIDATES_BOARD", sudoku::SetValueResult::VALUE_INVALIDATES_BOARD);

    py::class_<sudoku::Board>(m, "Board")

        .def(py::init(), "Creates an empty board.")

        .def(py::init<const std::vector<std::uint8_t> &>(), 
             "Creates a board with the given values (up to 81 values between 0 and 9).")

        .def(py::init<const sudoku::Board &>(),
             "Creates a board that is a copy of a given board.")

        .def_property_readonly("isEmpty", &sudoku::Board::isEmpty,
             "True if all the positions in the board are 0.")

        .def_property_readonly("isValid", &sudoku::Board::isValid,
             "True if the board has no invalid values nor repetitions of values "
             "across lines, columns or sections.")

        .def_property_readonly("isComplete", &sudoku::Board::isComplete,
             "True if the board corresponds to a solved puzzle.")

        .def("valueAt", &sudoku::Board::valueAt,
             "The value at a given board position - (line, column) pair.",
             py::arg("line"), py::arg("column"))

        .def("setValueAt", &sudoku::Board::setValueAt, 
             "Sets the value at a given board position - (line, column) pair.",
             py::arg("line"), py::arg("column"), py::arg("value"))

        .def("clear", &sudoku::Board::clear,
             "Clears the board by assigning 0 to all its positions.")

        .def(py::self == py::self)

        .def("__repr__",
             [](const sudoku::Board &board) {
                 std::ostringstream ostr;
                 ostr << "<py_libsudoku.Board:\n";
                 ostr << board;
                 ostr << ">\n";
                 return ostr.str();
                });

    py::class_<sudoku::Generator>(m, "Generator")
        .def(py::init());


    py::enum_<sudoku::SolverResult>(m, "SolverResult")
        .value("NO_ERROR", sudoku::SolverResult::NO_ERROR)
        .value("INVALID_BOARD", sudoku::SolverResult::INVALID_BOARD)
        .value("EMPTY_BOARD", sudoku::SolverResult::EMPTY_BOARD)
        .value("ALREADY_SOLVED", sudoku::SolverResult::ALREADY_SOLVED)
        .value("HAS_NO_SOLUTION", sudoku::SolverResult::HAS_NO_SOLUTION)
        .value("INVALID_CANDIDATES_VECTOR", sudoku::SolverResult::INVALID_CANDIDATES_VECTOR)
        .value("ASYNC_SOLVED_CANCELLED", sudoku::SolverResult::ASYNC_SOLVING_CANCELLED)
        .value("ASYNC_SOLVING_SUBMITTED", sudoku::SolverResult::ASYNC_SOLVING_SUBMITTED)
        .value("ASYNC_SOLVING_BUSY", sudoku::SolverResult::ASYNC_SOLVING_BUSY);

    py::class_<std::vector<sudoku::Board>>(m, "VectorOfBoards")
        .def(py::init<>())
        .def("clear", &std::vector<sudoku::Board>::clear)
        .def("pop_back", &std::vector<sudoku::Board>::pop_back)
        .def("__len__", [](const std::vector<sudoku::Board> &v) { return v.size(); })
        .def("__iter__", [](std::vector<sudoku::Board> &v) {
           return py::make_iterator(v.begin(), v.end());
        }, py::keep_alive<0, 1>()); /* Keep vector alive while iterator is used */

    py::class_<sudoku::Solver>(m, "Solver")
        .def(py::init())
        .def("solve", 
             (sudoku::SolverResult (sudoku::Solver::*)(const sudoku::Board &, sudoku::Board &)) &sudoku::Solver::solve,
             "Solves a Sudoku puzzle using the default candidates vector.")
        .def("solve", 
             (sudoku::SolverResult (sudoku::Solver::*)(const sudoku::Board &, const std::vector<uint8_t> &, sudoku::Board &,
                                                       size_t, std::vector<sudoku::Board> &)) &sudoku::Solver::solve,
             "Solves a Sudoku puzzle using the given candidates vector.")
        .def("solve",
             (sudoku::SolverResult (sudoku::Solver::*)(const sudoku::Board &, const std::vector<uint8_t> &, sudoku::Board &)) &sudoku::Solver::solve,
             "Solves a Sudoku puzzle using the given candidates vector.");
}

