from zenml.pipelines import pipeline
from zenml.integrations.constants import MLFLOW, SKLEARN


@pipeline(enable_cache=False, required_integrations=[MLFLOW, SKLEARN])
def train_pipeline(importer, split, train, evaluate):
    """
    Args:
        importer: DataClass
        train: DataClass
        split: DataClass
    Returns:
        mse: float
        rmse: float
    """
    df = importer()
    x_train, x_test, y_train, y_test = split(df)
    model = train(x_train, y_train)
    mse, rmse = evaluate(model, x_test, y_test)
