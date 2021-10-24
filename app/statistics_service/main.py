from fastapi import FastAPI
import pika


class RabbitMessageBroker:
    def __init__(self, host: str, port: int):
        self.parameters = pika.ConnectionParameters(host, port)
        self.connection = pika.BlockingConnection(self.parameters)

    def receive(self, queue: str) -> bytes:
        channel = self.connection.channel()
        _, _, message = next(channel.consume(queue))
        channel.close()
        return message


app = FastAPI()

message_broker = RabbitMessageBroker(host="0.0.0.0", port=5672)


@app.get("/get/statistics/")
async def get_statistics() -> str:
    message = message_broker.receive("creation_queue")
    return message.decode("utf8")
