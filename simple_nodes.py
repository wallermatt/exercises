'''
1. Node input and output
2. Node start and stop
3. loop, listen for messages/events
4. message queue
'''

class Network:

    def __init__(self, nodes=None):
        if not nodes:
            self.nodes = []
        else:
            self.nodes = nodes
        self.msg_queue = []

    def add_node(self, node):
        self.nodes.append(node)

    def mail_message(self, msg):
        for n in self.nodes:
            if msg.recipients == msg.ALL_NODES or n.node_id in msg.recipients:
                n.receive_msg(msg)

    def add_msg_queue(self, msg):
        for n in self.nodes:
            msg = n.send_msg()
            if msg:
                self.msg_queue.append(msg)

    def process_msg_queue(self):
        while self.msg_queue:
            self.mail_message(self.msg_queue.pop())

    def one_cycle(self):
        self.add_msg_queue()
        self.process_msg_queue()

    def yield_nodes(self):
        for n in self.nodes:
            yield n


class Msg:

    ALL_NODES = 'ALL_NODES'
    
    def __init__(self, sender, body, recipients=ALL_NODES):
        self.sender = sender
        self.body = body
        self.recipients = recipients


class Node:

    def __init__(self, node_id):
        self.node_id = node_id
        self.running = False
        self.sent_message = None

    def start(self):
        if not self.running:
            self.running = True
            print(f"Node {self.node_id} STARTED...")
        else:
            print(f"Node {self.node_id} already running!")

    def stop(self):
        if self.running:
            self.running = False
            print(f"Node {self.node_id} STOPPED")
        else:
            print(f"Node {self.node_id} NOT running!")

    def receive_msg(self, msg):
        print(f"Node {self.node_id} RECEIVED message from: {msg.sender}, body: {msg.body}")

    def create_send_msg(self, body, recipients):
        msg = Msg(self.node_id, body, recipients)
        self.sent_message = msg
        print(f"Node {self.node_id} CREATED message: {msg.body}")

    def send_msg(self):
        msg = self.sent_message
        self.sent_message = None
        return msg

