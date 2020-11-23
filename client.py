import socket
from random import randint
from time import sleep

class Client:
	def process(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = socket.gethostname()
		port = 9999
		remote_ip = socket.gethostbyname(host)
		s.connect((remote_ip , port))

		sleep(randint(5, 10))
		s.sendall(b"hello")
		print('message sent')
		s.close()

if __name__ == "__main__":
    client = Client()
    client.process()
