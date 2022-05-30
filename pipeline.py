import argparse
from steps.importer import importer
from steps.split import split
from steps.train import train
from steps.evaluate import evaluate
from pipelines.train_pipeline import train_pipeline
from pipelines.data_analysis_pipeline import data_analysis_pipeline
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri
from steps.visualizer import visualize_statistics, visualize_train_test_statistics


def training_pipeline_run():
    training_pipeline = train_pipeline(importer=importer(),
                                       split=split(),
                                       train=train(),
                                       evaluate=evaluate())

    training_pipeline.run()


def analyze_pipeline_run():
    """Pipeline for analyzing data."""
    analyze = data_analysis_pipeline(
        importer=importer(),
        split=split(),
    )
    analyze.run()
    visualize_statistics()
    visualize_train_test_statistics()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pipeline", type=str, choices=[
                        "analyze", "train", "all"])
    args = parser.parse_args()

    if args.pipeline == 'train':
        training_pipeline_run()
    elif args.pipeline == 'analyze':
        analyze_pipeline_run()
    else:
        print('No options chosen... Running training and analyzer pipeline')
        training_pipeline_run()
        analyze_pipeline_run()
