import os
import sys


def check_docker_is_running():
    print("Checking if docker is running...")
    status = os.popen("systemctl show --property ActiveState docker").read()
    print("Checked! Docker is already running...") if status == 'ActiveState=active\n' else start_docker()


def start_docker():
        os.system("systemctl start docker")
        print("Docker daemon is starting...")


def pull_images_and_start_zalenium(containers):
    print("--- Pulling docker-selenium---")
    os.system("docker pull elgalu/selenium")
    print("--- Pulling Zalenium ---")
    os.system("docker pull dosel/zalenium")
    print("--- Running Zalenium with " + containers + " containers---")
    os.system("docker run --rm -ti --name zalenium -p 4444:4444 \
              -v /var/run/docker.sock:/var/run/docker.sock \
              -v /tmp/videos:/home/seluser/videos \
              --privileged dosel/zalenium start --desiredContainers " + containers)


def verify_zalenium_params():
    if len(sys.argv) >= 2:
        container_number = sys.argv[1]
        if container_number.isnumeric():
            check_docker_is_running()
            pull_images_and_start_zalenium(container_number)
        else:
            print("ERROR! Please use a number!")
    else:
        containers = input("Insert the number of containers:")
        if containers.isnumeric():
            check_docker_is_running()
            pull_images_and_start_zalenium(containers)
        else:
            print("ERROR! Please use a number!")


if __name__ == '__main__':
    verify_zalenium_params()

