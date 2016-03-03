Title: 试试看Python代码块
Date: 2016-03-03 17:40:14
Category: Blog

刚才调整了一下代码块的显示，现在决定写一点Python测试代码来试试看效果

    :::python
    """
    Complex example which is a combination of the rr* examples from the zguide.
    """
    from gevent.monkey import patch_all
    patch_all()
    
    from gevent import spawn
    import zmq.green as zmq
    
    # server
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect("tcp://localhost:5560")
    
    def serve(socket):
        while True:
            message = socket.recv(copy=False)
            print "Received request: ", message
            socket.send("World", copy=False)
    server = spawn(serve, socket)
    
    
    # client
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5559")
    
    #  Do 10 requests, waiting each time for a response
    def client():
        for request in range(1,10):
            socket.send("Hello", copy=False)
            message = socket.recv(copy=False)
            print "Received reply ", request, "[", message, "]"
    
    
    # broker
    frontend = context.socket(zmq.ROUTER)
    backend  = context.socket(zmq.DEALER);
    frontend.bind("tcp://*:5559")
    backend.bind("tcp://*:5560")
    
    def proxy(socket_from, socket_to):
        while True:
            m = socket_from.recv_multipart()
            socket_to.send_multipart(m)
    
    a = spawn(proxy, frontend, backend)
    b = spawn(proxy, backend, frontend)
    
    spawn(client).join()
