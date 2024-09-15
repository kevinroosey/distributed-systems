# Threading: Overview

When a process is created, it is provided with a main thread. This thread is scheduled to run by the kernel


If a program has only the one single main thread, a connected socket cannot send and receive at the same time. Instead, the socket must complete each send and receive operation before beginning another.

Although there are async methods for sending and receiving data simultaneously, synchronous comms can avoid blocking by using separate threads for sending and recieving.

Because a program has a main thread when created, one additional thread
must be created in order to permit a socket to send and receive data at the
same time.


## Threading: Python

The threading module must be imported.
The threading.Thread class is used to create threading objects.
Typically, the threading.Thread class is used as a base class for a derived
class that overrides the run method.
The run method has no parameters and does not return a value. Hence,
in order to pass arguments to the thread, they must be specified in the constructor.
The start method of the Thread object launches the thread.
The Python 3.5 API for threading is contained in the Python Library at
“17.1. threading — Thread-based parallelism”

## Threading: Exiting a multi-threaded process
` sys.exit() ` will only exit the current thread
` os._exit() ` must be used to kill the program, no matter how many threads have been created

