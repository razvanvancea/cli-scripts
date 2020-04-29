import os


def cancel_shutdown():
    os.system("shutdown -c")
    print(">>> Shutdown scheduler has been stopped.")


if __name__ == '__main__':
    cancel_shutdown()
