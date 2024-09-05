def usage(script_name):
    print('usage: py' + script_name + ' <port number>')

if __name__ == "__main__":
    import sys
    import socket
    argc = len(sys.argv)
    if argc != 2:
        usage(sys.argv)
        sys.exit()
    message = sys.stdin.readline() #read from std input
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', int(sys.argv[1])))
    sock.send(message.encode())
    return_msg = sock.recv(1024)
    if return_msg:
        print('message returned: ' + return_msg.decode())
    else:
        print('Nothing returned! ')
    
    sock.close()
