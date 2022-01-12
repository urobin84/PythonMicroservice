import json
import pika

params = pika.URLParameters('amqps://eaknepmg:BVe14byoa4YSPXVeAQasmj7N1xBYrFaE@fox.rmq.cloudamqp.com/eaknepmg')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
