from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    dato = {
        "precio": random.randint(100000,500000),
        "habitaciones": random.randint(1,5)
    }

    producer.send('viviendas', dato)
    print(dato)

    time.sleep(2)