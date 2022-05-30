import pandas as pd
import numpy as np
import mlflow
from zenml.steps import Output, step
from sklearn.base import ClassifierMixin
from zenml.integrations.constants import MLFLOW, WANDB, SKLEARN
from zenml.integrations.mlflow.mlflow_step_decorator import enable_mlflow
from zenml.integrations.wandb.wandb_step_decorator import enable_wandb
import wandb
from sklearn.model_selection import RandomizedSearchCV
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier


@enable_wandb
@step
def train(X_train: pd.DataFrame,
          y_train: pd.DataFrame,
          X_test: pd.DataFrame,
          y_test: pd.DataFrame,
          ) -> ClassifierMixin:

    # mlflow.sklearn.autolog()
    random_grid = {
        'max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],
        'learning_rate': [0.01, 0.1, 0.01, 0.5]}

    clf = HistGradientBoostingClassifier()
    rsh = RandomizedSearchCV(
        estimator=clf, param_distributions=random_grid, random_state=42
    )
    rsh.fit(X_train, y_train.values.ravel())

    model = HistGradientBoostingClassifier(**rsh.best_params_)
    model.fit(X_train, y_train.values.ravel())

    # y_probas = model.predict_proba(X_test)
    # #importances = model.feature_importances_

    # wandb.sklearn.plot_class_proportions(
    #     y_train, y_test, labels=['diabetes', 'healthy'])
    # wandb.sklearn.plot_learning_curve(model, X_train, y_train)
    # wandb.sklearn.plot_roc(y_test, y_probas, labels=[
    #                        'diabetes', 'healthy'])
    # #wandb.sklearn.plot_feature_importances(model, X_train.columns)

    wandb.log(rsh.best_params_)
    wandb.log({"cv result": rsh.best_score_})
    return model
