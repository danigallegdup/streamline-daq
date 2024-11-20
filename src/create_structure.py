import os

# Define the directory structure
project_structure = {
    "data": ["raw/", "processed/"],
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

# Helper function to create files and directories
def create_structure(base_path, structure):
    for key, value in structure.items():
        path = os.path.join(base_path, key)
        if isinstance(value, list):  # If the value is a list, create files
            os.makedirs(path, exist_ok=True)
            for item in value:
                item_path = os.path.join(path, item)
                if "." in item:  # It's a file
                    with open(item_path, 'w') as f:
                        f.write("")  # Create an empty file
                else:  # It's a subdirectory
                    os.makedirs(item_path, exist_ok=True)
        elif isinstance(value, dict):  # If the value is a dict, create subdirectories recursively
            os.makedirs(path, exist_ok=True)
            create_structure(path, value)

# Base directory for the project
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Create root files
for root_file in project_structure["root_files"]:
    with open(os.path.join(base_dir, root_file), 'w') as f:
        f.write("")  # Create empty root file

# Create the remaining project structure
create_structure(base_dir, {k: v for k, v in project_structure.items() if k != "root_files"})

print(f"Project structure created successfully at: {base_dir}")
