# 4月30日 高校生プログラミング体験
## 環境構築
### Poetryのインストール

```
#公式のインストーラーを使用してインストール
curl -sSL https://install.python-poetry.org | python3 -  
#pathを設定。$HOMEのところをは適宜書き換える。上記インストールのときの出力に実行コマンドが書かれている。例：Add `export PATH="/home/username/.local/bin:$PATH"` to your shell configuration file.
echo PATH="$HOME/.local/bin:$PATH" >> ~/.bashrc 
#poetryで作る仮想環境をプロジェクト直下に生成するようにする。その他の設定はpoetry config --listで見れる
poetry config virtualenvs.in-project true 
```
### 作業環境の構築
```
#作業ディレクトリに移動
cd 430_seminer
#パッケージのインストール
poetry install
#仮想環境に移動
poetry shell
```
