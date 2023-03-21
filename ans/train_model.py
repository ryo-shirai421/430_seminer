import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier


MODELS = {"tree": tree.DecisionTreeClassifier(), "knn": KNeighborsClassifier(n_neighbors=2)}


def train_model(model_name="knn"):
    parent_dir = Path(__file__).resolve().parents[1]
    # 訓練データの読み込み
    X = pd.read_csv(parent_dir.joinpath("data", "train_data.csv"), header=None).values
    # 正解ラベルの読み込み
    y = np.ravel(pd.read_csv(parent_dir.joinpath("data", "train_label.csv"), header=None).values)
    # モデルの読み込み
    model = MODELS[model_name]
    # モデルの学習
    model.fit(X, y)
    # 学習済みのモデルを保存
    pickle.dump(model, open(parent_dir.joinpath("models", "{}_model.pkl".format(model_name)), "wb"))


if __name__ == "__main__":
    train_model()
