from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_data():
    for i in range(100):
        message = {"id": i, "value": i * 2}
        producer.send("data_topic", message)
        print(f"Sent: {message}")

if __name__ == "__main__":
    generate_data()
