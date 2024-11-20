import os

# Define the directory structure
directory_structure = {
    "data": ["raw", "processed"],  # Remove trailing slashes
    "docs": ["architecture-diagram.png", "README.md"],
    "src": {
        "data_ingestion": ["kafka_producer.py", "kafka_consumer.py"],
        "processing": ["data_cleaner.py", "feature_engineer.py"],
        "storage": ["postgres_handler.py", "mongo_handler.py"],
        "monitoring": ["grafana_setup.py", "api_server.py"],
        "utils": ["config.py", "logger.py"]
    },
    "tests": ["test_ingestion.py", "test_processing.py", "test_storage.py"],
    "root_files": [".gitignore", "docker-compose.yml", "Dockerfile", "LICENSE", "requirements.txt", "README.md"]
}

# Base directory
base_dir = "streamline-daq"

def create_project_structure(base, structure):
    for key, value in structure.items():
        path = os.path.join(base, key)
        if isinstance(value, list):  # Files and directories
            os.makedirs(path, exist_ok=True)
            for file in value:
                file_path = os.path.join(path, file)
                if "." in file:  # Check if it's a file (contains a dot)
                    with open(file_path, 'w') as f:
                        f.write("")  # Create an empty file
                else:  # Treat as a subdirectory
                    os.makedirs(file_path, exist_ok=True)
        elif isinstance(value, dict):  # Subdirectories
            os.makedirs(path, exist_ok=True)
           
