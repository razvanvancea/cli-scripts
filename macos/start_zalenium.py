import os
import sys


def pull_images_and_start_zalenium(containers):
    print("--- Pulling docker-selenium---")
    os.system("docker pull elgalu/selenium")
    print("--- Pulling Zalenium ---")
    os.system("docker pull dosel/zalenium")
    print("--- Running Zalenium with " + containers + " containers---")
    os.system("docker run --rm -ti --name zalenium -p 4444:4444 \
      -e DOCKER=17.06.2-ce \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v /tmp/videos:/home/seluser/videos \
      --privileged dosel/zalenium start --desiredContainers " + containers)


def verify_zalenium_params():
    if len(sys.argv) >= 2:
        container_number = sys.argv[1]
        if container_number.isnumeric():
            pull_images_and_start_zalenium(container_number)
        else:
            print("ERROR! Please use a number!")
    else:
        containers = input("Insert the number of containers:")
        if containers.isnumeric():
            pull_images_and_start_zalenium(containers)
        else:
            print("ERROR! Please use a number!")


if __name__ == '__main__':
    verify_zalenium_params()

