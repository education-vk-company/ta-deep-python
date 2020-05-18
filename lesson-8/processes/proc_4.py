import time
import requests
from multiprocessing import Process, Queue, Lock

session = None
lock = Lock()

def init_session():
    global session
    if not session:
        session = requests.Session()

def download_url(url, session_tmp, thread_id=0):
    with lock:
        with session.get(url) as response:
            print(f"Threading #{thread_id} finished for url [{url}]")
    time.sleep(0.1)

def download_all_urls(urls, thread_id=0):
    init_session()
    for url in urls:
        download_url(url, session, thread_id)

def download_all_urls_proc(queue, proc_id=0):
    session_tmp = requests.Session()
    while not queue.empty():
        url = queue.get()
        download_url(url, session_tmp, proc_id)

if __name__ == "__main__":
    urls = ["http://python.org", "http://toshcorp.ru/coins/"] * 10

    start_ts = time.time()
    download_all_urls(urls)
    end_ts = time.time()
    print("Время работы {}".format(end_ts - start_ts))

    q = Queue()
    for url in urls:
        q.put(url)

    procs = [Process(target=download_all_urls_proc, args=(q, i)) for i in range(5)]
    start_ts = time.time()
    for proc in procs:
        proc.start()
    for proc in procs:
        proc.join()
    end_ts = time.time()
    print("Время работы {} процессов {}".format(len(procs), end_ts - start_ts))



