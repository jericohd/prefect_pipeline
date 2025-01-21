from prefect import flow  # Import the flow decorator
from scripts.preprocess import preprocess_data
from scripts.train import train_model
from scripts.evaluate import evaluate_model
import os

# Define directories
DATA_DIR = './data'
PROCESSED_DIR = os.path.join(DATA_DIR, 'processed')
MODEL_DIR = './models'
METRICS_DIR = './metrics'

@flow
def ml_pipeline():
    """
    Main ML pipeline flow that orchestrates preprocessing, training, and evaluation tasks.
    """
    # Preprocessing step
    processed_files = preprocess_data(
        input_path=os.path.join(DATA_DIR, 'delivery_data.csv'),
        output_path=PROCESSED_DIR
    )

    # Training step
    model_file = train_model(
        input_path=PROCESSED_DIR,
        model_path=MODEL_DIR
    )

    # Evaluation step
    metrics = evaluate_model(
        input_path=PROCESSED_DIR,
        model_path=MODEL_DIR,
        metrics_path=METRICS_DIR
    )

    print(f"Pipeline completed successfully! Metrics: {metrics}")

if __name__ == '__main__':
    ml_pipeline()
