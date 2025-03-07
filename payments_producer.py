import json
import random
import uuid
from datetime import datetime, timedelta
from kafka import KafkaProducer

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='',
    security_protocol='SASL_SSL',
    sasl_mechanism='PLAIN',
    sasl_plain_username='',
    sasl_plain_password='',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Function to generate payment data
def generate_payment(order_id, payment_id):
    return {
        "payment_id": payment_id,
        "order_id": order_id,
        "payment_date": str((datetime.now() - timedelta(minutes=random.randint(0, 30))).isoformat()),
        "created_at": str(datetime.now().isoformat()),
        "amount": random.randint(50, 500)
    }

# Specify order_id and publish a single payment
order_id = "order_1"
payment_id = str(uuid.uuid4())

try:
    payment = generate_payment(order_id, payment_id)
    producer.send('payments_topic_data_v1', value=payment)
    print(f"Sent payment: {payment}")
finally:
    producer.flush()
    producer.close()