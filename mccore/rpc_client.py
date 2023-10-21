import pika


class RPCClient:
    
    def __init__(self, host:str='localhost', queue:str='mccore'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue)

    def call():
        pass 

    def close_connection(self):
        self.connection.close()