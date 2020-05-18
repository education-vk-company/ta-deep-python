import time
import threading

COUNT = 10_000_000

def execute(n):
    while n > 0:
        n -= 1

if __name__ == "__main__":
    start_ts = time.time()
    execute(COUNT)
    end_ts = time.time()
    print("Время выполнения {}".format(end_ts - start_ts))

    start_ts = time.time()
    thread1 = threading.Thread(target=execute, args=(COUNT//2,))
    thread2 = threading.Thread(target=execute, args=(COUNT//2,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end_ts = time.time()
    print("Время выполнения 2 потока: {}".format(end_ts - start_ts))
