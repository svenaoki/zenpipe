import pandas as pd
from zenml.steps import Output, step


@step
def importer() -> Output(df=pd.DataFrame):
    df = pd.read_csv(
        'https://raw.githubusercontent.com/liquidcarrot/data.pima-indians-diabetes/master/src/raw.csv', sep=',')
    return df
