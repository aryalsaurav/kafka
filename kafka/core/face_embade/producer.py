from kafka import KafkaProducer
import json
import random
from datetime import datetime

def generate_random_data():
    emotions = ["happy", "sad", "angry", "neutral"]
    genders = ["male", "female", "other"]

    data = {
        'id': random.randint(1, 10000000000000),
        'age': random.randint(18, 60),
        'emotion': random.choice(emotions),
        'gender': random.choice(genders),
        'timestamp': datetime.now().isoformat()
    }
    return data

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def produce_face_embed_data():
    data = generate_random_data()
    producer.send('face.embed.data', data)
    print(f'Produced: {data}')

if __name__ == "__main__":
    while True:
        produce_face_embed_data()
