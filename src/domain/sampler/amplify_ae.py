from amplify import Solver
from amplify.client import FixstarsClient


class AmplifyAe:
    client: FixstarsClient

    def __init__(self, token: str):
        self.client: FixstarsClient = FixstarsClient()
        self.client.token = token
        self.client.parameters.timeout = 5000


    def get_solver(self):
        return Solver(self.client)
