import zmq

context = zmq.Context()

print("Connecting to hello world server…")

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for times in range(10):
    print("Sending request %s …" % times)
    socket.send(b"Hello")

    message = socket.recv()
    print("Received reply %s [ %s ]" % (times, message))
