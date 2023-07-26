# tsp-basic-solver

TSPLIBの巡回セールスマン問題をイジングマシンで解くプログラム．

## Script
TSPLIBのgzファイルを全解凍．
```sh
bash scripts/untip_gz.sh
```

## Usage
att48のデータセットを解く．
```sh
pdm run python3 src/main.py att48
```