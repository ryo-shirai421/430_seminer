# 4月30日 高校生プログラミング体験
## 環境構築
```
cd 430_semener
# 仮想環境作成
python -m venv .venv
# 仮想環境の有効化（bashの場合）
source .venv/Scripts/activate
# パッケージのインストール
pip install -r requirements.txt
```
## 準備
```
# ラズベリーパイにssh接続
ssh <ユーザ名>@raspberrypi.local
# 温度センサの接続確認
i2cdetect -y 1
# 実行
python test.py
```
## 実行

```
python src/display.py
```

## ファイル説明

### src/
- display.py
  - メインのファイル
  - 実行オンリーで体験者は基本的に編集しない（体験の内容によっては編集してもらってもよい）.
  - センサ値のヒートマップと席の状態、時間などが表示される.
- get_status.py
  - センサ値から座席の状態を判別するコード.
  - 出力
    - 席の状態（0 : 不在、　1 : 在席、　2 : 離席）
    - 席のステータスが変更した時の時間
  - 入力
    - 今の時間、前回ステータスが変更した時間
    - 今のステータス、センサ値
  - 体験者に判定するコードを書いてもらう（ある程度サンプルコードを与えておく）.
- sandbox.ipynb
  - 体験者が適当にコードを試す場所
- train_model.py
  - 機械学習モデルの訓練と保存を行う．
### data/
- 訓練用データを格納
### params/
- 学習済みのモデルを格納
### ans/
- 演習の解答例
## リンク
- [温度センサデータシート](https://omronfs.omron.com/ja_JP/ecb/products/pdf/d6t_new.pdf)
- [温度センサセットアップガイド](https://docs.google.com/document/d/1fm1A4y2_XXyt_r_MGgmAdpNswXAutFpxiaugDuM-L6w/edit?usp=sharing)
