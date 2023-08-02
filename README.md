# tsp-basic-solver

巡回セールスマン問題（TSP）を解くためのPythonプログラム．
イジングマシンを利用してTSPの近似解を求めることができます．
[Fixstars Amplify](https://amplify.fixstars.com/ja/)を使用して，イジングマシンの計算を行います．
問題インスタンスは[TSPLIB](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/)を使用します．


## Requirement
- Package manager: [PDM](https://github.com/pdm-project/pdm)
- Ising machine: [AmplifyAE](https://amplify.fixstars.com/ja/)


## 環境構築
前提として以下のツールが必要になります．
- pdm ([reference](https://pdm.fming.dev/latest/#other-installation-methods))

1. virtualenvを使用しない場合，`__pypackages__`を作成．

```bash
mkdir __pypackages__
```

2. pythonのバージョンやパスをベースインタプリタとして指定．

```bash
pdm use
```

3. ライブラリをインストール．

```bash
pdm install
```


## Script

[TSPLIB](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/)のgzファイルを全解凍．
```bash
bash scripts/untip_gz.sh
```

## Usage

att48のデータセットを解く．
```bash
pdm solve att48
```


## Author
Tatsuya Noguchi ([@tatsuya-1412](https://github.com/tatsuya-1412))