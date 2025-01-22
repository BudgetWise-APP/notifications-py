from aiokafka import AIOKafkaConsumer
from email_service import send_email
from config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
from models import NotificationModel
import json


async def consume_messages():
    try:
        consumer = AIOKafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            group_id="notifications_service",
        )

        await consumer.start()
        print("Kafka Consumer started. Listening for messages...")
        try:
            async for msg in consumer:
                try:
                    data = json.loads(msg.value)
                    notification = NotificationModel(**data)
                    subject = "New crypto coin added!"
                    body = (
                        f"Hello,\n\nA new record with {notification.message} has been created."
                    )
                    print(data)
                    print(subject)
                    print(body)
                    await send_email(notification.user_email, subject, body)
                    print(f"Notification sent to {notification.user_email}")
                except Exception as e:
                    print(f"Error processing message: {e}")
        finally:
            await consumer.stop()
    except Exception as e:
        print(f"Error consuming messages: {e}")
