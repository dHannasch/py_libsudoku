import py_libsudoku as lsdk
import time

asyncGenComplete = False
genBoard = lsdk.Board()

def onGenProgress(currentStep, totalSteps):
    print("    .... asyncGenerate at step {} of {}"
          .format(currentStep, totalSteps))

def onGenFinished(result, board):
    global genBoard
    genBoard = board
    global asyncGenComplete
    asyncGenComplete = True
    print()
    print(".... asyncGenerate finished: {}".format(result))

gen = lsdk.Generator()

print("Will generate board with Hard difficulty ...")

gen.asyncGenerate(lsdk.PuzzleDifficulty.HARD,
                  onGenProgress, onGenFinished)

while not asyncGenComplete:
    time.sleep(0.1)

print("Generated board: {}".format(genBoard))

print()
print()

print("Solving generated board ...")
solver = lsdk.Solver()
solution_board = lsdk.Board()
solvResult = solver.solve(genBoard, solution_board)
print(".... solver result: {}".format(solvResult))
if solvResult == lsdk.SolverResult.NO_ERROR:
      print("Solution found: {}".format(solution_board))
