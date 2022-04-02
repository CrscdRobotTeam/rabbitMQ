# 1.消息队列
"""
1）Queue:将数据存到当前服务器的内存。
2）redis：列表，缓存。
3）rabbitMQ（专业做消息队列）：数据是安全的、稳定的、持久的，客户端、服务端挂掉数据不会丢失。
4）kafka（专业做消息队列）：分布式、存储或发送数据的效率高，
5）zeroMQ：把消息存在内存，是执行效率最高的一种消息队列方式
6）saltstack:
    --ssh:安装方便、执行效率低
    --agent:执行效率高（基于消息队列zeroMQ做的RPC）
"""
# 2.什么时候用消息队列
"""
1）任务处理：请求的数量太多了，需要把消息临时存放到某个地方，存放的是任务；
2）发布订阅：一旦发布消息，所有订阅者都会收到一条相同的消息；
"""
# 3.rabbitMQ安装
"""
服务端安装：
1）安装配置epel源：
    $ rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
2)安装erlang(rabbitMQ是基于erlang语言开发的)：
    $ yum -y install erlang
3)安装rabbitMQ：
    $ yum -y install rabbitmq-server
4）启动(无用户名和密码)：
    $ service rabbitmq-server start/stop
5）设置用户名和密码：
    $ sudo rabbitmqctl add_user wupeiqi 123
6)设置用户的角色：
    $ sudo rabbitmqctl set_user_tags wupeiqi administrator
7)设置权限：
    $ sudo rabbitmqctl set_permissions -p "/" root ".*" ".*" ".*"
8)启动：
    $ service rabbitmq-server start/stop
客户端安装：
    pip install pika
"""
# 4.rabbitMQ快速使用

# 生产者
import pika

# 无密码：
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # 创建链接
# 有密码：
credentials = pika.PlainCredentials("wupeiqi", "123")
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))  # 创建链接
channel = connection.channel()

# 声明一个队列（创建一个队列）
channel.queue_declare(queue='first')  # 不存在名字为first的队列新创建，否则用原来的
channel.basic_publish(exchange='', routing_key='first',
                      body='maskdaksdjasdhajsd')  # 往队列中发送数据 routing_key：队列名称 、body：发送的数据

connection.close()
