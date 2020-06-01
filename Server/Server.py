import socket


class Server:

    def __init__(self, port, handle_message):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.handle_message = handle_message
        self.server_address = ('localhost', port)
        self.server_socket.bind(self.server_address)

    """ starts to listen for clients """
    def listen(self):
        while True:
            try:
                message, client_address = self.server_socket.recvfrom(4096)
                answer = self.handle_message(message)
                self.send(answer, client_address)
            except:
                continue

    """ sends a message to the given address """
    def send(self, message, address):
        self.server_socket.sendto(bytes(message, encoding="utf-8"), address)
