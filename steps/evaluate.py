import pandas as pd
import numpy as np
from zenml.steps import Output, step
from sklearn.metrics import mean_squared_error
from sklearn.base import ClassifierMixin
from zenml.integrations.wandb.wandb_step_decorator import enable_wandb
import wandb


@enable_wandb
@step
def evaluate(model: ClassifierMixin, eval_df_x: pd.DataFrame, eval_df_y: pd.DataFrame) -> Output(mse=float, rmse=float):
    try:
        prediction = model.predict(eval_df_x)
        mse = mean_squared_error(eval_df_y, prediction)
        rmse = np.sqrt(mse)
        print(f'Validation MSE: {mse}, RMSE: {rmse}')
        wandb.log({"rmse": rmse})
        return mse, rmse
    except Exception as e:
        print('error', e)
