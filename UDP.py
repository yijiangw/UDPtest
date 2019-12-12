import socket

# 创建socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 56789))  # 连接到另一个socket
    num = 0
    while True:
        data = s.recv(65565)  # 65535是一次性能接收的最大值    
        print('Received', str(data))  # 打印收到的数据
        num += 1
        if num >100 :
            break
        