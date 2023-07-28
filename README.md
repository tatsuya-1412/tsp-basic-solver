# tsp-basic-solver

TSPLIBの巡回セールスマン問題をイジングマシンで解くプログラム．

## Requirement

- Package manager: [PDM](https://github.com/pdm-project/pdm)
- Ising machine: [AmplifyAE](https://amplify.fixstars.com/ja/)

## Script

[TSPLIB](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/)のgzファイルを全解凍．
```sh
bash scripts/untip_gz.sh
```

## Usage

att48のデータセットを解く．
```sh
pdm run python3 src/main.py att48
```


## Author
Tatsuya Noguchi ([@tatsuya-1412](https://github.com/tatsuya-1412))