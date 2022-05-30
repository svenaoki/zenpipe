from sklearn.linear_model import RidgeClassifier
import pandas as pd
import mlflow
from zenml.steps import Output, step
from sklearn.base import ClassifierMixin
from zenml.integrations.constants import MLFLOW, SKLEARN
from zenml.integrations.mlflow.mlflow_step_decorator import enable_mlflow

@enable_mlflow
@step
def train(train_df_x: pd.DataFrame,
    train_df_y: pd.DataFrame
    ) -> ClassifierMixin:

    print('logging data')
    mlflow.sklearn.autolog()
    clf = RidgeClassifier()
    clf.fit(train_df_x, train_df_y)


    return clf
