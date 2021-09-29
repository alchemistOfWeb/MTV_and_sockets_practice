import socket, urls

class Server:
    __instance = None
    listener_count = 5
    host = '127.0.0.1'
    port = 8000


    def __init__(self, *args, **kwargs) -> None:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(self.listener_count)


    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = Server(args, kwargs)

        return cls.__instance
            

    def run(self):
        try:            
            print('Working...')

            while True:
                self.update()
                            
        except KeyboardInterrupt:
            self.server.close()
            print('\nshutdown the server')

    def update(self):
        client_socket, adress = self.server.accept()
        data = client_socket.recv(1024).decode('utf-8')
        print(data)
        
        HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        response_body = self.handle_request(data).encode('utf-8')
        client_socket.send(HDRS.encode('utf-8') + response_body)
        client_socket.shutdown(socket.SHUT_WR)


    def handle_request(self, request_data:str) -> str:
        path = request_data.split(' ')[1]
        uri = path
        handler = urls.urlpatterns.get(uri)
        

        if hasattr(handler, '__class__') \
            and handler.__class__.__name__ == 'function':
            response = handler()
            return response

        return '404:Not found'


    
