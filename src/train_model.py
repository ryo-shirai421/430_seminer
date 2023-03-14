import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier


def main():
    parent = Path(__file__).resolve().parents[1]
    # 訓練データの読み込み
    X = pd.read_csv(parent.joinpath('data/train_data.csv'), header=None).values
    # 正解ラベルの読み込み
    y = np.ravel(pd.read_csv(parent.joinpath('data/train_label.csv'), header=None).values)
    # モデルの読み込み
    model = KNeighborsClassifier(n_neighbors=2)
    # モデルの学習
    model.fit(X, y)
    # 学習済みのモデルを保存
    pickle.dump(model, open(parent.joinpath('params/knn_model.pkl'), "wb"))


if __name__ == "__main__":
    main()
