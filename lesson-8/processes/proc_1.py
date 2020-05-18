import os
from multiprocessing import Process

def print_info(name):
    print(f"Process {name}, pid={os.getpid()}, parent pid={os.getppid()}")

if __name__ == "__main__":
    print_info("main")
    processes = [Process(target=print_info, args=(f"child{i}",)) for i in range(1, 5)]
    for proc in processes:
        proc.start()
    for proc in processes:
        proc.join()

