import os

import numpy as np
import pandas as pd
from dotenv import load_dotenv

from domain.model.tsp import Tsp
from domain.sampler.amplify_ae import AmplifyAe
from usecase.tsp_optimize import TspOptimize

# 環境変数の読み込み
env_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(env_path)
TOKEN = os.environ.get("AMPLIFYAE_TOKEN")

# 座標データの読み込み，距離行列計算
with open("../lib/att48.tsp", "r") as f:
	lines = f.read().splitlines()
n_city = int(lines[3].split(' : ')[1])
data = pd.read_csv('../lib/att48.tsp', header=5)
df = data['NODE_COORD_SECTION'].str.split(' ', expand=True)
df = df.drop(df.columns[0], axis=1).drop(df.index[-1])
points = df.astype(int).to_numpy()
all_diffs = np.expand_dims(points, axis=1) - np.expand_dims(points, axis=0)
distances = np.sqrt(np.sum(all_diffs**2, axis=-1))

# QUBOモデルの作成
tsp = Tsp(n_city=n_city, d=distances)
tsp.create_model(alpha=np.amax(distances))
model = tsp.get_model()

# ソルバーの取得
ae = AmplifyAe(token=TOKEN)
solver = ae.get_solver()

# 最適化
opt = TspOptimize(model=model, solver=solver)
opt.optimize()
result = opt.get_result()
energy, values = result[0].energy, result[0].values

print(energy)
# print(values)