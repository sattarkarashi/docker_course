import os
import time

# An orphan process is a process whose parent process has finished or terminated, though it remains running itself.
#  Orphan processes are usually adopted by the init process, which is the first process started when a Linux system boots up.

def create_orphan_process():
    pid = os.fork()
    if pid == 0:
        print("Child process")
        time.sleep(30)
        print("Child process exiting")
    else:
        print("Parent process")
        time.sleep(10)
        print("Parent process exiting")

if __name__ == "__main__":
    create_orphan_process()
# In the above code, the parent process will sleep for 10 seconds and the child process will sleep for 30 seconds.
# The child process will exit after the parent process.