import subprocess


def upload():
    subprocess.run("pio run -t uploadfs", shell=True)


if __name__ == '__main__':
    upload()
