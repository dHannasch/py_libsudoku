import py_libsudoku as lsk
import time

asyncSolveComplete = False

def onSolverProgress(progressPercentage, numSolutions):
    print(".... asyncSolveForGood at {:05.2f}%: {} solution(s) so far"
          .format(progressPercentage, numSolutions))

def onSolverFinished(result, solvedBoards):
    global asyncSolveComplete
    asyncSolveComplete = True
    print()
    print("asyncSolveForGood finished: {}".format(result))
    print("Found {} solution(s):".format(len(solvedBoards)))
    for b in solvedBoards:
        print()
        print("{}".format(b))

solvable_one_solution = lsk.Board(
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

solution = lsk.Board()

solver = lsk.Solver()

print("Board to be solved - 'solvable_one_solution': {}"
      .format(solvable_one_solution))

print("Looking for solution ...")

result = solver.solve(solvable_one_solution, solution)
if result == lsk.SolverResult.NO_ERROR:
    print("... solution found: {}".format(solution))
    print("Is solution ok? {}"
          .format(solution.isComplete))
else:
    print("... could not find solution :(")

print()
print("Doing an exhaustive search for all solutions ...")
print("   (there's just 1, but it will take long to find that out.)")
print("...")

solver.asyncSolveForGood(solvable_one_solution,
                         onSolverProgress,
                         onSolverFinished)

while not asyncSolveComplete:
    time.sleep(0.1)