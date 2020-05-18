import time
import requests
import threading

session = None

def init_session():
    global session
    if not session:
        session = requests.Session()

def download_url(url, thread_id=0):
    with session.get(url) as response:
        time.sleep(0.1)
        print(f"Threading #{thread_id} finished for url [{url}]")

def download_all_urls(urls, thread_id=0):
    init_session()
    for url in urls:
        download_url(url, thread_id)

if __name__ == "__main__":
    urls = ["http://python.org", "http://toshcorp.ru/coins/"] * 10

    start_ts = time.time()
    download_all_urls(urls)
    end_ts = time.time()
    print("Время работы {}".format(end_ts - start_ts))

    threads = [threading.Thread(target=download_all_urls, args=(urls[:2],i)) for i in range(5)]
    start_ts = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_ts = time.time()
    print("Время работы {} потоков {}".format(len(threads), end_ts - start_ts))



