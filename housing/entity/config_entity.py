# Importing required packages
from collections import namedtuple


# Define data ingestion configuration
DataIngestionConfig = namedtuple(
    'DataIngestionConfig', 
    ['dataset_download_url', 'tgz_download_url', 'raw_data_dir', 'ingested_train_dir', 'ingested_test_dir']
)

# Define data validation configuration
DataValidationConfig = namedtuple(
    'DataValidationConfig',
    ['schema_file_path']
)

# Define data transformation configuration
DataTransformationConfig = namedtuple(
    'DataTransformationConfig',
    ['add_bedroom_per_room', 'transformed_train_dir', 'transformed_test_dir', 'preprocessed_object_file_path']
)

# Define model trainer configuration
ModelTrainerConfig = namedtuple(
    'ModelTrainerConfig',
    ['trained_model_file_path', 'base_accuracy']
)

# Define model evaluation configuration
ModelEvaluationConfig = namedtuple(
    'ModelEvaluationConfig',
    ['model_evaluation_file_path', 'timestamp']
)