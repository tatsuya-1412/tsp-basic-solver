import numpy as np
import pandas as pd
from amplify import BinarySymbolGenerator, Solver
from amplify.client import FixstarsClient
from amplify.constraint import one_hot

# locations = np.random.uniform(size=(10, 2))
# print(locations)

# # 距離行列
# all_diffs = np.expand_dims(locations, axis=1) - np.expand_dims(locations, axis=0)
# print(np.expand_dims(locations, axis=1))
# print(np.expand_dims(locations, axis=0))
# print(all_diffs)
# distances = np.sqrt(np.sum(all_diffs**2, axis=-1))
# print(distances)

with open("../lib/att48.tsp", "r") as f:
	lines = f.read().splitlines()
print(lines[3].split(' : ')[1])
data = pd.read_csv('../lib/att48.tsp', header=5)
df = data['NODE_COORD_SECTION'].str.split(' ', expand=True)
df = df.drop(df.columns[0], axis=1).drop(df.index[-1])
points = df.astype(int).to_numpy()
all_diffs = np.expand_dims(points, axis=1) - np.expand_dims(points, axis=0)
distances = np.sqrt(np.sum(all_diffs**2, axis=-1))
print(distances.shape)


# gen = BinarySymbolGenerator()
# q = gen.array(3)
# f = 2 * q[0] * q[1] * q[2] - q[0] * q[1] + q[2] + 1
# c = one_hot(q[0] + q[1])  # 制約: q[0] + q[1] == 1

# client = FixstarsClient()
# client.token = ""
# client.parameters.timeout = 1000  # タイムアウト1秒

# model = f + c
# solver = Solver(client)
# result = solver.solve(model)
# print(type(result))
# energy, values = result[0].energy, result[0].values
# print(f'energy: {energy}')
# print(f'values: {values}')