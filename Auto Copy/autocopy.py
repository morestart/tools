from time import sleep
import shutil
import os
from psutil import disk_partitions
import threading


class MoveToUsb:
    def __init__(self, music_dir_path):
        self.musicDirPath = music_dir_path
        self.musicPathList = []
        self.usbIndex = []

    def get_file_name(self):
        for root, dirs, files in os.walk(self.musicDirPath):
            for file in files:
                self.musicPathList.append(os.path.join(root, file))

    def get_usb_index(self):
        for item in disk_partitions():
            if 'removable' in item.opts:
                driver, opts = item.device, item.opts
                print('可移动存储器:' + driver)
                if driver not in self.usbIndex:
                    self.usbIndex.append(driver)
            else:
                print('没有找到可移动驱动器')

    def move_music(self):
        print(self.usbIndex)
        for file in self.musicPathList:
            for usb in self.usbIndex:
                try:
                    shutil.copy(file, usb)
                except IOError as e:
                    print("Unable to copy file. %s" % e)
        print('文件复制成功')
        self.usbIndex.clear()


if __name__ == '__main__':
    move = MoveToUsb("C:\\Users\\admin\\Desktop\\Map Music Data")
    move.get_file_name()
    while True:
        move.get_usb_index()
        move.move_music()
