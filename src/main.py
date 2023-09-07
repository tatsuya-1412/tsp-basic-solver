import os
import sys

import numpy as np
import pandas as pd
from dotenv import load_dotenv

from domain.model.tsp import Tsp
from domain.plotter.result_plotter import ResultPlotter
from domain.sampler.amplify_ae import AmplifyAe
from domain.sampler.dwave_advantage import DwaveAdvantage
from usecase.tsp_optimize import TspOptimize

# 環境変数の読み込み
env_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(env_path)
AMPLIFYAE_TOKEN = os.environ.get("AMPLIFYAE_TOKEN")
DWAVEADVANTAGE_TOKEN = os.environ.get("DWAVEADVANTAGE_TOKEN")

args = sys.argv

# 座標データの読み込み，距離行列計算
datafile_path = os.path.join(os.path.dirname(__file__), '../lib/ALL_tsp/'+args[1]+'.tsp')
with open(datafile_path, "r") as f:
	lines = f.read().splitlines()
n_city = int(lines[3].split(': ')[1])
data = pd.read_csv(datafile_path, header=5)
df = data['NODE_COORD_SECTION'].str.split(' ', expand=True)
df = df.drop(df.columns[0], axis=1).drop(df.index[-1])
points = df.astype(int).to_numpy()
all_diffs = np.expand_dims(points, axis=1) - np.expand_dims(points, axis=0)
distances = np.sqrt(np.sum(all_diffs**2, axis=-1))

# 最適経路データの読み込み
optfile_path = os.path.join(os.path.dirname(__file__), '../lib/ALL_tsp/'+args[1]+'.opt.tour')
data = pd.read_csv(optfile_path, header=4)
df = data['TOUR_SECTION'].str.split(' ', expand=True)
df = df.drop(df.index[-2:])
opt_route = df.transpose().values.astype('int')[0] - 1

# QUBOモデルの作成
tsp = Tsp(n_city=n_city, d=distances)
tsp.create_model(alpha=np.amax(distances))
model = tsp.get_model()

# ソルバーの取得
ae = AmplifyAe(token=AMPLIFYAE_TOKEN)
solver_ae = ae.get_solver()
ad = DwaveAdvantage(token=DWAVEADVANTAGE_TOKEN)
solver_ad = ad.get_solver()

# ↓Amplify
# 最適化
opt_ae = TspOptimize(model=model, solver=solver_ae)
opt_ae.optimize()
result = opt_ae.get_result()
energy, values = result[0].energy, result[0].values
print(f'energy={energy}')
route = tsp.get_route(values=values)
print(route)

# 結果の表示
file_path = os.path.join(os.path.dirname(__file__), '../results/img_st70.pdf')
plotter = ResultPlotter(route=route, distances=distances, points=points)
plotter.show(is_saved=True, file_path=file_path)

# 最適解の表示
file_path = os.path.join(os.path.dirname(__file__), '../results/img_st70.opt.pdf')
plotter = ResultPlotter(route=opt_route, distances=distances, points=points)
plotter.show(is_saved=True, file_path=file_path)

# ↓D-Wave
# # 最適化
# opt_ad = TspOptimize(model=model, solver=solver_ad)
# opt_ad.optimize()
# result = opt_ad.get_result()
# energy, values = result[0].energy, result[0].values
# print(f'energy={energy}')
# route = tsp.get_route(values=values)

# file_path = os.path.join(os.path.dirname(__file__), '../results/img_ad.pdf')
# plotter = ResultPlotter(route=route, distances=distances, points=points)
# plotter.show(is_saved=True, file_path=file_path)