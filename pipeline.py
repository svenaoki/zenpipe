from zenml.integrations.constants import MLFLOW, SKLEARN
#from zenml.integrations.mlflow.mlflow_step_decorator import enable_mlflow
from zenml.pipelines import pipeline

from steps.importer import importer
from steps.split import split
from steps.train import train
from steps.evaluate import evaluate


from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri

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



if __name__ == "__main__":
    pipeline = train_pipeline(importer=importer(), split=split(), train=train(), evaluate=evaluate())
    pipeline.run()

    print(
    "Now run \n "
    f"    mlflow ui --backend-store-uri {get_tracking_uri()}\n"
    "To inspect your experiment runs within the mlflow UI.\n")