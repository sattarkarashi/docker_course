import os
import time
# A zombie process is a process that has completed execution but still has an entry in the process table. Zombie processes usually occur for child processes, as the parent process still needs to read its child's exit status. Once the exit status is read via the wait system call, the zombie process is removed.


def create_zombie_process():
    pid = os.fork()
    if pid == 0:
        print("Child process")
        time.sleep(2)
        print("Child process exiting")
    else:
        print("Parent process")
        time.sleep(30)
        print("Parent process exiting")

# In the above code, the parent process will sleep for 30 seconds and the child process will sleep for 2 seconds. The child process will exit before the parent process.
#  The child process will become a zombie process as the parent process will not read the exit status of the child process.
#  The child process will be removed from the process table once the parent process exits.