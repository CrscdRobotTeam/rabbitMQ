import pika

credentials = pika.PlainCredentials("wupeiqi", "123")
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", credentials=credentials))
chanel = connection.channel()
chanel.queue_declare(queue='first')  # 消费者监听这个队列


def callback(ch, method, properties, body):
    print("消费者接收到了任务：%r" % body)


chanel.basic_consume(callback, queue='first', no_ack=True)  # 有消息立即执行callback函数，没有消息夯住
chanel.start_consuming()  # 开始消费
