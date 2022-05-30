from zenml.integrations.constants import FACETS, SKLEARN
from zenml.pipelines import pipeline


@pipeline(
    enable_cache=False,
    required_integrations=[FACETS, SKLEARN],
    requirements="requirements.txt"
)
def data_analysis_pipeline(importer, split):
    """Pipeline for analyzing data.
    Args:
        ingest_data  : Ingest data from the data source.
        data_splitter: Splits the data into train and test data.
    """
    df = importer()
    X_train, X_test, y_train, y_test = split(df)
