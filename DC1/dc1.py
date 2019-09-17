import socket


ssid = input("请输入待连接的WiFi SSID（仅支持2.4G）: ")
password = input("请输入待连接的WiFi密码: ")
send_data = "{\"header\":\"phi-plug-0001\",\"uuid\":\"00010\",\"action\":\"wifi=\",\"auth\":\"\",\"params\":{\"ssid\":\""+ssid+"\",\"password\":\""+password+"\"}}\n"
for i in range(5):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(send_data.encode("utf-8"), ("192.168.4.1", 7550))
    udp_socket.close()
print("发送配网数据成功...")
