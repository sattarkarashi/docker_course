import os
import ctypes

libc = ctypes.CDLL("libc.so.6", use_errno=True)
CLONE_NEWNS = 0x00020000


def unshare_ns(flags):
    result = libc.unshare(flags)
    if result < 0:
        errno = ctypes.get_errno()
        raise OSError(errno, os.strerror(errno))

        
def run():
    pid = os.fork()
    print("Starting process")
    print(pid)

    if pid == 0:
        print("Child process")
        unshare_ns(CLONE_NEWNS)
        os.system("mount -t proc none /home/sato/what_I_learned_today/docker/docker_course/myroot/proc")
        # Change root directory
        # print(os.getcwd())
        os.chroot("/home/sato/what_I_learned_today/docker/docker_course/myroot")
        os.chdir("/")
        # os.chdir("/")
        os.execvp(file="/bin/busybox", args=["/bin/busybox", "sh"])

    else:
        rid, status = os.waitpid(pid, 0)
        os.system("umount /home/sato/what_I_learned_today/docker/docker_course/myroot/proc")
        print(rid, status)
        print("Parent process")
    
    print("Finishing process")


if __name__ == "__main__":
    run()