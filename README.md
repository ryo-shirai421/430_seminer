# 4月30日 高校生プログラミング体験
## 環境構築
### Pyenv & Poetry のインストール
- Python version: 3.10
- (参考) https://zenn.dev/kumamoto/articles/9f0b520020bdd0

### 作業環境の構築
```
# 作業ディレクトリに移動
cd 430_seminer
# パッケージのインストール
poetry install
# 仮想環境に移動
poetry shell
```
## 実行

```
python src/display.py
```

## ファイル説明

### src/display.py
- メインのファイル
- 実行オンリーで体験者は基本的に編集しない（体験の内容によっては編集してもらってもよい）.
- センサ値のヒートマップと席の状態、時間などが表示される
### src/get_status.py
- センサ値から座席の状態を判別するコード
- 出力
  - 席の状態（0 : 不在、　1 : 在席、　2 : 離席）
  - 席のステータスが変更した時の時間
- 入力
  - 今の時間、前回ステータスが変更した時間、
  - 今のステータス、センサ値
- 体験者に判定するコードを書いてもらう（ある程度サンプルコードを与えておく）.
