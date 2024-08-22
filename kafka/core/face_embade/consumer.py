import os
import django
import sys

sys.path.append('/Users/sauravaryal/Developer/interview/kafka/core')
# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Set up Django
django.setup()


from kafka import KafkaConsumer
import json
from face_embade.models import FaceEmbade
from django.utils import timezone
from django.db.utils import IntegrityError
from datetime import datetime



def consume_face_embed_data():
    consumer = KafkaConsumer(
        'face.embed.data',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    for message in consumer:
        data = message.value
        try:
            FaceEmbade.objects.create(
                id=data['id'],
                age=data['age'],
                emotion=data['emotion'],
                gender=data['gender'],
                timestamp=datetime.fromisoformat(data['timestamp'])
            )
        except IntegrityError:
            print("Data not stored due to Integrity error")
        print(f"Consumed and stored: {data}")


if __name__ == "__main__":
    consume_face_embed_data()
