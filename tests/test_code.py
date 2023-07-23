from amplify import BinarySymbolGenerator, Solver
from amplify.client import FixstarsClient
from amplify.constraint import one_hot

gen = BinarySymbolGenerator()
q = gen.array(3)
f = 2 * q[0] * q[1] * q[2] - q[0] * q[1] + q[2] + 1
c = one_hot(q[0] + q[1])  # 制約: q[0] + q[1] == 1

client = FixstarsClient()
client.token = ""
client.parameters.timeout = 1000  # タイムアウト1秒

model = f + c
solver = Solver(client)
result = solver.solve(model)
print(type(result))
energy, values = result[0].energy, result[0].values
print(f'energy: {energy}')
print(f'values: {values}')