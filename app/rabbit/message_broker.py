import pika


class RabbitMessageBroker:
    def __init__(self, host: str, port: int):
        self.parameters = pika.ConnectionParameters(host, port)
        self.connection = pika.BlockingConnection(self.parameters)

    def publish(self, exchange: str, routing_key: str, body: bytes):
        with self.connection.channel() as channel:
            channel.basic_publish(exchange, routing_key, body)

    def receive(self, queue: str) -> bytes:
        channel = self.connection.channel()
        _, _, message = next(channel.consume(queue))
        channel.close()
        return message
