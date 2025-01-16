import os

def run():
    pid = os.fork()
    print("Starting process")
    print(pid)

    if pid == 0:
        print("Child process")
        # Change root directory
        print(os.getcwd())
        os.chroot("/home/sato/what_I_learned_today/docker/docker_course/myroot")
        os.chdir("/")
        os.execvp(file="/bin/bash", args=["/bin/bash"])

    else:
        rid, status = os.waitpid(pid, 0)
        print(rid, status)
        print("Parent process")
    
    print("Finishing process")


if __name__ == "__main__":
    run()