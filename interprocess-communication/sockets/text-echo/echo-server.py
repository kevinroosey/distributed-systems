#Echo cursor


def usage(script_name):
    print('usage: py ' + script_name + ' <port number>')

if __name__ == "__main__":
    import sys
    import socket
    argc = len(sys.argv)
    if argc != 2:
        usage(sys.argv[0])
        sys.exit()
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('', int(sys.argv[1])))
    serversocket.listen(5)
    sock, addr = serversocket.accept()
    serversocket.close()
    msg_bytes = sock.recv(1024)
    sock.send(msg_bytes)
    sock.close()
