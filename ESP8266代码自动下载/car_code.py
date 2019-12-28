# try:
#     import esptool
# except ImportError:
#     import subprocess
#     subprocess.run("pip install esptool", shell=True)
import serial
import serial.tools.list_ports
import threading
import subprocess
import time
# import esptool
import json


def get_serial_list(port_name):
    # while True:
    port_list = list(serial.tools.list_ports.comports())
    for i in port_list:
        if port_name == i.device:
            upload()


def upload():
    """
            使用esptools模式
            port = "COM3"
            baud = 115200
            file_path = "tcpcar.bin"
            upload_code_cmd = "esptool.py --port {0} --baud {1} write_flash -fm dio -fs 32m 0x00000 {2}".format(port, baud, file_path)
        """
    # 使用pio上传
    earse = r"C:\Users\admin\.platformio\penv\Scripts\platformio.exe run -d E:\ArduinoCode\TCPCar --target erase"
    upload_file_cmd = r"C:\Users\admin\.platformio\penv\Scripts\platformio.exe run -d E:\ArduinoCode\TCPCar --target uploadfs"
    upload_code_cmd = r"C:\Users\admin\.platformio\penv\Scripts\platformio.exe run -d E:\ArduinoCode\TCPCar --target upload"
    print("开始下载程序&文件")
    subprocess.run(earse, shell=True)
    subprocess.run(upload_file_cmd, shell=True)
    subprocess.run(upload_code_cmd, shell=True)
    
    # 暂时没有获取设备唯一标识码,使用延时等待下一个设备
    # time.sleep(5)


if __name__ == '__main__':
    ssid = "toddler-1"
    password = ssid
    com = "COM3"
    data = {
            "ssid": ssid,
            "password": password
        }
    data = json.dumps(data)
    with open(r'E:\ArduinoCode\TCPCar\data\wifi.json', 'w') as f:
        f.write(data)
    with open(r"C:\Users\admin\Documents\PlatformIO\Projects\CarController\data\wifi.json", 'w') as f:
        f.write(data)
    get_serial_list("COM3")
    print("下载完毕")

