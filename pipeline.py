import argparse
from steps.importer import importer
from steps.split import split
from steps.train import train
from steps.evaluate import evaluate
from pipelines.train_pipeline import train_pipeline
from pipelines.data_analysis_pipeline import data_analysis_pipeline
from steps.visualizer import visualize_statistics, visualize_train_test_statistics


def training_pipeline_run():
    train_pipeline(
        importer=importer(),
        split=split(),
        train=train(),
        evaluate=evaluate()).run()


def analyze_pipeline_run():
    """Pipeline for analyzing data."""
    data_analysis_pipeline(
        importer=importer(),
        split=split(),
    ).run()
    visualize_statistics()
    visualize_train_test_statistics()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pipeline", type=str, choices=[
                        "analyze", "train"])
    args = parser.parse_args()

    if args.pipeline == 'train':
        training_pipeline_run()
    elif args.pipeline == 'analyze':
        analyze_pipeline_run()
