import json
from kafka import KafkaProducer
import pandas as pd

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: json.dumps(x).encode('utf-8'))

def stream_data(file_path):
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        producer.send('atlas-data', value=row.to_dict())
        print(f"Sent: {row.to_dict()}")

if __name__ == "__main__":
    stream_data('data/raw/ATLAS-top-tagging/your_dataset.csv')
