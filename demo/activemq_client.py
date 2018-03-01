import time

import stomp


class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)


# 连接到服务器
conn = stomp.Connection(host_and_ports=[('localhost', 61613)])
# 有消息的时候触发
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', 'admin', wait=True)

# 订阅
conn.subscribe(destination='/queue/test', id=1, ack='auto')

# 发送消息
for times in range(100):
    conn.send(body='Hello World! Times: ' + str(times), destination='/queue/test')

time.sleep(2)
conn.disconnect()
