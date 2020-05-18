from multiprocessing import Process, Array
from ctypes import c_char_p

def process_handler(i, array, result):
    print(f"Process #{i}. Adding {array[i][-1::-1]} to result")
    result[i] = array[i][-1::-1]

if __name__ == "__main__":
    result = Array(c_char_p, 3)
    input_array = ["Jesse", "Walter", "Soul"]
    procs = [Process(target=process_handler, args=(i, input_array, result)) for i in range(3)]
    for proc in procs:
        proc.start()
    for proc in procs:
        proc.join()
    print("Result", result[:])
