# Synchronous Communication using Sockets: Overview

Communication occurs over a virtual connection.
Virtual connection is formed between two programs, which may be running on the
same computer or different hosts.


## Steps for creating this connection:
    1. Server listens for a client to request a connection.
    2. Client attempts to connect, i.e., request a connection.
    3. Server accepts the connection.

Using the connection, client and server send and receive data at will.
When communication is finished, the connection is closed on each end.
The system library that handles the setting up and tearing down of connections, as well as the transmission of data, is known as the socket library. A socket is an operating system supplied object that permits the sending and receiving of packets over a network connection.

## Creating a client socket:
    1. Determine the address and port number of the server you wish to connect to.
        * For purposes of this class, we will connect programs running on the same host.
    2. Import the socket module and call the socket function, which returns a socket object.
        * This function can receive configuration information about the type of socket to be created.
        * By default, it creates a TCP/IP socket
    3. Using the newly-created socket object, call the connect method, passing in the name or address of the server and the port number that the server is listening on. If a connection cannot be established, such as because the server isn't running, then an exception is raised.

## Creating a server socket:
    1. Determine the port number that you want the server to listen on.
    2. Import the socket module and call the socket function.
    3. Bind the socket to the port number using the bind method of the socket object.
        * This function takes an address tuple as its sole argument.
    4.  Permit the socket to receive connection requests by calling the listen methodon the socket object.
    5. Once the socket receives a connection request, call the accept method, which returns a tuple containing a new socket and the address of the client that is
    connected.
        * The new socket is used to communicate with the client program.
        * The server socket is not longer needed.

## Sending and receiving data
    1. The socket method send is used to send bytes to the other end of the connection.
        * The first argument passed to the send method is a bytes object containing the bytes
    to send.
        * This method returns the number of bytes actually sent.
    2. The socket method recv is used to receive bytes from the other end of the connection.
        * This method returns a bytes object.
        * It has one mandatory parameter, the maximum number of bytes that can be received
        in one call to the method.
    3. A string sequence can be converted into a bytes sequence using the encode method
    on the string object.
        * By default, this method converts the string into a utf-8 bytes sequence, but that
        assumption can be overridden using an argument to the call.
    4. A bytes sequence received by the socket can be converted to a string by using the
    decode method on the bytes object.
        * By default, this method assumes that the bytes object represents utf-8 encoding,
        but that assumption can be overridden using an argument to the call.

## Shutting down a client socket
    Three steps to shut down a client socket
    1. The output portion (a.k.a, output stream)  of the socket is shut down
    2. The input stream of the socket is shut down
    3. The memory allocated for the socket is released

    The output stream is shut down by one socket sending a packet to the other
    endpoint that contains a TCP/IP header but no data. This packet is
    commonly referred to as a zero-length message. More on this later….
    The socket library contains functions that shut down output and input, as well as
    release the socket resource.
    Although you can call any or all of these functions, only the functions that shut down
    output and input are guaranteed to work immediately.
    The close function merely schedules the release of the socket; it is up to the
    programming language library to determine when to execute.
    Nonetheless, calling close will also shut down the socket, if the streams are still
    functioning.

## Shutting down a server socket
    The server, or listening, socket is dedicated to listening for connection requests
    and accepting them; it cannot send or receive data.
    Tearing down the listening socket and releasing it back to the operating system
    requires two steps:
    1. The socket is unbound from the listening port
    2. The memory allocated for the socket is released
    The close function performs both steps.
    The listening port number becomes available to the system again once all
    sockets using it have been closed or in a state wherein the port can be reused.

## Library functions for shutting down sockets
    socket.shutdown( how )
    * how may be SHUT_RD, SHUT_WR, or SHUT_RDWR
    socket.close( )
    
    * Note: Python does not always close a socket when you call the close function!
    Instead, close merely schedules the socket for closing (when the system library
    is good and ready).
    In order to let the other side know immediately that you are closing a client socket,
    call shutdown directly
