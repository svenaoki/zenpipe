from sklearn.model_selection import train_test_split
import pandas as pd
from zenml.steps import Output, step

@step
def split(df: pd.DataFrame) -> Output(
    train_x=pd.DataFrame,
    train_y=pd.DataFrame,
    test_x=pd.DataFrame,
    test_y=pd.DataFrame):

    X = df.drop('diabetic', axis=1)
    y = df[['diabetic']]
    train_x, train_y, test_x, test_y = train_test_split(X, y, test_size=0.3, random_state=42)
    return train_x, train_y, test_x, test_y




    
