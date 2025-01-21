import asyncio
from kafka_consumer import consume_messages


async def main():
    await consume_messages()


if __name__ == "__main__":
    asyncio.run(main())
