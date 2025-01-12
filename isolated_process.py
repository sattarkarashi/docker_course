import os

def run():
    pid = os.fork()

    if pid == 0:
        print("Child process")
        os.execvp(file="/bin/bash", args=["bash"])

    else:
        rid, status = os.waitpid(pid, 0)
        print(rid, status)
        print("Parent process")


if __name__ == "__main__":
    run()