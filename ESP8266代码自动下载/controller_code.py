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
    earse = r"C:\Users\admin\.platformio\penv\Scripts\platformio.exe run -d C:\Users\admin\Documents\PlatformIO\Projects\CarController --target erase"
    upload_file_cmd = r"C:\Users\admin\.platformio\penv\Scripts\platformio.exe run -d C:\Users\admin\Documents\PlatformIO\Projects\CarController --target uploadfs"
    upload_code_cmd = r"C:\Users\admin\.platformio\penv\Scripts\platformio.exe run -d C:\Users\admin\Documents\PlatformIO\Projects\CarController --target upload"
    print("开始下载程序&文件")
    subprocess.run(earse, shell=True)
    subprocess.run(upload_file_cmd, shell=True)
    subprocess.run(upload_code_cmd, shell=True)


if __name__ == '__main__':
    get_serial_list("COM3")
    print("下载完毕")
    # get_serial = threading.Thread(target=get_serial_list, args=("/dev/cu.SOC",))
    # get_serial.start()

