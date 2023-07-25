#!/bin/bash

# スクリプトのあるディレクトリを取得
script_directory=$(dirname "$(readlink -f "$0")")

# 解凍対象のディレクトリをlibディレクトリの上のディレクトリに設定
target_directory="$script_directory/../lib/ALL_tsp"

for gz_file in "$target_directory"/*.gz; do
  # gzファイルが存在しない場合は処理をスキップ
  [ -e "$gz_file" ] || continue

  # gzファイルを解凍
  echo "Extracting $gz_file..."
  gzip -d "$gz_file"
done

echo "Done."
