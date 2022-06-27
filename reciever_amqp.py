import pika
import sys

AMQP_ADDRESS = "127.0.0.1"
AMQP_PORT = 35672
AMQP_USER = "guest"
AMQP_PASSWORD = "guest"
AMQP_QUEUE_NAME = "hello"


def callback(channel, method, properties, message):
    print("Received: " + message.decode())
    channel.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":

    pika_credentials = pika.PlainCredentials(AMQP_USER, AMQP_PASSWORD)
    pika_con_parm = pika.ConnectionParameters(
        AMQP_ADDRESS, AMQP_PORT, credentials=pika_credentials
    )
    pika_con = pika.BlockingConnection(pika_con_parm)
    pika_channel = pika_con.channel()

    try:
        pika_channel.queue_declare(queue=AMQP_QUEUE_NAME, passive=True)
    except pika.exceptions.ChannelClosedByBroker as ex:
        print(ex)
        exit(1)

    try:
        pika_channel.basic_consume(queue=AMQP_QUEUE_NAME, on_message_callback=callback)
        pika_channel.start_consuming()
    except KeyboardInterrupt:
        pika_con.close()
        sys.exit()
