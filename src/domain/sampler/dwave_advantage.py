from amplify import Solver
from amplify.client.ocean import DWaveSamplerClient


class DwaveAdvantage:
    client: DWaveSamplerClient

    def __init__(self, token: str):
        self.client: DWaveSamplerClient = DWaveSamplerClient()
        self.client.token = token
        self.client.solver = "Advantage_system6.2"
        # self.client.parameters.num_reads = 100
        self.client.parameters.annealing_time = 2000


    def get_solver(self):
        return Solver(self.client)
