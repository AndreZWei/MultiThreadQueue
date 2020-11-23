import threading
import socket
import _thread

class MainThread:
    def __init__(self):
        self.queue = []

    def listen(self):
        HOST = socket.gethostname()
        PORT = 9999

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(10)

        cv = threading.Condition()
        for i in range(3):
            conn, addr = s.accept()
            _thread.start_new_thread(self.clientthread, (conn, cv))
        
        with cv:
            while not len(self.queue) == 3:
                print("Current Queue Size: " + str(len(self.queue)))
                print("Waiting")
                cv.wait()
        print("Queue is full!")

        s.close()


    def clientthread(self, conn, cv):
        while True:
            timeout = 1
            try:
                packet = conn.recv(4096)
                if packet:
                    with cv:
                        self.queue.append(packet)
                        cv.notify()
            except:
                pass
        conn.close()

if __name__ == "__main__":
    main_thread = MainThread()
    main_thread.listen()


