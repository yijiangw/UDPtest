import socket
import struct
# 创建socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(("192.168.33.30", 4098))
    num = 0
    d = []
    while True:
        data = s.recvfrom(65565)  # 65535是一次性能接收的最大值
        d.append(data)
        # print(data[0])
        packet = []
        # print(len(data[0]))
        # print(data[0][1])
        num += 1
        if num >100 :
            break
        # for i in range(len(data[0])):
            # packet.append(struct.unpack('BBBB',data[0][i]))

        
        # print('Received', str(data))  # 打印收到的数据
    for x in range(100):
        data = d[x]
        print(len(data[0]))
        print("     ")
        for i in range(100):
            print('packet', data[0][i])
        
        
