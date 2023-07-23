from amplify import BinaryPoly, Solver, SolverResult


class TspOptimize():
    model: BinaryPoly
    solver: Solver
    result: SolverResult

    def __init__(self, model: BinaryPoly, solver: Solver):
        self.model = model
        self.solver = solver

    def optimize(self):
        result = self.solver.solve(self.model)
        self.result = result

    def get_result(self):
        return self.result