from sklearn.linear_model import RidgeClassifier
import pandas as pd
import mlflow
from zenml.steps import Output, step
from sklearn.base import ClassifierMixin
from zenml.integrations.constants import MLFLOW, SKLEARN
from zenml.integrations.mlflow.mlflow_step_decorator import enable_mlflow


@enable_mlflow
@step
def train(X_train: pd.DataFrame,
          y_train: pd.DataFrame
          ) -> ClassifierMixin:

    print('logging data')
    mlflow.sklearn.autolog()
    clf = RidgeClassifier()
    clf.fit(X_train, y_train)

    return clf
