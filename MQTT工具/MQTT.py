import pickle
import subprocess
try:
    import paho.mqtt.client as mqtt
except ModuleNotFoundError:
    subprocess.run("pip3 install paho-mqtt", shell=True)
    import paho.mqtt.client as mqtt
import datetime
import time


class Logger:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'

    @staticmethod
    def info(info):
        print(Logger.OKBLUE + info + Logger.ENDC)

    @staticmethod
    def warn(info):
        print(Logger.WARNING + info + Logger.ENDC)

    @staticmethod
    def error(info):
        print(Logger.FAIL + info + Logger.ENDC)


def on_connect(client, userdata, flags, rc):
    # print("Connected with result code " + str(rc))
    if rc == 0:
        Logger.info("|      连接成功        |")
        Logger.info("-----------------------")
        print("\n")
        client.subscribe("#")
        # client.subscribe("equipment")
    else:
        Logger.error("连接失败  Return Code:" + str(rc))
        time.sleep(4)
        os.remove("info.pkl")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    now = datetime.datetime.now()
    Logger.info(now.strftime('%H:%M:%S') + "   |主题|   " + msg.topic + "   |信息|   " + str(msg.payload.decode("utf-8")))
    # print("-" * len(str(msg.payload)) * 3)


def mqtt_init():
    client = mqtt.Client()
    with open("info.pkl", "rb") as f:
        con = pickle.load(f)
        uname = con[0]
        pass_word = con[1]
        host = con[2]
        port = con[3]
        Logger.info("正在连接到服务器:" + host)
        Logger.info("MQTT用户名:" + uname)
        Logger.info("MQTT密码:" + pass_word)
        Logger.info("MQTT服务器地址:" + host)
        Logger.info("-----------------------")

    mqtt_username = uname
    mqtt_password = pass_word
    HOST = host
    PORT = int(port)
    # 必须设置，否则会返回「Connected with result code 4」
    client.username_pw_set(mqtt_username, mqtt_password)
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(HOST, PORT, 60)
    except Exception as e:
        # print("无网络连接,正在等待网络连接...")
        print(e)
        # print("连接失败")

    client.loop_forever()


if __name__ == '__main__':
    import os

    if os.path.exists("info.pkl"):
        mqtt_init()
    else:
        info = []
        print("Input MQTT User Name:")
        user_name = input(">")
        info.append(user_name)
        print("Input MQTT Password:")
        psd = input(">")
        info.append(psd)
        print("Input Host Address:")
        add = input(">")
        info.append(add)
        print("Input port:")
        port = input(">")
        info.append(port)
        with open("info.pkl", "wb") as f:
            pickle.dump(info, f)
        mqtt_init()