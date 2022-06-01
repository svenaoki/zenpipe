import pandas as pd
from zenml.steps import Output, step
import logging


class IngestData:
    def __init__(self):
        pass

    def import_data(self) -> pd.DataFrame:
        df = pd.read_csv(
            'https://raw.githubusercontent.com/liquidcarrot/data.pima-indians-diabetes/master/src/raw.csv', sep=',')
        return df


@step
def importer() -> Output(df=pd.DataFrame):
    try:
        ingest_data = IngestData()
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(e)
        raise e
