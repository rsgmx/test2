import socketserver, threading, time

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
cnt         = 0


class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data   = str( self.request[0].strip(), 'utf-8')
        socket = self.request[1]
        current_thread = threading.current_thread()
        print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address, data))
        global cnt
        cnt += 1
        s = (str(data.upper())+" {}").format( cnt)
        print ( s)
        socket.sendto( s.encode('utf-8')  , self.client_address)

class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass

if __name__ == "__main__":

    server = ThreadedUDPServer((localIP, localPort), ThreadedUDPRequestHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True

    try:
        server_thread.start()
        print("Server started at {} port {}".format(localIP, localPort))
        while True: time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        exit()