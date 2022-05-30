from zenml.integrations.constants import MLFLOW, SKLEARN
#from zenml.integrations.mlflow.mlflow_step_decorator import enable_mlflow
from zenml.pipelines import pipeline

from steps.importer import importer
from steps.split import split
from steps.train import train
from steps.evaluate import evaluate
from pipelines.train_pipeline import train_pipeline

from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri


def training_pipeline_run():
    training_pipeline = train_pipeline(importer=importer(),
                                       split=split(),
                                       train=train(),
                                       evaluate=evaluate())

    training_pipeline.run()


if __name__ == "__main__":
    training_pipeline_run()

    print(
        "Now run \n "
        f"    mlflow ui --backend-store-uri {get_tracking_uri()}\n"
        "To inspect your experiment runs within the mlflow UI.\n")
