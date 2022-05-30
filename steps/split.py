from sklearn.model_selection import train_test_split
import pandas as pd
from zenml.steps import Output, step


@step
def split(df: pd.DataFrame) -> Output(
        X_train=pd.DataFrame,
        X_test=pd.DataFrame,
        y_train=pd.DataFrame,
        y_test=pd.DataFrame):

    X = df.drop('diabetic', axis=1)
    y = df[['diabetic']]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test
