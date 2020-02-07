import os


def check_docker_status():
    status = os.popen("systemctl show --property ActiveState docker").read()
    print ("Docker is already running...") if status == 'ActiveState=active\n' else start_docker()


def start_docker():
    print(">>> StartDocker.py script is being executed... <<<")
    os.system("systemctl start docker")
    print("Docker daemon is starting...")


if __name__ == '__main__':
    check_docker_status()
