import pika
import sys

AMQP_ADDRESS = "127.0.0.1"
AMQP_PORT = 35672
AMQP_USER = "guest"
AMQP_PASSWORD = "guest"
AMQP_QUEUE_NAME = "hello"


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

    if len(sys.argv) > 1:
        msg = sys.argv[1]
    else:
        msg = "Hello world!!"

    pika_channel.basic_publish(exchange="", routing_key=AMQP_QUEUE_NAME, body=msg)
    pika_con.close()
